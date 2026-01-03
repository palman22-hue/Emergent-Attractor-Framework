import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sklearn.decomposition import PCA
import time

from sim_wrapper import run_simulation_record

st.set_page_config(page_title="Emergent Attractor — Live 3D", layout="wide")

st.title("Emergent Attractor — Live 3D Visualization")
st.write("Interactive prototype: run live simulations and inspect agents in 3D (PCA projection).")

# Sidebar controls
st.sidebar.header("Simulation Parameters")
scenario = st.sidebar.selectbox("Scenario", ["RUN#C1 — Compassion", "RUN#C2 — Coercion"])
num_agents = st.sidebar.slider("Agents", min_value=50, max_value=1000, value=200, step=50)
num_dims = st.sidebar.slider("Dimensions (state space)", min_value=3, max_value=21, value=21)
timesteps = st.sidebar.slider("Timesteps", min_value=10, max_value=500, value=200, step=10)
seed = st.sidebar.number_input("Random seed (0 = random)", value=0, min_value=0, step=1)

st.sidebar.markdown("---")
if scenario.startswith("RUN#C1"):
    st.sidebar.markdown("**Attractor:** Compassion (linear gradient by default)")
else:
    st.sidebar.markdown("**Attractor:** Coercion (uniform negative attractor by default)")

run_button = st.sidebar.button("Run simulation")

# Cached runner
@st.cache_data
def cached_run(num_agents, num_dims, timesteps, scenario, seed):
    seed_val = None if seed == 0 else int(seed)
    # choose idea_attractor based on scenario
    if scenario.startswith("RUN#C1"):
        idea_attractor = np.linspace(0.2, 0.9, num_dims)
    else:
        idea_attractor = -0.8 * np.ones(num_dims)

    return run_simulation_record(
        num_agents=num_agents,
        num_dims=num_dims,
        timesteps=timesteps,
        idea_attractor=idea_attractor,
        seed=seed_val,
    )

# Run the simulation on button press
if run_button:
    with st.spinner("Running simulation... this may take a few seconds"):
        result = cached_run(num_agents, num_dims, timesteps, scenario, seed)

    states_history = result["states_history"]
    entropy_history = result["entropy_history"]

    # PCA to 3D
    pca = PCA(n_components=min(3, num_dims))
    flat = states_history.reshape(-1, num_dims)
    proj_flat = pca.fit_transform(flat)
    proj = proj_flat.reshape(timesteps, num_agents, -1)

    st.sidebar.success("Simulation complete ✅")

    # Main layout: left = 3D viewer, right = controls + entropy
    col1, col2 = st.columns([3, 1])

    with col2:
        st.subheader("Controls")
        timestep = st.slider("Timestep", 0, timesteps - 1, 0)
        color_by = st.selectbox("Color by", ["Agent index", "Distance to attractor"])
        animate = st.button("Animate")

        st.markdown("---")
        st.subheader("Entropy")
        st.line_chart(entropy_history)

    with col1:
        placeholder = st.empty()

        def make_fig(tt):
            coords = proj[tt]
            if coords.shape[1] == 2:
                x = coords[:, 0]
                y = coords[:, 1]
                z = np.zeros_like(x)
            else:
                x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

            if color_by == "Agent index":
                colors = np.arange(len(x))
                colorscale = "Viridis"
            else:
                # distance to attractor: compute norm of agent state relative to idea_attractor
                idea = result["idea_attractor"]
                raw_states = states_history[tt]
                d = np.linalg.norm(raw_states - idea, axis=1)
                colors = d
                colorscale = "Plasma"

            fig = go.Figure(
                data=[
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode="markers",
                        marker=dict(size=3, color=colors, colorscale=colorscale, showscale=True),
                    )
                ]
            )
            fig.update_layout(margin=dict(l=0, r=0, t=30, b=0), height=700)
            fig.update_traces(marker=dict(opacity=0.8))
            fig.update_layout(scene=dict(xaxis_title='PC1', yaxis_title='PC2', zaxis_title='PC3'))
            fig.update_layout(title=f"Agents — timestep {tt}")
            return fig

        # initial render
        fig = make_fig(timestep)
        placeholder.plotly_chart(fig, use_container_width=True)

        # react to slider changes
        # Note: Streamlit reruns; so we just re-render using selected 'timestep'

        if animate:
            for tt in range(timesteps):
                fig = make_fig(tt)
                placeholder.plotly_chart(fig, use_container_width=True)
                time.sleep(0.05)

    st.success("Done — adjust parameters and Run again to re-simulate.")

else:
    st.info("Configure parameters on the left and click **Run simulation** to start.")

# Footer
st.markdown("---")
st.write("Prototype: live simulation + PCA 3D. For better performance use fewer agents or fewer timesteps.")
