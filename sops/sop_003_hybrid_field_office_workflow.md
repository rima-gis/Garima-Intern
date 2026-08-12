# SOP: Hybrid Field + Office Data Workflow

**Author**: Garima Dhakal
**Date**: 2026-08-12
**Objective**: Document the end-to-end process for a half-day hybrid survey — from field GPX/photo collection through transfer, import, and attribute enrichment in QGIS.

---

## Prerequisites
- [x] QGIS installed and project folder set up (NepTrails-Intern)
- [x] GPS tracking app installed on phone (e.g. Geo Tracker)
- [x] OSM Standard basemap available in QGIS for reference
- [x] Git configured for commit/push at end of workflow

## Step-by-Step Procedure

### 1. Field Survey (Morning)
1. Plan a 1.5–2 km route near NepTrails' office.
2. Start GPS tracking app and record the route as a GPX track.
3. Mark waypoints at notable locations along the route (e.g. hazards, viewpoints, landmarks).
4. Take at least 2 photos at notable locations during the survey.
5. Stop recording and export/save the GPX file once back at the office.

### 2. Data Transfer
1. Transfer the GPX file into **`data/day4_hybrid_survey.gpx`**.
2. Transfer photo files into **`data/photos/day4/`**, renamed to match their corresponding waypoint name (e.g. `school.jpg`).
3. Open QGIS, go to **Layer** > **Add Layer** > **Add Vector Layer**, and load the GPX file.
4. Visually verify the track and waypoints align correctly against the OSM Standard basemap.

### 3. Attribute Enrichment
1. In the Layers panel, identify the **waypoints** sublayer (not track_points or route_points).
2. Right-click **waypoints** > **Export** > **Save Features As** > choose GeoPackage format > save as `data/day4_enriched_waypoints.gpkg`.
3. Open the new `day4_enriched_waypoints` layer's attribute table and toggle editing.
4. Use **Field Calculator** to add:
   - `survey_date` (Text) — set to today's date
   - `surveyor` (Text) — set to candidate name
   - `category` (Text) — classify manually per waypoint (rest_stop, viewpoint, hazard, landmark)
5. Check whether a vector road layer is available (via **Layer Properties** > confirm it has an attribute table with fields, not just symbology). If only a raster basemap is available, skip the `nearest_road_distance` join and note this in the SOP/log.
6. Save edits and toggle editing off.

## Verification Steps
*How do you prove the procedure worked correctly?*
- [x] Check that `data/day4_hybrid_survey.gpx` exists and is > 0 KB.
- [x] Verify waypoint count in `day4_enriched_waypoints.gpkg` matches the number marked in the field.
- [x] Confirm `survey_date`, `surveyor`, and `category` fields are populated for every waypoint row (no blanks).
- [x] Confirm at least 2 photos exist in `data/photos/day4/`, named to match their waypoints.
- [ ] Confirm git commit includes GPX, gpkg, photos, and this SOP file.