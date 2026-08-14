# SOP: NepTrails Hybrid Team Member — Daily Operations Manual

**Author**: Garima Dhakal
**Date**: 2026-08-14
**Objective**: Enable a new hybrid team member to independently complete a full field-to-database survey cycle, from morning planning through final data enrichment, using only this manual.

---

## Prerequisites
- [x] QGIS installed and working, with project CRS set (EPSG:4326 default; EPSG:32645 for measurements)
- [x] OSM Standard basemap layer available in the project
- [x] GPS tracking app installed on mobile device (e.g. Geo Tracker) with high-accuracy mode enabled
- [x] Git repository cloned locally, with `data/`, `sops/`, and `scripts/` folders present
- [x] Python environment working in QGIS (for `scripts/auto_categorize.py` or equivalent)

## Step-by-Step Procedure

### 1. Morning Planning
1. Open QGIS and load the working project with the OSM Standard basemap visible.
2. Create a new temporary scratch **Line** layer named `[dayN]_planned_route`.
3. Toggle editing, then click **Add Line Feature**, and trace a route along real visible roads/paths on the basemap (prefer a closed loop over out-and-back).
4. Finish the line with a double-click, then check its length via **Field Calculator** — confirm it's close to the day's target distance (e.g. ~1 km).
5. Save the layer.

### 2. Field Survey
1. Open the tracking app and confirm GPS accuracy is high and signal is present.
2. Tap **Start Track**, name it `[dayN]_survey`, at the exact start point.
3. Walk the planned loop, turning consistently in one direction at junctions to close the loop without retracing the path.
4. Drop a minimum of 3 named waypoints along the way (e.g. "Nursery," "School," "Cafe") at meaningful landmarks.
5. Optionally photograph each waypoint.
6. Tap **Stop Track** back at the start point.

### 3. Data Transfer and Import
1. Export the GPX file from the tracking app.
2. Move it into `data/[dayN]_survey.gpx` in the project folder (and photos into `data/photos/[dayN]/`, if captured).
3. In QGIS, go to **Layer > Add Layer > Add GPX Layer**, select the file, and load the track and waypoint layers.
4. Style the imported track/waypoints distinctly from the planned route layer for visual comparison.

### 4. Attribute Enrichment and Automation
1. Open the waypoint layer's attribute table and add fields: `survey_date`, `surveyor`, `category`, `utm_x`, `utm_y`, `description`.
2. Reproject to EPSG:32645 and populate `utm_x`/`utm_y` via Field Calculator using `$x` / `$y`.
3. Export the enriched layer to `data/[dayN]_enriched_waypoints.gpkg` (and CSV if needed).
4. Run `scripts/auto_categorize.py` (or equivalent) to apply consistent categorization logic rather than tagging manually.

### 5. Documentation and Commit
1. Update the daily log with a summary of what was planned vs. completed, files produced, and any gaps encountered.
2. Run `git add .`, then `git commit -m "[DayN] [brief summary]"`, then `git push`.

## Verification Steps
*How do you prove the procedure worked correctly?*
- [ ] Planned route length and actual track length are within a reasonable margin of each other
- [ ] Track forms a closed loop with no unexplained gaps or overlapping segments
- [x] Waypoint count in QGIS matches the count recorded in the field
- [x] All enrichment fields (`survey_date`, `surveyor`, `category`, `utm_x`, `utm_y`) are populated with no blanks
- [x] Exported `.gpkg`/`.csv` file size is greater than 0 and opens correctly in QGIS
- [x] Git commit is pushed and visible in the remote repository

## Known Gaps
- - The planned route and the actual walked track may not always match exactly — small deviations (a missed turn, GPS drift, an obstacle on the ground) can happen and should be noted rather than assumed to be an error.
- - If turns aren't taken consistently in one direction, the loop may not close properly and the distance can end up well over target — as happened on this attempt. A future version of this SOP could include a step to check the live GPS trail every few hundred meters to catch this earlier.