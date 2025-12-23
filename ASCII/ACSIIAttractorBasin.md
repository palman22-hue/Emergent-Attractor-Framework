# ASCII Diagram — Attractor Basins

This diagram visualizes, at a conceptual level, how agents move in state space under
two different alignment regimes: voluntary alignment and forced uniformity.

We represent a low-dimensional slice of the high-dimensional emotional space.

================================================================================
1. VOLUNTARY ALIGNMENT — EMERGENT ATTRACTOR BASIN
================================================================================

      State Space (conceptual 2D slice)
      Agents move toward a meaningful attractor,
      but variation and structure are preserved.

                         y
                         ^
                         |
              .          |         .         .
                  .      |   .          .
             .           |        .           .
                         |
        .      .         |        * A (Attractor)
                         |
            .        .   |  .           .
                         |
        ---------------------------------------------> x
                         |
              Local variations and micro-clusters
              remain around the attractor A.

Key properties:
- Agents form a **cluster around A**, not a single point.
- There is **non-zero spread**: small differences between agents remain.
- The system has an **attractor basin**: perturbations pull agents back toward A.
- Structure is **emergent and resilient**.

================================================================================
2. FORCED UNIFORMITY — COMPRESSED STATE
================================================================================

      State Space (conceptual 2D slice)
      Agents are strongly compressed toward a single target state u.

                         y
                         ^
                         |
                         |
                         |
                         |                * u (Uniform Target)
                         |              *** 
                         |             *****
                         |              ***
        ---------------------------------------------> x
                         |
                         |
                         |

Key properties:
- Agents are **almost exactly on top of each other** at u.
- **Spread ≈ 0**: variation is nearly eliminated.
- The system does **not** have a rich basin structure:
  small perturbations may move it away without internal diversity to correct.
- Stability is **apparent but fragile**.

================================================================================
3. COMPARATIVE VIEW — BASIN VS. POINT
================================================================================

     VOLUNTARY ALIGNMENT                    FORCED UNIFORMITY
     ---------------------                  -------------------
     Cluster around A                       Compression to u
     Resilient basin                        Thin point attractor
     Non-zero variance                      Near-zero variance
     Adaptive structure                     Reduced adaptability

        Voluntary Alignment:     A = attractor with a basin
        Forced Uniformity:       u = compression point without a rich basin

