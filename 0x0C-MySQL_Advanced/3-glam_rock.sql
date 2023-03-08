-- List glam rock bands
SELECT band_name, split - formed as lifespan FROM metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;