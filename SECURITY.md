# Security Policy

## Supported versions

Emergent-Attractor-Framework is currently an experimental research project and only the `main` branch is actively maintained.  
Other branches or forks are not covered by security support.

## Deployment model

Emergent-Attractor-Framework is designed for local research and experimentation (e.g. simulations, CLI tools, notebooks).  
This repository does **not** provide a public, maintainer-operated API or hosted service; any external exposure (for example, via a custom-built web service or multi-agent deployment) is the responsibility of the deploying party.

## Data & privacy

- The framework typically operates on synthetic, experimental, or user-provided datasets for studying alignment, entropy, and stability.  
- Any datasets, logs, and experiment results are stored locally on the user’s system.  
- The maintainer does not receive automatic telemetry or user data.

Users are responsible for:
- Ensuring that any real-world data they use in experiments is handled in accordance with applicable privacy and data protection laws.  
- Securing their own host system, operating system, and runtime (Python environment, containers, etc.).

## Reporting a vulnerability

If you discover a potential vulnerability or a serious misuse risk in Emergent-Attractor-Framework, please use **responsible disclosure**.

If Private Vulnerability Reporting is enabled for this repository:
1. Use the **“Report a vulnerability”** button on the repository’s GitHub page to submit a private report.

If Private Vulnerability Reporting is not available:
1. Open a minimal public issue that:
   - Only states that you have found a potential vulnerability.
   - Does **not** include technical details or exploit code.
2. Wait for the maintainer to respond with an appropriate private channel for sharing details.

Where possible, include:
- A description of the vulnerability or misuse scenario (e.g. unsafe defaults, misconfigured simulations, unintended exposure when integrated into agents).  
- Reproduction steps or a proof-of-concept (shared only through a private channel).  
- Relevant environment details (OS, Python version, libraries, container configuration).

The goal is to provide an initial response within 14 days, including an indication of next steps.

## Scope

In scope:
- The code in this repository (`main` branch), including:
  - Core simulation and analysis code for attractors, entropy, and stability.  
  - CLI utilities, scripts, and configuration files referenced in the README.  
  - Example experiments and notebooks included with the project.

Out of scope:
- External libraries, runtimes, and tools used together with the framework (e.g. plotting libraries, ML libraries, container runtimes).  
- Third-party multi-agent systems, decision systems, or production deployments that integrate this framework.  
- Hardware- and OS-specific issues that do not directly originate from the code in this repository.

## Responsible use

Emergent-Attractor-Framework is intended as an open research framework for studying alignment, entropy, and stability in complex and multi-agent systems.  
Users are strongly discouraged from using the framework for:

- Designing harmful, deceptive, or coercive multi-agent or decision-making systems.  
- Building opaque high-impact systems (e.g. in governance, finance, critical infrastructure) without appropriate domain-specific safety, oversight, and audit mechanisms.

If you observe misuse of Emergent-Attractor-Framework in the wild, you may report it using the same contact path as above.
