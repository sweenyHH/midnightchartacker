# AR-001: Character Export Files As Primary Datastore

## Status

Accepted

## Context

Midnight Character Tracker imports character data from text-based character exports.

The application requires persistent storage for character information while remaining simple to use and easy to distribute.

Introducing a database would increase installation complexity and maintenance effort.

## Decision

Character export files are used as the primary datastore.

Each character is represented by a single text file that contains imported game data and application-specific user data.

## Consequences

### Positive

- No database dependencies
- Simple backup process
- Human-readable files
- Easy troubleshooting
- Simplified installer and deployment

### Negative

- Changes require file parsing
- Large-scale querying is less efficient than a database

