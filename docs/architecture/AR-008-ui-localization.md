# AR-008: Introduce Multi-Language User Interface

## Status

Planned

## Goal

Provide a fully localized user interface for all supported application languages.

The application already supports:

- Localized currency names
- Localized item currency names
- Localized number formatting

This architecture record extends localization support to all user interface elements.

## Motivation

Currently, most UI strings are hardcoded in English.

Examples:

- PvE
- PvP
- Character Resources
- Mythic+
- Vault
- Honor Level
- Honor Progress
- Item Level

This creates an inconsistent experience when the user has selected German or French.

A fully localized UI is required for a polished 2.0 release.

## Supported Languages

- English
- German
- French

The language system shall remain extensible for future languages.

## Scope

### Localization Infrastructure

Introduce a centralized localization layer for all UI strings.

The localization system shall:

- Avoid hardcoded UI labels
- Support runtime language switching
- Remain independent from business logic
- Be simple to maintain

### Overview Tab

Localize:

- PvE
- PvP
- Character Resources
- Mythic+
- Vault
- Delves
- Raid
- Honor Level
- Honor Progress
- Item Level

### Tracking Tab

Localize all:

- Headers
- Labels
- Buttons
- Placeholder texts
- Tooltips

### Detail View

Localize:

- Overview
- Tracking
- Equipment
- Currencies
- Progress
- Additional tabs

### Main Window

Localize:

- Menus
- Dialogs
- Settings
- Theme selection
- Language selection

### Messages

Localize:

- Information dialogs
- Warning messages
- Error messages

## Architectural Principles

Localization files shall only contain text.

Business logic must never depend on language-specific strings.

Canonical internal identifiers remain language-independent.

## Success Criteria

The application can be fully displayed in:

- English
- German
- French

without requiring an application restart.

All visible UI strings are sourced from the localization layer.