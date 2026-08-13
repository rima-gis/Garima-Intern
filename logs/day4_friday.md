# Day 4 — Friday — August 12, 2026
**Candidate**: Garima Dhakal
**Work Structure**: Hybrid

---

## 1. Morning Plan (09:00 – 09:30)

### Yesterday's Review
- **What I accomplished yesterday**:
  - Recorded a GPX track with 3 named waypoints near Sitapaila, imported and styled in QGIS, calculated track length/elevation stats, wrote sop_002_gpx_import_analysis.md
- **What I did not complete**:
  - nearest_road_distance — not completed 

- **Why (if incomplete)**: (reason: OSM Standard was a raster basemap only, no vector road layer available for spatial join)
  -

### Today's Target
- [x] Task 1: Conduct a 1.5–2 km field survey near NepTrails' office, record GPX + waypoints + photos
- [x] Task 2: Transfer and enrich waypoint data in QGIS
- [x] Task 3: Write sop_003_hybrid_field_office_workflow.md

### Questions / Clarifications Needed
- Confirmed OSM Standard layer was a raster basemap only (no vector road layer), so nearest_road_distance was not applicable

---

## 2. Midday Status (After Break)

### Morning Session Review
- **Tasks completed this morning**:
  - Completed field survey (~1.5–2 km route near NepTrails' office), recorded GPX track, marked [7] waypoints, took [12] photos
  - Transferred GPX to data/day4_hybrid_survey.gpx and photos to data/photos/day4/
  - Loaded GPX into QGIS, verified alignment against basemap
- **Current blockers**:
  - None
- **Adjusted target for afternoon**:
  - Proceed as planned with attribute enrichment and SOP writing

---

## 3. End-of-Day Review (16:35 – 17:00)

### Tasks Completed Today
- [x] Field survey conducted, GPX track and waypoints recorded near NepTrails' office
- [x] Data transferred and verified in QGIS
- [x] Exported waypoints to data/day4_enriched_waypoints.gpkg
- [x] Added survey_date, surveyor, category fields via Field Calculator
- [ ] nearest_road_distance — not completed (reason: OSM Standard was a raster basemap only, no vector road layer available for spatial join)
- [x] Wrote sop_003_hybrid_field_office_workflow.md

### Lessons Learned
- Distinguishing waypoints vs. track_points/route_points layers after GPX import is important before exporting
- A basemap tile layer (e.g. OSM Standard) is not the same as a queryable vector layer — need to check via Layer Properties before assuming a spatial join is possible

### SOP Created Today
- [x] Yes → File: `sops/sop_003_hybrid_field_office_workflow.md`

### Tomorrow's Plan
-Await Day 5 worksheet/task assignment