# Day 3 — Thursday — 2026-08-11

**Candidate**: Garima Dhakal
**Work Structure**: Hybrid

---

## 1. Morning Plan (09:00 – 09:30)

### Yesterday's Review
- **What I accomplished yesterday**:
  - Built `practice_trails.gpkg` (8 waypoints, 3 trail lines), practiced attribute table operations (sort, select by expression, Field Calculator, statistics)
  - Filtered and exported `high_rest_stops.gpkg` (reprojected to EPSG:32645), ran PyQGIS Console exercises (layer listing, feature count, attribute read, select by expression)
  - Wrote SOP: `sops/sop_001_filter_export_gpkg.md`
- **What I did not complete**:
  - N/A — Day 2 tasks were completed
- **Why (if incomplete)**:
  - N/A

### Today's Target
- [x] Task 1: Understand GPX data structure (tracks, waypoints, segments)
- [x] Task 2: Record a real GPX track (≥1 km) with ≥3 named waypoints, import into QGIS
- [x] Task 3: Perform spatial analysis (track length, elevation statistics) and write SOP

### Questions / Clarifications Needed
-

---

## 2. Midday Status (After Break)

### Morning Session Review
- **Tasks completed this morning**:
  - Reviewed GPX data structure and key concepts (tracks, waypoints, segments)
  - Recorded a GPX track around Sitapaila (near NepTrails office) using Geo Tracker for Android
  - Track length: 1111.29 m; 3 named waypoints marked: Nursery, School, Cafe
- **Current blockers**:
  -N/A
- **Adjusted target for afternoon**:
  - Proceed with QGIS import, styling, and spatial analysis as planned

---

## 3. End-of-Day Review (16:35 – 17:00)

### Tasks Completed Today
- [x] Recorded `my_track.gpx` (1111.29 m, 3 named waypoints: Nursery, School, Cafe) via Geo Tracker for Android
- [x] Imported GPX into QGIS (track_points, tracks, waypoints sublayers)
- [x] Styled tracks layer (red line, width 2) and waypoints layer (yellow circle marker, size 8)
- [x](my_tracks_screenshot_qgis.png)
- [x] Verified track alignment against basemap — track follows real street shapes correctly
- [x] Reprojected tracks layer to EPSG:32645 (UTM Zone 45N) and calculated track length: **1111.3 m**
- [x] Calculated elevation statistics on track_points (`ele` field):
  - Minimum: 1264.7 m
  - Maximum: 1307.84 m
  - Mean: 1286.53 m
  - Standard deviation: 11.65 m
  - Elevation gain (Max − Min): 43.14 m
  
- [x] Wrote SOP: `sops/sop_002_gpx_import_analysis.md`

### Lessons Learned
- A GPX track can contain multiple `trkseg` segments if the GPS loses signal or recording is paused/resumed — this is expected behavior, not an error (observed a segment break near the Cafe waypoint)
- GPX layers loaded directly into QGIS are read-only; editing attributes requires exporting to an editable format (e.g. GeoPackage) first

### SOP Created Today
- [x] Yes → File: `sops/sop_002_gpx_import_analysis.md`

### Tomorrow's Plan
-  Continue with Day 4  tasks as assigned
