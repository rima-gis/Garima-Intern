# Day 2 — Wednesday — 2026-08-10
**Candidate**: Garima Dhakal
**Work Structure**: Hybrid

---

## 1. Morning Plan (09:00 – 09:30)

### Yesterday's Review
- **What I accomplished yesterday**:
  - Wrote NepTrails summary, confirmed Python/Git/PostgreSQL/QGIS/VS Code all working, set up project folder structure, set QGIS default CRS to EPSG:4326, committed and pushed to GitHub
- **What I did not complete**:
  - N/A — Day 1 tasks were completed
- **Why (if incomplete)**:
  - N/A

### Today's Target
- [x] Task 1: Create `practice_trails.gpkg` with waypoints and trail lines (2.1)
- [x] Task 2: Practice attribute table operations — sort, select by expression, Field Calculator, statistics (2.2)
- [x] Task 3: Filter and export features to a new CRS, then document the process in an SOP (2.3–2.5)

### Questions / Clarifications Needed
- None

---

## 2. Midday Status (After Break)

### Morning Session Review
- **Tasks completed this morning**:
  - Built `practice_trails.gpkg` with 8 waypoints (name, elevation, type) and 3 trail lines (trails_name, length)
  - Sorted and filtered attribute table, added a `Category` field with the Field Calculator, ran Basic Statistics (count: 8, min: 900, max: 2600, mean: 1712.5, median: 1650)
  - Filtered waypoints by `"type" = 'rest_stop' AND "elevation" > 1500` and exported the result to `high_rest_stops.gpkg`, reprojected to EPSG:32645
- **Current blockers**:
  - Hit a "Cannot overwrite an OGR layer in place" error while saving a scratch layer, and later accidentally deleted the exported `high_rest_stops.gpkg` — resolved by re-filtering and re-exporting
- **Adjusted target for afternoon**:
  - Proceed to Python Console exercises and SOP writing as planned

---

## 3. End-of-Day Review (16:35 – 17:00)

### Tasks Completed Today
- [x] `practice_trails.gpkg` created with 8 waypoints and 3 trail lines
- [x] Attribute table operations (sort, select by expression, Field Calculator, statistics)
- [x] `high_rest_stops.gpkg` filtered and exported in EPSG:32645
- [x] Python Console exercises (layer listing, feature count, attribute read, select by expression)
- [x] SOP written and saved

### Lessons Learned
- Mastered Attribute Operations: Practiced sorting, selecting by expressions, and using the Field Calculator to add new attributes and run basic dataset statistics
- Process Documentation: Learned to convert technical vector processing and export steps into a standardized, reproducible Standard Operating Procedure (SOP)
- TPyQGIS Scripting: Learned to interact with QGIS programmatically through the Python Console to read layer lists, query feature counts, attribute records

### SOP Created Today
- [x] Yes → File: `sops/sop_001_filter_export_gpkg.md`

### Tomorrow's Plan
- Continue with Day 3 tasks as assigned