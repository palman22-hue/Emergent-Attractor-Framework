import numpy as np

# Re-implement minimal dynamics from RUN#C1.py so we can call them safely
NUM_AGENTS = 500
NUM_DIMS = 21
TIMESTEPS = 1000

IDEA_STRENGTH = 0.02
SOCIAL_STRENGTH = 0.03
NOISE_LEVEL = 0.01


def emotion_to_prob(e):
    return (e + 1.0) / 2.0


def shannon_entropy(e, eps=1e-12):
    p = emotion_to_prob(e)
    p = np.clip(p, eps, 1.0 - eps)
    H = - (p * np.log(p) + (1 - p) * np.log(1 - p))
    return np.mean(H, axis=-1)


class IdeaField:
    def __init__(self, attractor, strength=IDEA_STRENGTH):
        self.attractor = np.array(attractor, dtype=float)
        self.strength = strength

    def influence(self, states):
        return self.strength * (self.attractor - states)


def init_agents(num_agents=NUM_AGENTS, num_dims=NUM_DIMS):
    return np.random.uniform(-1, 1, size=(num_agents, num_dims))


def social_influence(states, strength=SOCIAL_STRENGTH):
    mean_state = np.mean(states, axis=0, keepdims=True)
    return strength * (mean_state - states)


def noise_term(states, noise_level=NOISE_LEVEL):
    return noise_level * np.random.normal(0.0, 1.0, size=states.shape)


def clamp_states(states):
    return np.clip(states, -1.0, 1.0)


def run_simulation_record(
    num_agents=NUM_AGENTS,
    num_dims=NUM_DIMS,
    timesteps=TIMESTEPS,
    idea_attractor=None,
    seed=None,
):
    """Run the attractor simulation and record states at every timestep.

    Returns:
        dict with keys:
            - states_history: np.array shaped (timesteps, num_agents, num_dims)
            - entropy_history: np.array shaped (timesteps,)
            - idea_attractor: array
    """
    if seed is not None:
        np.random.seed(seed)

    states = init_agents(num_agents, num_dims)

    if idea_attractor is None:
        idea_attractor = np.linspace(0.2, 0.9, num_dims)

    idea_field = IdeaField(idea_attractor)

    states_history = np.zeros((timesteps, num_agents, num_dims), dtype=float)
    entropy_history = []

    for t in range(timesteps):
        delta_idea = idea_field.influence(states)
        delta_social = social_influence(states)
        delta_noise = noise_term(states)

        states = states + delta_idea + delta_social + delta_noise
        states = clamp_states(states)

        states_history[t] = states.copy()

        H = shannon_entropy(states)
        entropy_history.append(np.mean(H))

    return {
        "states_history": states_history,
        "entropy_history": np.array(entropy_history),
        "idea_attractor": idea_attractor,
    }
