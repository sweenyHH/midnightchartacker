# AR-010: Dashboard Enrichment

## Status

Planned

## Goal

Expand the Overview dashboard with additional progression-focused information while preserving the dashboard-first design established in AR-007.

## Motivation

AR-007 introduced the dashboard architecture:

- Character
- PvE
- Resources
- PvP

The architecture is now stable and capable of supporting additional information without further layout redesign.

Future changes should focus on enriching content rather than restructuring the dashboard.

## PvE Dashboard

Potential additions:

### Mythic+

Display:

- Seasonal score
- Future seasonal metrics

### Vault

Display:

- Delve slots
- Raid slots
- Mythic+ slots

using visual indicators.

### Raid Tile

Display:

- Current raid
- Bosses defeated
- Progress summary

if data becomes available.

### Delve Tile

Display:

- Seasonal delve progression
- Relevant endgame milestones

if data becomes available.

## PvP Dashboard

Introduce dedicated rating tiles:

- 2v2
- 3v3
- Rated Battleground
- Solo Shuffle
- Battleground Blitz

Display:

- Current rating
- Rating colorization
- Bracket status

when export data becomes available.

## Resources Dashboard

Continue using data-driven resource selection.

Future improvements may include:

- Resource ordering
- Resource categories
- Expansion-specific resource groupings

All resource visibility decisions shall remain CSV-driven.

## Design Principles

Overview remains:

- Read-only
- Informational
- Dashboard-oriented

Configuration and maintenance actions belong in Tracking.

## Success Criteria

The dashboard continues to answer:

- Who is this character?
- How is PvE progression?
- How is PvP progression?
- Which resources matter?

at a glance without opening additional tabs.