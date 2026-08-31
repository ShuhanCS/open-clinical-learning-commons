# Geometry source review

## Accepted source

- Source ID: `TIGER2024-MA-TRACT`.
- Release: 2024 TIGER/Line Massachusetts census tracts.
- Release page: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
- State download interface: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?layergroup=Census+Tracts&year=2024
- Direct archive: https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_25_tract.zip
- Archive bytes: `4,506,627`.
- Archive SHA-256: `74ca27e8dd9ed393e43b75e237ff7d652ef072e413532821847de58a7aa4bfd4`.
- Source-manifest rows: `8`.
- Source-manifest SHA-256: `f1d530f18fd55aacba6d99fbfef847c214c60aba66759e8746bb9713e4d872b0`.

The Census release page states that the legal boundaries and names are as of January 1, 2024, and that the 2024 TIGER/Line Shapefiles were released September 25, 2024. The files contain geographic entity codes that can link to Census demographic data. They do not contain clinical or demographic measures by themselves.

## Archive and geometry acceptance

The archive contains the expected `.cpg`, `.dbf`, `.prj`, `.shp`, two XML metadata files, and `.shx` members. Every member passes its decompressed byte and SHA-256 check.

The accepted geometry has 1,620 rows and 1,620 unique 11-character tract GEOIDs. Every row has state FIPS `25`. The layer spans 14 counties. It contains 1,617 Polygon rows and 3 MultiPolygon rows. All 1,620 geometries are valid; none are null or empty.

The source coordinate system is NAD83 geographic coordinates, EPSG 4269. Area checks use NAD83 Massachusetts Mainland, EPSG 26986. The largest relative difference between projected geometry area and source `ALAND + AWATER` is `0.0001990791`, below the declared `0.001` gate.

## Source role and limit

TIGER supplies official tract keys and boundary geometry. A tract boundary does not define a community, care market, service area, catchment, lived neighborhood, need, vulnerability, priority, eligibility, or authority to act. The source supports a geographic join and teaching display only when the joined measure keeps its own source, period, method, interval, and claim limit.
