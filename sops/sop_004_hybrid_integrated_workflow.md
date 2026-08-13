# SOP: Hybrid Field-Office Data Workflow

**Author**: Garima Dhakal
**Date**: 2026-08-14
**Objective**: Enrich field-collected waypoints with UTM coordinates, descriptions, and automated categorization, then export and version-control the results.

---

## Prerequisites
- [x] QGIS installed and working
- [x] GPX field data already recorded and imported (see SOP 003)
- [x] `day4_enriched_waypoints.gpkg` (or equivalent enriched waypoints layer) available
- [x] QGIS Python Console accessible

## Step-by-Step Procedure

### 1. Field Data Recap
1. Confirm the waypoints layer from the field survey is loaded in QGIS.
2. Open the attribute table and check that `name`, `Category`, and `ele` (elevation) fields are populated.

### 2. Add UTM Coordinate Fields
1. Open the attribute table for the waypoints layer.
2. Click **Field Calculator** (abacus icon).
3. Create a new field named `utm_x`, type **Decimal number (real)**, with expression:
   `x(transform($geometry, 'EPSG:4326', 'EPSG:32645'))`
4. Repeat, creating `utm_y` with expression:
   `y(transform($geometry, 'EPSG:4326', 'EPSG:32645'))`

### 3. Add Description Field
1. Open **Field Calculator** again.
2. Create a new field named `description`, type **Text (string)**, with expression:
   `"name" || ' - ' || "Category" || ' (' || "ele" || 'm)'`
3. Confirm field names in the expression exactly match the attribute table (case-sensitive).

### 4. Export Enriched Dataset
1. Right-click the layer > **Export** > **Save Features As**.
2. Set format to **CSV**.
3. Save to `data/day5_enriched_waypoints.csv`.

### 5. Run Automated Categorization Script
1. Open **Plugins > Python Console**, then open the **Script Editor**.
2. Paste in `scripts/auto_categorize.py`.
3. Click **Run**. The script:
   - Locates the enriched waypoints layer
   - Starts an edit session if not already active
   - Adds an `auto_category` field if not already present
   - Loops through all features, labeling each `High Altitude` (elevation > 2000m) or `Standard`
   - Commits changes

 ### 6. Version Control
1. Open the **Source Control** panel in VS Code (branch icon, left sidebar).
2. Review the list of changed files.
3. Enter commit message: `Day 5 hybrid integration`.
4. Click **Commit**.
5. Click **Sync Changes** (or **Push**) to push to GitHub.

## Verification Steps
*How do you prove the procedure worked correctly?*
- [x] `utm_x` and `utm_y` fields contain non-null decimal values for every feature
- [x] `description` field shows readable text (not `NULL` or blank) for every feature
- [x] Exported CSV file size is > 0 and opens correctly in a spreadsheet program
- [x] `auto_category` field is populated with either `High Altitude` or `Standard` for every feature — no blanks
- [x] Feature count in the CSV matches the feature count in the original QGIS layer (8, per today's dataset)

