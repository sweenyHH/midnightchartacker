# AR-012: Canonical Character Stat Identifiers And Catalog-Based Localization

## Status

Implemented

## Goal

Introduce canonical internal identifiers for character statistics and equipment data while localizing all user-facing names through catalogs.

This architecture extends the catalog pattern already established for:

- Currencies
- Item Currencies
- Reputations

to additional character data domains.

## Motivation

Character exports originate from World of Warcraft clients that may use different languages.

Examples:

### Attributes

English export:

```text
Strength
Agility
Intellect
Stamina
```

German export:

```text
Stärke
Beweglichkeit
Intelligenz
Ausdauer
```

### Combat Ratings

English export:

```text
Critical Strike
Haste
Mastery
Versatility
```

German export:

```text
Kritischer Treffer
Tempo
Meisterschaft
Vielseitigkeit
```

### Equipment Slots

English export:

```text
Head
Neck
Shoulder
Chest
```

German export:

```text
Kopf
Hals
Schulter
Brust
```

The export language is not under application control and cannot be standardized.

Using export strings directly as UI text results in mixed-language displays and prevents reliable localization.

## Architectural Principle

The application shall never use export names directly as user-facing display text.

Instead:

```text
Export Name
    ↓
Catalog Lookup
    ↓
Canonical Internal Identifier
    ↓
Localized Display Name
```

shall be used consistently.

## New Catalogs

### Attribute Catalog

Introduce:

```text
attributes.csv
attribute_catalog.py
attribute_definition.py
```

Example:

```csv
key;english_name;german_name;french_name
strength;Strength;Stärke;Force
agility;Agility;Beweglichkeit;Agilité
intellect;Intellect;Intelligenz;Intelligence
stamina;Stamina;Ausdauer;Endurance
```

### Combat Rating Catalog

Introduce:

```text
combat_ratings.csv
combat_rating_catalog.py
combat_rating_definition.py
```

Example:

```csv
key;english_name;german_name;french_name
critical_strike;Critical Strike;Kritischer Treffer;Coup critique
haste;Haste;Tempo;Hâte
mastery;Mastery;Meisterschaft;Maîtrise
versatility;Versatility;Vielseitigkeit;Polyvalence
```

### Equipment Slot Catalog

Introduce:

```text
equipment_slots.csv
equipment_slot_catalog.py
equipment_slot_definition.py
```

Example:

```csv
key;english_name;german_name;french_name
head;Head;Kopf;Tête
neck;Neck;Hals;Cou
shoulder;Shoulder;Schulter;Épaules
chest;Chest;Brust;Torse
```

## Required Catalog Features

Each catalog shall support:

### Lookup By Canonical Key

```python
get_attribute_by_key(
    "strength"
)
```

### Lookup By Export Name

```python
get_attribute_by_name(
    "Strength"
)

get_attribute_by_name(
    "Stärke"
)

get_attribute_by_name(
    "Force"
)
```

All lookups shall return the same canonical identifier.

### Localized Display Names

```python
get_attribute_display_name(
    "strength",
    "de",
)
```

returns:

```text
Stärke
```

## Parser Responsibilities

Parsers shall convert export text into canonical identifiers during parsing.

Example:

```text
Strength
```

↓

```python
strength
```

Example:

```text
Stärke
```

↓

```python
strength
```

The internal model shall only store canonical identifiers.

## UI Responsibilities

UI components shall never display raw export values.

All display names must be obtained through catalog display functions.

Example:

```python
get_attribute_display_name(...)
```

instead of:

```python
attribute.name
```

## Benefits

### Consistent Localization

All supported languages receive consistent terminology.

### Export Language Independence

English, German and French exports produce identical internal data.

### Stable Internal Model

Application logic remains language-independent.

### Reusable Architecture

The solution follows the same successful architecture already used for:

- Currency catalogs
- Item currency catalogs
- Reputation catalogs

## Success Criteria

The application stores:

```text
strength
critical_strike
head
```

internally regardless of export language.

All displayed names originate from catalog localization.

Changing the application display language immediately changes the displayed names without requiring different export data.