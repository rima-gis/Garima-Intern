# Day 1 — Tuesday — August 9, 2026
**Candidate**: Garima Dhakal
**Work Structure**: [Field / Hybrid / Office] 

## 1. Morning Plan (09:00 – 09:30)
### Today's Target
- [x] Task 1: Read NepTrails overview and write summary

## 1.1 NepTrails Summary
Neptrails is a GIS-based travel-tech startup that maps and improves trail tourism in Nepal. Field teams collect spatial daata using GPS devices, phones, and cameras during trail surveys. This raw data is theen processed through a series of Python scripts inside QGIS, moving  from point data to stitched line data. Processed information is stored in GeoPackage{.gpkg} files and eventually synced with OpenStreetMap, whicch acts as a the mainn external database. Before anything is uploaded, a "Guarded Upload" system checks the data quality and can roll back changes if something goes wrong.