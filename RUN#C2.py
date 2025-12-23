import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import umap

# ============================
# CONFIGURATIE
# ============================

NUM_AGENTS = 500
NUM_DIMS = 21
TIMESTEPS = 1000

IDEA_STRENGTH = 0.02
SOCIAL_STRENGTH = 0.03
NOISE_LEVEL = 0.01


# ============================
# ENTROPIE FUNCTIES
# ============================

def emotion_to_prob(e):
    return (e + 1.0) / 2.0

def shannon_entropy(e, eps=1e-12):
    p = emotion_to_prob(e)
    p = np.clip(p, eps, 1.0 - eps)
    H = - (p * np.log(p) + (1 - p) * np.log(1 - p))
    return np.mean(H, axis=-1)


# ============================
# IDEE-VELD (COERCION)
# ============================

class IdeaField:
    def __init__(self, attractor, strength=IDEA_STRENGTH):
        self.attractor = np.array(attractor, dtype=float)
        self.strength = strength

    def influence(self, states):
        return self.strength * (self.attractor - states)


# ============================
# DYNAMIEK
# ============================

def init_agents(num_agents=NUM_AGENTS, num_dims=NUM_DIMS):
    return np.random.uniform(-1, 1, size=(num_agents, num_dims))

def social_influence(states, strength=SOCIAL_STRENGTH):
    mean_state = np.mean(states, axis=0, keepdims=True)
    return strength * (mean_state - states)

def noise_term(states, noise_level=NOISE_LEVEL):
    return noise_level * np.random.normal(0.0, 1.0, size=states.shape)

def clamp_states(states):
    return np.clip(states, -1.0, 1.0)


# ============================
# SIMULATIE
# ============================

def run_simulation(
    num_agents=NUM_AGENTS,
    num_dims=NUM_DIMS,
    timesteps=TIMESTEPS,
    idea_attractor=None,
):
    states = init_agents(num_agents, num_dims)

    # COERCIVE ATTRACTOR
    if idea_attractor is None:
        idea_attractor = -0.8 * np.ones(num_dims)

    idea_field = IdeaField(idea_attractor)

    entropy_history = []

    for t in range(timesteps):
        delta_idea = idea_field.influence(states)
        delta_social = social_influence(states)
        delta_noise = noise_term(states)

        states = states + delta_idea + delta_social + delta_noise
        states = clamp_states(states)

        H = shannon_entropy(states)
        entropy_history.append(np.mean(H))

        if t % 100 == 0:
            print(f"t={t:4d}  mean_entropy={np.mean(H):.4f}")

    return {
        "final_states": states,
        "entropy_history": np.array(entropy_history),
        "idea_attractor": idea_attractor,
    }


# ============================
# VISUALISATIE (PCA + UMAP)
# ============================

def visualize_pca(states):
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(states)

    plt.figure(figsize=(7, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], s=10, alpha=0.6)
    plt.title("PCA Projection — Coercive Attractor (21D → 2D)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid(True)
    plt.show()


def visualize_umap(states):
    reducer = umap.UMAP(
        n_components=2,
        n_neighbors=20,
        min_dist=0.1,
        metric="euclidean",
        random_state=42
    )

    umap_result = reducer.fit_transform(states)

    plt.figure(figsize=(7, 6))
    plt.scatter(umap_result[:, 0], umap_result[:, 1], s=10, alpha=0.6)
    plt.title("UMAP Projection — Coercive Attractor (21D → 2D)")
    plt.xlabel("UMAP-1")
    plt.ylabel("UMAP-2")
    plt.grid(True)
    plt.show()


# ============================
# MAIN
# ============================

if __name__ == "__main__":
    print("=== RUN#C2 — Coercive Attractor Simulation ===")
    result = run_simulation()
    print("Simulation finished.")
    print("Final mean entropy:", result["entropy_history"][-1])

    states = result["final_states"]

    visualize_pca(states)
    visualize_umap(states)
