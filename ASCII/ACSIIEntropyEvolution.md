# ASCII Diagram — Entropy Evolution (RUN#C1 vs RUN#C2)

This diagram provides a conceptual view of how system entropy evolves over time
for two different dynamics: voluntary alignment (RUN#C1) and forced uniformity (RUN#C2).

It does not represent exact numerical values, but the qualitative behavior observed
in the simulations.

================================================================================
1. ENTROPY AXIS AND TIME AXIS
================================================================================

           Entropy S(t)
                 ^
                 |                         .
                 |                      .
                 |                   .
                 |                .
                 |             .
                 |          .
                 |       .
                 |    .
                 | .
                 +---------------------------------------------> t
                             Time

Entropy S(t) is the average emotional entropy of agents in the system.

================================================================================
2. VOLUNTARY ALIGNMENT — RUN#C1
================================================================================

Qualitative behavior:
- Start from random states → moderate entropy.
- Entropy initially fluctuates, then gradually decreases.
- Converges to a **stable, non-minimal** entropy plateau.
- Indicates a structured, coherent but still diverse cluster.

Conceptual curve:

           Entropy S(t)
                 ^
      high  -    |\            RUN#C1 (Voluntary Alignment)
                 | \.
                 |  \..
                 |    \...
                 |      \.....
   moderate  -   |        \---------
                 |
                 +---------------------------------------------> t
                             Time

Key properties:
- **Not** minimizing entropy at all cost.
- Stabilizes at a value where structure and variation coexist.
- Reflects a **resilient attractor basin**.

================================================================================
3. FORCED UNIFORMITY — RUN#C2
================================================================================

Qualitative behavior:
- Start from random states → similar initial entropy as RUN#C1.
- Entropy rapidly decreases and approaches a low value.
- Converges to a **compressed, low-entropy state**.
- Indicates loss of variation and potential fragility.

Conceptual curve:

           Entropy S(t)
                 ^
      high  -    |\
                 | \
                 |  \      RUN#C2 (Forced Uniformity)
                 |   \...
                 |      \....
   low     -     |         \__________
                 |
                 +---------------------------------------------> t
                             Time

Key properties:
- Strong entropy reduction through compression.
- Final entropy is **lower** than in RUN#C1.
- Reflects a **compressed, fragile configuration**.

================================================================================
4. SIDE-BY-SIDE COMPARISON
================================================================================

           Entropy S(t)
                 ^
      high  -    |\
                 | \
                 |  \        RUN#C2
                 |   \...    (Forced Uniformity)
                 |      \....
   moderate  -   |        \---------
                 |          RUN#C1
                 |          (Voluntary Alignment)
   low     -     |------------------------------
                 +---------------------------------------------> t

Interpretation:
- Both dynamics reduce entropy relative to random initialization.
- RUN#C2 achieves **lower entropy**, but via compression.
- RUN#C1 maintains **higher (but stable) entropy**, reflecting preserved diversity.
- The difference is not just quantitative (how low), but qualitative (how and with what cost).

================================================================================
5. LINK TO THE ETHICAL STABILITY THEOREM
================================================================================

- RUN#C1: Entropy reduction + stable plateau → coherent, adaptive attractor basin.
- RUN#C2: Strong entropy reduction → compressed state with reduced adaptability.

This aligns with the theorem:
- Voluntary alignment → low-entropy + resilience.
- Forced uniformity → low-entropy + fragility.

