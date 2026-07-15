# AR-005: Prefer Local UI Refreshes Over Global Reloads

## Status

Accepted

## Context

Many user actions originally resulted in broad application refreshes.

Examples included updates to:

- Vault Progress
- Notes
- Weekly Duties

This increased UI activity and reduced responsiveness.

## Decision

When possible, UI updates should be limited to affected components.

Examples:

- Vault Progress refreshes the Vault Tab
- Returning to the Character List refreshes the table
- Global reloads are reserved for character-level data changes

## Consequences

### Positive

- Faster UI updates
- Reduced complexity
- Improved user experience

### Negative

- Components must manage update relationships explicitly
