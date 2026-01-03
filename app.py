import importlib.util
import inspect
import io
import json
import traceback
from typing import Optional

import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Mapping of presets to file paths
PRESETS = {
    "Exp1 (compassionate)": "Exp1.py",
    "Exp2": "Exp2.py",
    "RUN#C1": "RUN#C1.py",
    "RUN#C2 (coercive)": "RUN#C2.py",
}


def load_module_from_path(path: str):
    spec = importlib.util.spec_from_file_location("sim_module", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_attractor(text: str, num_dims: int) -> Optional[np.ndarray]:
    if not text:
        return None
    text = text.strip()
    if text.lower() in ("none", "auto", "", "default"):
        return None
    try:
        parts = [p.strip() for p in text.split(",") if p.strip()]
        if len(parts) == 1 and ("linspace" in parts[0].lower() or ":" in parts[0]):
            # support simple ranges like 0.2:0.9 or linspace(0.2,0.9)
            if ":" in parts[0]:
                a, b = parts[0].split(":")
                vals = np.linspace(float(a), float(b), num_dims)
                return vals
            if "linspace" in parts[0].lower():
                inside = parts[0].split("(", 1)[1].rstrip(")")
                a, b = [float(x) for x in inside.split(",")[:2]]
                return np.linspace(a, b, num_dims)
        vals = [float(p) for p in parts]
        if len(vals) != num_dims:
            st.warning(f"Provided attractor length {len(vals)} != num_dims ({num_dims}). Will pad/truncate.")
            arr = np.zeros(num_dims)
            for i, v in enumerate(vals[:num_dims]):
                arr[i] = v
            return arr
        return np.array(vals, dtype=float)
    except Exception as e:
        st.error(f"Could not parse attractor: {e}")
        return None


def run_selected_simulation(path: str, params: dict):
    module = load_module_from_path(path)
    if not hasattr(module, "run_simulation"):
        raise AttributeError("Selected module does not expose run_simulation(...) function")
    func = module.run_simulation

    sig = inspect.signature(func)
    call_kwargs = {}
    for name in sig.parameters.keys():
        if name in params:
            call_kwargs[name] = params[name]

    # Call function
    return func(**call_kwargs)


def main():
    st.set_page_config(page_title="Emergent Attractor Explorer", layout="wide")
    st.title("Emergent Attractor Framework — Explorer 🔧")

    with st.sidebar:
        st.header("Simulation settings")
        preset = st.selectbox("Experiment preset", list(PRESETS.keys()))

        num_agents = st.number_input("num_agents", value=500, min_value=10, max_value=5000, step=10)
        num_dims = st.number_input("num_dims", value=21, min_value=2, max_value=100, step=1)
        timesteps = st.number_input("timesteps", value=1000, min_value=1, max_value=100000, step=10)

        idea_strength = st.number_input("idea_strength", value=0.02, step=0.005, format="%.4f")
        social_strength = st.number_input("social_strength", value=0.03, step=0.005, format="%.4f")
        noise_level = st.number_input("noise_level", value=0.01, step=0.005, format="%.4f")

        attractor_text = st.text_input("custom idea attractor (comma-separated or ranges like 0.2:0.9)", value="")
        seed = st.number_input("random seed (optional)", value=0, step=1)
        use_umap = st.checkbox("Compute UMAP projection (extra dependency)", value=True)

        run_button = st.button("Run simulation")

        st.markdown("---")
        st.markdown("Built from repository: show the code & choose presets from project files.")

    # Main area
    status_area = st.empty()

    if run_button:
        status_area.info("Starting simulation...")
        try:
            if seed:
                np.random.seed(int(seed))

            params = {
                "num_agents": int(num_agents),
                "num_dims": int(num_dims),
                "timesteps": int(timesteps),
                "idea_strength": float(idea_strength),
                "social_strength": float(social_strength),
                "noise_level": float(noise_level),
            }

            attractor = parse_attractor(attractor_text, int(num_dims))
            if attractor is not None:
                params["idea_attractor"] = attractor

            # load and run
            module_path = PRESETS[preset]
            with st.spinner("Running simulation — this may take a while..."):
                result = run_selected_simulation(module_path, params)

            status_area.success("Simulation finished ✅")

            # Show entropy
            if "entropy_history" in result:
                ent = np.array(result["entropy_history"])
                st.subheader("Entropy over time")
                st.line_chart(ent)

            # Projection
            st.subheader("Projection (PCA)")
            states = result.get("final_states")
            if states is not None:
                try:
                    pca = PCA(n_components=2)
                    pca_result = pca.fit_transform(states)
                    fig, ax = plt.subplots(figsize=(6, 5))
                    ax.scatter(pca_result[:, 0], pca_result[:, 1], s=8, alpha=0.6)
                    ax.set_title("PCA projection (2D)")
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"PCA failed: {e}")

                if use_umap:
                    try:
                        import umap

                        reducer = umap.UMAP(n_components=2, random_state=42)
                        umap_result = reducer.fit_transform(states)
                        fig2, ax2 = plt.subplots(figsize=(6, 5))
                        ax2.scatter(umap_result[:, 0], umap_result[:, 1], s=8, alpha=0.6)
                        ax2.set_title("UMAP projection (2D)")
                        st.pyplot(fig2)
                    except Exception as e:
                        st.warning("UMAP not available or failed to run (install umap-learn to enable)")

                # Summary
                st.subheader("Final state summary")
                st.write("Mean final state (first 10 dims):", np.round(np.mean(states, axis=0)[:10], 4).tolist())

                # Download
                buf = io.BytesIO()
                np.savez_compressed(buf, final_states=states, entropy_history=result.get("entropy_history", []))
                buf.seek(0)
                st.download_button("Download results (.npz)", data=buf, file_name="results.npz")

            else:
                st.warning("No final states in result to display")

        except Exception as e:
            tb = traceback.format_exc()
            status_area.error("Simulation failed — see error below")
            st.code(tb)

    else:
        st.info("Configure parameters in the sidebar and press 'Run simulation' to start.")


if __name__ == "__main__":
    main()
