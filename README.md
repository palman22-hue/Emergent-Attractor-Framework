# EMERGENT ATTRACTOR FRAMEWORK  
**A Formal Model of Alignment, Entropy, and Stability in Multi-Agent Systems**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: CC0](https://img.shields.io/badge/License-CC0-green.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Research Framework](https://img.shields.io/badge/Type-Research%20Framework-orange.svg)](#)
[![DOI](https://zenodo.org/badge/1121764509.svg)](https://doi.org/10.5281/zenodo.18035787)

## 🧠 Overview

This repository contains a complete research framework for studying ethical stability in multi-agent systems using entropy dynamics and attractor-based alignment.  
It integrates formal theory, simulation, documentation, and visualization — structured as a reproducible research lab.

---

## 📂 Repository Structure

### 🔬 Theory & Documentation

Documents(EN)/           → Formal English write-ups (definitions, lemmas, theorem, paper sections)
Documents(NL)/           → Dutch documentation and early conceptual notes
FullPaper/               → Integrated academic documents and supporting materials
ASCII/                   → Conceptual ASCII diagrams (architecture, attractors, entropy)


### 🧪 Experiments & Simulation

Experiments/             → Raw experiment notes and logs
RUNC1/                   → Voluntary alignment run (visuals, CLI, interpretation)
RUNC2/                   → Forced uniformity run (visuals, CLI, interpretation)
RUN#C1VSRUN#C2.md        → Comparative analysis of both runs
Exp1.py  / Exp2.py         → Core simulation scripts


---

## 📘 Key Documents

### 📄 Theory

- `Definitions.md`  
- `Lemmata.md`  
- `MainTheorem.md`  
- `MathematicalAppendix.md`  
- `Glossary.md`

### 📄 Paper Sections

- `1.Abstract.md`  
- `2.Introduction.md`  
- `3.Discussion.md`  
- `4.Conclusion.md`  
- `5.FutureWork.md`  
- `FullPaper.md`

### 📄 Visual & Conceptual

- `OverviewDiagram.md`  
- `AttractorBasins.md`  
- `EntropyEvolution.md`  
- `Experiments.md`  
- `Architecture.md`

---

## 📊 Simulation Runs

### RUN#C1 — Voluntary Alignment  
- Emergent attractor basin  
- Structured cluster  
- Stable entropy plateau  
- Resilient behavior

### RUN#C2 — Forced Uniformity  
- Compressed state  
- Flattened cluster  
- Sharp entropy drop  
- Fragile behavior

### Comparison  
- `RUN#C1VSRUN#C2.md` shows side-by-side analysis of entropy, PCA, and stability.

---

## 🎯 Purpose

This framework offers a **neutral, formal, and reproducible** method for analyzing:

- Entropy flow  
- Attractor dynamics  
- Stability and resilience  
- Alignment mechanisms  
- Emergent structure in multi-agent systems

It does not prescribe ethical norms, but provides tools to study how different forms of alignment influence system behavior.

---

## 🧭 Suggested Reading Order

1. `1.Abstract.md`  
2. `2.Introduction.md`  
3. `Definitions.md`, `Lemmata.md`, `MainTheorem.md`  
4. `Experiments.md`, `RUN#C1.md`, `RUN#C2.md`, `RUN#C1VSRUN#C2.md`  
5. `EntropyEvolution.md`, `AttractorBasins.md`  
6. `3.Discussion.md`, `4.Conclusion.md`, `5.FutureWork.md`  
7. `FullPaper.md`, `Architecture.md`, `Glossary.md`

---

## 🧠 Author

This framework is designed and documented by **Esteban Palman**, as part of an evolving research lab on emergent ethics, attractor theory, and multi-agent dynamics.

---

## 📌 License & Citation

This project is open-source and intended for academic use, simulation, and theoretical exploration.  

- **Code** is licensed under **GPLv3** → ensuring freedom to use, modify, and distribute, while preventing proprietary "black box" use without source disclosure.  
- **Documentation & diagrams** are licensed under **CC‑BY 4.0**, with an optional **CC0 waiver** → allowing maximal freedom, but encouraging attribution to maintain transparency.  

Please cite appropriately if used in publications or derivative work:

> Esteban, *Emergent Attractor Framework: Alignment, Entropy, and Stability in Multi-Agent Systems*, 2025.  
> Licensed under GPLv3 (code) and CC‑BY 4.0 / CC0 (documentation).


## 🔧 How to Reuse

You are welcome to use this framework in your own research, teaching, or projects.  
Here’s how to do it transparently:

- **Fork or clone the code** → All `.py` scripts are licensed under GPLv3.  
  - You may modify and redistribute them, but derivative works must also remain open-source under GPLv3.  
  - Always include the original license header when reusing code.

- **Reuse the documentation** → All `.md` files and ASCII diagrams are licensed under CC‑BY 4.0.  
  - You may quote, adapt, and share them freely, provided you credit *Esteban*.  
  - If you prefer maximal freedom, you may also treat them as CC0 (Public Domain), but attribution is strongly encouraged.

- **Cite the work** → When publishing or presenting, please cite:  
  > Esteban Palman , *Emergent Attractor Framework: Alignment, Entropy, and Stability in Multi-Agent Systems*, 2025.  
  > Licensed under GPLv3 (code) and CC‑BY 4.0 / CC0 (documentation).

- **Stay transparent** → If you build on this framework, keep your modifications open and visible.  
  This ensures the work does not disappear into proprietary black boxes and remains part of the collective knowledge base.

## 🚀 Quick Start

Follow these steps to run the framework locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/EMERGENT-ATTRACTOR-FRAMEWORK.git
   cd EMERGENT-ATTRACTOR-FRAMEWORK

2. Run the first experiment (Voluntary Alignment)

    python Exp1.py

     -Output: entropy evolution logs

     -Visuals: see RUNC1/RUN_C1.png and RUNC1/RUN_C1_CLI.png

     -Documentation: RUNC1/RUN#C1.md

3. Run the second experiment (Forced Uniformity)

    python Exp2.py

     -Output: entropy evolution logs

     -Visuals: see RUNC2/RUN_C2.png and RUNC2/RUN_C2_CLI.png

     -Documentation: RUNC2/RUN#C2.md

4. Compare both runs

     -Open RUN#C1VSRUN#C2.md for side‑by‑side analysis.

     -Check entropy curves and PCA plots for differences in resilience vs. fragility.

5. Explore the theory

     -Start with Documents(EN)/1.Abstract.md and 2.Introduction.md.

     -Dive into Definitions.md, Lemmata.md, and MainTheorem.md.

     -For a full overview, read FullPaper/FullPaper.md.

## 🤝 Contributing

Collaboration is welcome! This framework is designed as an open research lab, and contributions from the community help it grow stronger.

### How to Contribute

1. **Fork the repository**  
   - Create your own copy to experiment with.

2. **Create a feature branch**  
   ```bash
   git checkout -b feature/YourFeatureName

3. Make your changes

     -For code: follow the GPLv3 license and keep modifications open.

     -For documentation: follow CC‑BY 4.0 (or CC0 waiver) and cite appropriately.

4. Commit and push

    git commit -m "Add: description of your change"
    git push origin feature/YourFeatureName

5. Open a Pull Request (PR)

     -Describe your changes clearly.

     -Link to related experiments, diagrams, or theory sections if relevant.

     -Explain how your contribution improves reproducibility, clarity, or functionality.

6. Contribution Guidelines
    
     -Code style: Keep Python scripts clean, documented, and reproducible.

     -Documentation: Use clear Markdown, include references, and maintain transparency.

     -Experiments: When adding new runs, include both .py scripts and .md documentation with visuals.

     -Respect licensing: Ensure all contributions remain open and cite sources properly.

     -Discussion: Use issues to propose new ideas, raise questions, or suggest improvements.