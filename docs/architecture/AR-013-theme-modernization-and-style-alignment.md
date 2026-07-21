# AR-013: Theme Modernization And Style Alignment

## Status

Planned

## Goal

Review and modernize all application themes to align with the architectural and UI changes introduced during the 2.0 development cycle.

The visual design should consistently support the current user experience across all major screens and supported display languages.

## Motivation

The application UI has evolved significantly since the themes were originally created.

Recent architectural and UI changes include:

- AR-007 Overview And Tracking Split
- AR-008 Multi-Language User Interface
- AR-011 Remove Redundant UI Tabs
- AR-012 Canonical Character Stat Identifiers And Catalog-Based Localization

As a result, some visual styling no longer reflects the current structure of the application.

Several newly introduced widgets and layouts either rely on generic styling or have not been reviewed across all supported themes.

## Scope

### Overview Dashboard

Review styling for:

- Character card
- PvE section
- PvP section
- Character Resources section
- Vault indicators
- Resource tiles
- Status indicators

Ensure visual consistency and balanced information density.

### Tracking View

Review styling for:

- Notes widget
- Weekly Duties widget
- Vault Progress widget

Ensure:

- Consistent spacing
- Consistent typography
- Clear section hierarchy
- Appropriate padding and margins

### Detail View

Review:

- Tab appearance
- Selected tab styling
- Hover states
- Spacing
- Visual consistency between themes

Verify that localized labels fit properly within tabs.

### Character Table

Review:

- Table header styling
- Checkbox alignment
- Row spacing
- Class-color presentation
- Sorting indicator visibility
- Task column readability

### Dialogs

Review:

- Settings Dialog
- Paste Dialog
- Warband Tasks Dialog

Ensure:

- Consistent button styling
- Consistent spacing
- Consistent typography
- Proper sizing for translated text

### Theme Consistency

Review all supported themes:

- Dark Theme
- Light Theme
- Modern Theme
- WoW Theme

Verify that all screens remain usable and visually coherent.

### Localization Compatibility

Validate all supported UI languages:

- English
- German
- French

Ensure:

- No clipped text
- No overlapping text
- No broken layouts
- Acceptable spacing for longer translations

### Widget-Specific Styling

Review custom widget styles including:

- Overview dashboard cards
- Status indicators
- Resource panels
- Table headers
- Dashboard section headers
- Tracking widgets

Replace temporary or inherited styling with dedicated theme definitions where appropriate.

## Out Of Scope

This AR does not introduce:

- New dashboard features
- New business functionality
- Additional themes

The goal is visual alignment and polish only.

## Success Criteria

All supported themes:

```text
Dark
Light
Modern
WoW
```

correctly support the complete 2.0 user interface.

All newly introduced widgets have appropriate styling.

No layout issues occur due to localization.

The visual appearance is consistent across:

- Overview
- Tracking
- Character Table
- Dialogs
- Detail Views

The application is visually ready for the 2.0 release.

## Expected Outcome

The application transitions from a feature-focused development UI to a polished product-quality interface suitable for public release as Warband Manager 2.0.