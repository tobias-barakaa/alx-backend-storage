-- Calculate lifespan for each band with Glam rock as the main style
SELECT
    band_name,
    IFNULL(YEAR(2022) - formed, 0) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
