# AR-007 — Split Overview and Tracking

## Status

Implemented

---

## Background

The current `OverviewTab` has grown into two different responsibilities:

### 1. Information Display

Purpose:

Show important character information at a glance.

Examples:

- Character name
- Class
- Specialization
- Level
- Item level
- Gold
- Featured currencies
- Featured reputations
- Weekly status
- Vault status

This is dashboard-style information.

---

### 2. Tracking / Maintenance

Purpose:

Allow the user to manage and track character progress.

Examples:

- Notes
- Weekly duties
- Vault entries
- Character-specific tracking data

This is an editing/maintenance workflow.

---

## Problem

The current `OverviewTab` mixes both responsibilities.

As a result:

- UI feels overloaded
- Dashboard information competes with editing widgets
- Future localization becomes harder
- Future redesign becomes harder
- The tab no longer has a clear purpose

---

## Goal

Split the current functionality into two tabs:

### Overview

Read-only dashboard.

Purpose:

Answer the question:

> "How is this character doing right now?"

### Tracking

Maintenance and tracking tools.

Purpose:

Answer the question:

> "What information do I need to update or manage?"

---

## Phase 1 — Rename Existing Overview

No functional changes.

### Rename

Current:

```text
app/ui/detail/overview_tab.py
```

New:

```text
app/ui/detail/tracking_tab.py
```

### Rename Class

Current:

```python
class OverviewTab(QWidget):
```

New:

```python
class TrackingTab(QWidget):
```

### DetailView Changes

Current:

```python
from .detail.overview_tab import OverviewTab
```

New:

```python
from .detail.tracking_tab import TrackingTab
```

Current:

```python
self.overview_tab = OverviewTab()
```

New:

```python
self.tracking_tab = TrackingTab()
```

Current:

```python
self.tabs.addTab(
    self.overview_tab,
    "Overview"
)
```

New:

```python
self.tabs.addTab(
    self.tracking_tab,
    "Tracking"
)
```

Goal:

Free the filename:

```text
overview_tab.py
```

for the future dashboard implementation.

---

## Phase 2 — Create New OverviewTab

Create:

```text
app/ui/detail/overview_tab.py
```

Purpose:

Dashboard only.

No editing.

No tracking widgets.

No notes.

No maintenance actions.

---

## Initial Overview Content

### Character Summary

- Character Name
- Class
- Specialization
- Level
- Faction
- Average Item Level

---

### Featured Reputations

Source:

```python
featured=True
```

from:

```text
reputations.csv
```

Display using:

```python
reputation_key
```

and localized catalog names.

---

### Featured Currencies

Source:

```python
featured=True
```

from:

```text
currencies.csv
```

Display using:

```python
currency_key
```

and localized catalog names.

---

### Gold

Display total gold.

---

### Weekly Status

High-level summary only.

No editing.

---

### Vault Status

High-level summary only.

No editing.

---

## Phase 3 — Long-Term Improvements

Potential future additions:

### Ready Indicators

Examples:

- Vault complete
- Weekly complete
- Delves complete

---

### Character Alerts

Examples:

- Missing vault entries
- Missing weekly progress
- Currency caps reached

---

### Expansion Dashboards

Examples:

- Midnight
- The War Within

Focused overview cards.

---

## Localization

The new Overview tab must use:

```python
get_display_language()
```

and catalog display helpers.

No direct use of:

```python
rep.name
currency.name
```

for UI labels where a catalog key exists.

Use:

```python
get_reputation_display_name(...)
```

and:

```python
get_currency_display_name(...)
```

instead.

---

## Success Criteria

### Tracking Tab

Contains:

- Notes
- Weekly Duties
- Vault Management

### Overview Tab

Contains:

- Character Dashboard
- Featured Reputations
- Featured Currencies
- High-Level Status Information

### Result

Clear separation between:

Dashboard / Information

and

Tracking / Maintenance