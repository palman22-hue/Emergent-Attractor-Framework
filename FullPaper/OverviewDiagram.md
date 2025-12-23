# Overview Diagram  
**Emergent Attractor Framework — Conceptual Architecture**

This diagram provides a high-level overview of the components, flows, and relationships within the Emergent Attractor Framework. It summarizes how definitions, dynamics, simulations, and theoretical results interact to form a coherent research structure.

---

## 1. System Architecture (Top-Level)

+-----------------------------------------------------------+
|                 Emergent Attractor Framework              |
+-----------------------------------------------------------+
|  Definitions  |  Dynamics  |  Theory  |  Experiments      |
+-----------------------------------------------------------+


---

## 2. Agent Model

+---------------------------+
|     Agent (i)            |
+---------------------------+
| Emotional state e_i ∈ R^d|
| Entropy S(e_i)           |
+---------------------------+


Agents exist in a high-dimensional emotional space and evolve over time.

---

## 3. Core Components

+----------------------+      +----------------------+
|   Social Influence   | ---> |   Agent State Update |
+----------------------+      +----------------------+
^                         |
|                         v
+----------------------+      +----------------------+
|    Attractor Field   | ---> |   Entropy Dynamics   |
+----------------------+      +----------------------+


- **Social Influence:** agents move toward the mean state  
- **Attractor Field:** agents move toward a target vector  
- **Noise:** introduces controlled variation  
- **Entropy Dynamics:** tracks uncertainty and coherence  

---

## 4. Two Alignment Modes

+---------------------------+     +---------------------------+
|     Voluntary Alignment   |     |     Forced Uniformity     |
+---------------------------+     +---------------------------+
| - Social influence        |     | - Strong compression      |
| - Attractor guidance      |     | - Minimal variation       |
| - Preserved variation     |     | - Single fixed point      |
+---------------------------+     +---------------------------+


These two modes define the central comparison in the framework.

---

## 5. System Evolution Loop

+-----------------------------+
|   Initialize Agents         |
+-------------+---------------+
|
v
+-----------------------------+
|   Apply Social Influence    |
+-------------+---------------+
|
v
+-----------------------------+
|   Apply Attractor Field     |
+-------------+---------------+
|
v
+-----------------------------+
|   Add Noise                 |
+-------------+---------------+
|
v
+-----------------------------+
|   Clamp to [-1,1]^d         |
+-------------+---------------+
|
v
+-----------------------------+
|   Compute Entropy           |
+-------------+---------------+
|
v
+-----------------------------+
|   Repeat for T timesteps    |
+-----------------------------+


---

## 6. Theoretical Layer

+---------------------------+
|       Definitions         |
+---------------------------+
|
v
+---------------------------+
|          Lemmas           |
+---------------------------+
|
v
+---------------------------+
|      Main Theorem         |
+---------------------------+


The theory formalizes the behavior observed in simulations.

---

## 7. Experimental Layer

+---------------------------+
|        RUN#C1             |
|  Compassion Attractor     |
|  - Structured cluster     |
|  - Stable entropy         |
+---------------------------+

+---------------------------+
|        RUN#C2             |
|  Coercive Attractor       |
|  - Compressed cluster     |
|  - Fragile stability      |
+---------------------------+

+---------------------------+
|   RUN#C1 vs RUN#C2        |
|  Comparative analysis     |
+---------------------------+


---

## 8. Document Structure

Documents(EN)/
Definitions.md
Lemmata.md
MainTheorem.md
1.Abstract.MD
2.Introduction.md
3.Discussion.md
4.Conclusion.md
5.Futurework.md
FullPaper.md

Experiments/
RUN_C1/
RUN_C2/
Comparison/


---

## 9. Conceptual Summary

Voluntary Alignment  →  Coherence + Resilience
Forced Uniformity    →  Compression + Fragility


This relationship is the core insight of the framework.

---

## 10. Purpose of the Framework

To provide a **neutral, formal, reproducible** method for studying:

- entropy flow  
- attractor dynamics  
- stability  
- emergent order  
- alignment mechanisms  

in high-dimensional multi-agent systems.

