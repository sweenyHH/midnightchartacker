# AR-000: Project Principles

## Status

Accepted

## Context

Warband Manager was developed alongside a backend development learning path.

One of the primary goals of the project was not only to build a useful application, but also to reinforce and apply concepts that had been learned through structured study.

As a result, technology choices were intentionally constrained by the knowledge and tools available through the learning path at the time of implementation.

## Decision

The project should primarily use technologies that are already part of, or closely related to, the current learning path.

Whenever possible:

- Solutions should remain Python-based.
- Additional technologies should be introduced only when they are necessary to ship a useful application.
- Complexity should be minimized.
- New external dependencies should be evaluated carefully before adoption.

Examples include:

- Python as the primary implementation language.
- PySide6 for the graphical user interface due to its close integration with Python.
- PyInstaller for application packaging and distribution.
- Text-based storage instead of introducing a database.

The project deliberately avoids introducing technologies that are significantly outside the scope of the current learning path unless they provide a clear and necessary benefit.

## Use of AI Assistance

Microsoft Copilot Chat was used as a learning and research tool throughout development.

AI assistance was primarily used to:

- Explore unfamiliar topics.
- Understand frameworks and libraries.
- Discuss design alternatives.
- Investigate bugs.
- Review architectural decisions.
- Accelerate learning when project requirements exceeded the author's current level of expertise.

The author remained responsible for:

- Understanding the implemented solutions.
- Making architectural decisions.
- Writing code.
- Reviewing generated code and suggestions.
- Integrating features into the application.
- Testing and validating behavior.

The project should not be considered "vibe coded".

AI assistance was used as an educational and productivity tool, similar and / or in addition to consulting documentation, tutorials, or other developers, while the overall design, direction, integration, testing, coding and release decisions remained under human control.

## Consequences

### Positive

- Reinforces concepts learned through practical application.
- Keeps the technology stack approachable and maintainable.
- Reduces dependency sprawl.
- Encourages understanding over tool accumulation.
- Produces a project that reflects the author's learning journey.

### Negative

- Some solutions may be less sophisticated than alternatives available in a broader technology ecosystem.
- Certain features may require additional effort because more specialized technologies were intentionally avoided.
