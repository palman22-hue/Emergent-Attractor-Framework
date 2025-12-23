# Experiments  
**Empirical Validation of the Emergent Attractor Framework**

This document summarizes the experimental runs performed to validate the theoretical components of the framework. The experiments compare voluntary alignment (RUN#C1) and forced uniformity (RUN#C2) using entropy tracking, PCA visualization, and qualitative analysis.

---

## 1. Experimental Setup

### Agent Configuration
- Number of agents: 500  
- Emotional space: 21 dimensions  
- Initialization: uniform random distribution in [-1, 1]^d  

### Dynamics
- Social influence: weighted averaging  
- Attractor field: fixed vector a  
- Noise: small Gaussian perturbations  
- Clamping: all values restricted to [-1, 1]  

### Metrics
- Emotional entropy S(e)  
- System entropy \(\bar{S}(t)\)  
- PCA projections for visualization  
- Cluster spread and structure  

---

## 2. RUN#C1 — Voluntary Alignment

### Observations
- Agents converge toward the attractor while maintaining variation.
- PCA shows a **structured, coherent cluster**.
- Entropy decreases gradually and stabilizes at a moderate plateau.
- System remains **resilient** under small perturbations.

### Interpretation
RUN#C1 demonstrates the emergence of a **stable attractor basin** with non-zero spread, consistent with the Ethical Stability Theorem.

---

## 3. RUN#C2 — Forced Uniformity

### Observations
- Agents rapidly collapse toward a single compressed state.
- PCA shows a **tight, flattened cluster** near the origin.
- Entropy drops sharply and remains low.
- System becomes **fragile**: small perturbations disrupt stability.

### Interpretation
RUN#C2 illustrates the behavior of a **compressed point attractor**, lacking the basin structure required for resilience.

---

## 4. Comparative Analysis (RUN#C1 vs RUN#C2)

### Entropy
- C1: moderate, stable plateau  
- C2: low, compressed plateau  

### PCA Structure
- C1: emergent, coherent cluster  
- C2: collapsed, low-variance cluster  

### Stability
- C1: resilient  
- C2: fragile  

### Summary Table

| Property           | RUN#C1 (Voluntary) | RUN#C2 (Forced) |
|-------------------|---------------------|------------------|
| Final Entropy     | Moderate            | Low              |
| Cluster Spread    | Non-zero            | Near-zero        |
| Stability         | High                | Low              |
| Adaptivity        | Preserved           | Reduced          |

---

## 5. Connection to Theory

The experiments validate:

- **Lemma 2:** attractor fields reduce entropy  
- **Lemma 3:** variation supports resilience  
- **Lemma 4:** compression reduces adaptability  
- **Main Theorem:** voluntary alignment yields stable low-entropy states  

---

## 6. Conclusion

The experimental results align closely with the theoretical predictions.  
RUN#C1 and RUN#C2 provide clear empirical evidence for the structural differences between emergent attractor basins and compressed uniform states.

These experiments form the empirical backbone of the Emergent Attractor Framework.
