# AR-011: Remove Redundant UI Tabs

## Status

Planned

## Goal

Simplify the Detail View by removing tabs that do not provide unique user-facing functionality.

## Motivation

The introduction of the Overview dashboard and the Overview / Tracking split (AR-007) has made some tabs redundant.

These tabs duplicate information already available elsewhere while consuming valuable navigation space.

## Remove Vault Tab

The Vault tab displays information that is already available in:

- Tracking (editing)
- Overview PvE Vault Tile (viewing)

The tab does not provide unique functionality.

## Remove Debug Tab

The Debug tab is intended for development and troubleshooting workflows.

Developer-facing functionality should not be exposed in the release UI.

## Expected Result

Detail View navigation becomes:

- Overview
- Tracking
- Currencies
- Stats
- Reputation

The application focuses on user-facing functionality and improves information density.