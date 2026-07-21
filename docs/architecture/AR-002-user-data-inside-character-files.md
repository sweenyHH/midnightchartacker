# AR-002: Store User Data Inside Character Files

## Status

Implemented

## Context

Features such as:

- Notes
- Weekly Duties
- Vault Progress

require persistent storage.

A decision was needed regarding whether these should be stored in separate files or together with character exports.

## Decision

User-maintained data is stored inside the corresponding character file.

Application-managed sections are separated from imported game data using dedicated storage sections.

## Consequences

### Positive

- One file per character
- User data survives character imports
- Simple backup and migration
- No additional storage layer

### Negative

- Character files become application-specific
- Additional parsing logic required

