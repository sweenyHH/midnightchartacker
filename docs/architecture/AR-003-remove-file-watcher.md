# AR-003: Replace File Watcher With Explicit Refresh Flow

## Status

Implemented

## Context

The application originally monitored the import directory using a file watcher.

The watcher automatically refreshed application data when files changed.

During testing, the watcher caused:

- unnecessary reloads
- self-triggered refreshes
- user experience issues
- increased architectural complexity

Additional mechanisms such as debounce logic and internal write tracking became necessary.

## Decision

The file watcher was removed.

Application refreshes are now triggered explicitly by user actions such as:

- Character Import
- Character Deletion
- Returning to the Character List
- Settings Changes

## Consequences

### Positive

- Simpler architecture
- Improved responsiveness
- Improved maintainability
- Fewer race conditions
- More predictable behavior

### Negative

- External manual file changes are not detected automatically
- User must reload through application restart
