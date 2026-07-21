# Architecture Records

This directory contains Architecture Records (ARs) describing important technical and architectural decisions made during development.

## Records

- AR-000 Project Principles
- AR-001 Character Export Files As Primary Datastore
- AR-002 Store User Data Inside Character Files
- AR-003 Replace File Watcher With Explicit Refresh Flow
- AR-004 Use Persistent UI Widgets Instead Of Rebuilding Views
- AR-005 Prefer Local UI Refreshes Over Global Reloads
- AR-006 Canonical Internal Identifiers And Separate UI Localization
- AR-007 Overview And Tracking Split
- AR-008 Introduce Multi-Language User Interface
- AR-009 Rebrand Application As Warband Manager
- AR-010 Dashboard Enrichment

## Reading Order

For new contributors, the recommended reading order is:

1. AR-000 Project Principles
2. AR-001 Character Export Files As Primary Datastore
3. AR-002 Store User Data Inside Character Files
4. AR-003 Replace File Watcher With Explicit Refresh Flow
5. AR-004 Use Persistent UI Widgets Instead Of Rebuilding Views
6. AR-005 Prefer Local UI Refreshes Over Global Reloads
7. AR-006 Canonical Internal Identifiers And Separate UI Localization
8. AR-007 Overview And Tracking Split
9. AR-008 Introduce Multi-Language User Interface
10. AR-009 Rebrand Application As Warband Manager
11. AR-010 Dashboard Enrichment

## Current Architectural Focus

The current architecture is based on the following principles:

- Character export files are the primary datastore.
- User-maintained data is stored inside character files.
- UI refreshes should be local and targeted.
- Widgets should remain persistent whenever possible.
- Internal identifiers must remain language-independent.
- User-facing text should be localized.
- Overview provides dashboard functionality.
- Tracking provides maintenance and data-entry functionality.
- Dashboard content should be driven by data where practical.
- The application evolves toward a warband management platform rather than a simple tracking utility.