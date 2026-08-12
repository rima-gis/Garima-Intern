# SOP: How to Import and Analyze GPX Data in QGIS

**Author**: Garima Dhakal
**Date**: 2026-08-11
**Objective**: Transfer a field-recorded GPX track into QGIS, style it, and calculate its length and elevation statistics.

---

## Prerequisites
- [x] QGIS installed and open, with the project's default basemap (OSM Standard, CRS EPSG:4326)
- [x] A recorded `.gpx` file (track + at least 3 named waypoints), transferred to the computer
- [x] GPX file placed in the project's data folder (e.g. `NepTrails-Intern/data/my_track.gpx`)

## Step-by-Step Procedure

### 1. Transfer GPX from Phone to Computer
1. Record the track using a GPS tracking app (e.g. Geo Tracker for Android), marking at least 3 named waypoints along the way.
2. Once recording is complete, export the track as a `.gpx` file from within the app.
3. Transfer the file to the computer (email attachment, WhatsApp/Telegram, or Google Drive upload/download).
4. Rename the file descriptively and place it in `NepTrails-Intern/data/my_track.gpx`.
`
### 2. Load GPX Layers in QGIS
1. Open QGIS. Go to **Layer** > **Add Layer** > **Add Vector Layer**.
2. Browse to `my_track.gpx` and select it.
3. When prompted, tick all relevant sublayers: `track_points`, `tracks`, `waypoints`.
4. Double-click the **tracks** layer > **Symbology** tab > set a bright color and line width `2`.
5. Double-click the **waypoints** layer > **Symbology** tab > set marker shape to star or circle, size `8`.
6. Right-click the **tracks** layer > **Zoom to Layer**.

### 3. Calculate Track Length
1. Open the **tracks** layer's Attribute Table > **Field Calculator**.
2. Create a new field `length_meters` (Decimal number / Real), expression `$length`.
3. If the layer's CRS is EPSG:4326, this result is in **degrees**, not meters — reprojection is required.
4. Right-click **tracks** > **Export** > **Save Features As** > Format: GeoPackage > CRS: `EPSG:32645` (UTM Zone 45N, correct for Nepal) > save as a new layer (e.g. `tracks_utm`).
5. Open the new layer's Attribute Table > Field Calculator > recreate `length_meters` with the same expression `$length`. This result is now in meters.

### 4. Calculate Elevation Statistics
1. Go to **Vector** > **Analysis Tools** > **Basic Statistics**.
2. Set Input layer to **track_points**, Field to `ele`. Run.
3. Record Minimum, Maximum, Mean, and Standard deviation from the report.
4. Elevation gain can be approximated as Maximum minus Minimum.

### 5. Verify Track Alignment with the Basemap
1. Visually compare the track's shape against the basemap (roads, buildings) after zooming to layer.
2. Optionally add satellite imagery via **Layer** > **Add Layer** > **Add XYZ Layer** for a clearer visual check.
3. If the track appears significantly offset from real-world features, this indicates a CRS mismatch — confirm the layer's CRS matches the project CRS and reproject if necessary.

## Verification Steps
*How do you prove the procedure worked correctly?*
- [x] `tracks_utm` layer exists with a `length_meters` field showing a value in the hundreds/thousands (not a small decimal in degrees).
- [x] `waypoints` layer contains the expected number of named points (e.g. 3).
- [x] Track visually follows real streets/paths on the basemap, without significant offset.
- [x] Basic Statistics report on `ele` returns non-null Minimum, Maximum, Mean, and Standard deviation values.

## Notes
-  A GPX track may contain multiple `trkseg` segments if the GPS loses signal or recording is paused/resumed. This is expected behavior, not an error.

- GPX layers loaded directly into QGIS are read-only. To edit attribute values, export the layer first (Export > Save Features As > GeoPackage), then edit the new layer.