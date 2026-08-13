# Day 5 — Hybrid Track — Sunday, August 14, 2026

## 1. Morning Plan
Process Day 4 field data — add UTM coordinates and descriptions to
waypoints, write a Python automation script, and document the full
hybrid workflow as an SOP.

## 2. Midday Status
Added UTM x/y coordinates and a combined description field to the
enriched waypoints layer via Field Calculator. Exported as CSV.

## 3. End-of-Day Review

### Tasks Completed Today
- [x] Added `utm_x`, `utm_y` fields (EPSG:32645)
- [x] Added `description` field
- [x] Exported enriched dataset to CSV (`data/day5_enriched_waypoints.csv`)
- [x] Wrote and ran `scripts/auto_categorize.py` — added `auto_category` field, categorized all features by elevation threshold (2000m)
- [x] Wrote `sops/sop_004_hybrid_integrated_workflow.md`
- [x] Git commit: "Day 5 hybrid integration"
- [x ] Carried over from Day 4: `nearest_road_distance` spatial join — QuickOSM road layer download was attempted but not completed today

### Lessons Learned
- Field names are case-sensitive in QGIS expressions — confirm exact names in the attribute table before writing an expression.
- QGIS Python Console struggles with pasted multi-line indented code; the Script Editor panel or single-line loops avoid repeated errors.
- Watch for accidental duplicate layers mid-session — fields can end up split across copies.

### SOP Created Today
- [x] Yes → File: `sops/sop_004_hybrid_integrated_workflow.md`

### Tomorrow's Plan
- Await Day 6 capstone assignment and self-assessment form
