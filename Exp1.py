import numpy as np

# ============================
# Configuratie
# ============================

NUM_AGENTS = 500
NUM_DIMS = 21      # D12–D32
TIMESTEPS = 1000

# Krachten (tweakbaar)
IDEA_STRENGTH = 0.02      # hoe sterk het idee agents aantrekt
SOCIAL_STRENGTH = 0.03    # hoe sterk agents naar groepsgemiddelde bewegen
NOISE_LEVEL = 0.01        # hoeveel random variatie

# ============================
# Entropie helpers (Shannon-achtig)
# ============================

def emotion_to_prob(e):
    """
    Map [-1,1] -> [0,1] per component.
    e: (..., NUM_DIMS)
    """
    return (e + 1.0) / 2.0

def shannon_entropy(e, eps=1e-12):
    """
    e: array shape (..., NUM_DIMS), values in [-1,1]
    Retourneert entropie per agent (scalar per agent).
    """
    p = emotion_to_prob(e)
    p = np.clip(p, eps, 1.0 - eps)
    H = - (p * np.log(p) + (1 - p) * np.log(1 - p))
    return np.mean(H, axis=-1)  # gemiddelde over dimensies

# ============================
# Idee-veld
# ============================

class IdeaField:
    def __init__(self, attractor, strength=IDEA_STRENGTH):
        """
        attractor: (NUM_DIMS,) vector in [-1,1]
        strength: float, hoe sterk de kracht van het idee is
        """
        self.attractor = np.array(attractor, dtype=float)
        self.strength = strength

    def influence(self, states):
        """
        states: (N, NUM_DIMS)
        Retourneert delta to state door het idee-veld.
        """
        return self.strength * (self.attractor - states)

# ============================
# Simulatie
# ============================

def init_agents(num_agents=NUM_AGENTS, num_dims=NUM_DIMS, mode="random"):
    if mode == "random":
        # willekeurig in [-1,1]
        return np.random.uniform(-1, 1, size=(num_agents, num_dims))
    elif mode == "neutral":
        # alles rond 0 met kleine ruis
        return np.random.normal(0.0, 0.1, size=(num_agents, num_dims))
    else:
        raise ValueError("Unknown init mode.")

def social_influence(states, strength=SOCIAL_STRENGTH):
    """
    Agents bewegen naar het groepsgemiddelde.
    """
    mean_state = np.mean(states, axis=0, keepdims=True)  # (1, NUM_DIMS)
    return strength * (mean_state - states)

def noise_term(states, noise_level=NOISE_LEVEL):
    """
    Random ruis.
    """
    return noise_level * np.random.normal(0.0, 1.0, size=states.shape)

def clamp_states(states):
    return np.clip(states, -1.0, 1.0)

# ============================
# Hoofdloop
# ============================

def run_simulation(
    num_agents=NUM_AGENTS,
    num_dims=NUM_DIMS,
    timesteps=TIMESTEPS,
    idea_attractor=None,
    idea_strength=IDEA_STRENGTH,
    social_strength=SOCIAL_STRENGTH,
    noise_level=NOISE_LEVEL,
    init_mode="random",
):
    # Init agents
    states = init_agents(num_agents, num_dims, init_mode)
    
    # Als geen attractor meegegeven, maak een "compassionate" idee
    if idea_attractor is None:
        # voorbeeld: hoge waarden voor Love, Compassion, Connection, Meaning, Harmony, Serenity
        # hier gewoon generiek een "positieve" vector
        idea_attractor = np.linspace(0.2, 0.9, num_dims)
        idea_attractor = np.clip(idea_attractor, -1, 1)
    
    idea_field = IdeaField(idea_attractor, strength=idea_strength)
    
    # Metrics opslag
    mean_states_history = []
    entropy_history = []
    
    for t in range(timesteps):
        # Idee invloed
        delta_idea = idea_field.influence(states)                  # (N, D)
        
        # Sociale invloed
        delta_social = social_influence(states, social_strength)   # (N, D)
        
        # Ruis
        delta_noise = noise_term(states, noise_level)              # (N, D)
        
        # Update
        states = states + delta_idea + delta_social + delta_noise
        states = clamp_states(states)
        
        # Metrics
        mean_state = np.mean(states, axis=0)
        H = shannon_entropy(states)  # entropie per agent
        mean_H = np.mean(H)
        
        mean_states_history.append(mean_state)
        entropy_history.append(mean_H)
        
        if t % 100 == 0:
            print(f"t={t:4d}  mean_entropy={mean_H:.4f}")
    
    return {
        "final_states": states,
        "mean_states_history": np.array(mean_states_history),
        "entropy_history": np.array(entropy_history),
        "idea_attractor": idea_attractor,
    }

if __name__ == "__main__":
    result = run_simulation()
    print("Simulation finished.")
    print("Final mean entropy:", result["entropy_history"][-1])
