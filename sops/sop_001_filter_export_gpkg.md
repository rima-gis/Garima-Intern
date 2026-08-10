# SOP: How to Filter and Export Features from a GeoPackage

**Author**: Garima Dhakal
**Date**: 2026-08-10
**Objective**: Filter a layer by attribute values and export the result to a new GeoPackage with a different CRS.

---

## Prerequisites
- [ ] QGIS open on your computer
- [ ] A layer already loaded (points or lines) that has some data columns you can filter by — for example, a layer with a "type" column and an "elevation" column

## Step-by-Step Procedure

### 1. Filter the Layer
1. Open QGIS and make sure your layer is loaded and visible in the Layers list on the left.
2. Right-click on the layer's name.
3. Click **Filter...** A small window will pop up.
4. In the box, type your condition. For example, to only show rest stops above 1500m:
   `"type" = 'rest_stop' AND "elevation" > 1500`
5. Click **Test** — this tells you how many points match, without changing anything yet.
6. Click **OK**. Now only the matching points will show on the map and in the table.

### 2. Export the Filtered Features
1. Right-click the same layer again.
2. Click **Export**, then click **Save Features As...**
3. Where it says Format, choose **GeoPackage**.
4. Click the **...** button next to the file name box, and choose the folder where you want to save it (for example, your `data` folder).
5. Type a name for the new file, like `high_rest_stops.gpkg`.
6. Type a name for the layer inside that file, like `high_rest_stops`.
7. Where it says CRS, search for `32645` and pick **EPSG:32645 - WGS 84 / UTM zone 45N**.
8. Click **OK**. Your new file is now saved.

## Verification Steps
*How do you prove the procedure worked correctly?*
- [ ] Open the new file in QGIS and look at its table — the number of points should match what the Test button showed earlier.
- [ ] Right-click the new layer, click **Properties**, then the **Source** tab, and check that it says EPSG:32645.
- [ ] Look in your folder and make sure the new file is actually there and is not 0 KB in size.