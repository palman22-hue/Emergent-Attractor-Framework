import importlib.util
import sys
import numpy as np

PRESETS = {
    "Exp1": "Exp1.py",
    "Exp2": "Exp2.py",
    "RUN#C1": "RUN#C1.py",
    "RUN#C2": "RUN#C2.py",
}


def load_module(path):
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


if __name__ == "__main__":
    ok = True
    for name, path in PRESETS.items():
        try:
            m = load_module(path)
            if not hasattr(m, "run_simulation"):
                print(f"{name}: missing run_simulation")
                ok = False
                continue
            res = m.run_simulation(timesteps=5, num_agents=50, num_dims=5)
            if not isinstance(res, dict) or "final_states" not in res:
                print(f"{name}: unexpected return structure: {type(res)} keys={getattr(res, 'keys', lambda:[])()}"
)
                ok = False
            else:
                print(f"{name}: OK — final_states shape {res['final_states'].shape}")
        except Exception as e:
            print(f"{name}: FAILED — {e}")
            ok = False
    sys.exit(0 if ok else 2)
