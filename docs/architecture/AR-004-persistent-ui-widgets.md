# AR-004: Use Persistent UI Widgets Instead Of Rebuilding Views

## Status

Accepted

## Context

OverviewTab and VaultTab originally recreated large parts of the user interface during refresh operations.

This increased complexity and contributed to visual refresh issues.

## Decision

UI elements are created once during widget initialization.

Character changes update existing widgets rather than rebuilding them.

## Consequences

### Positive

- Better performance
- Reduced complexity
- More predictable UI behavior
- Improved responsiveness

### Negative

- Widgets must handle state updates correctly
