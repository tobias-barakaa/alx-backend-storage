-- Calculate lifespan for each band with Glam rock as the main style
SELECT
    band_name,
    IFNULL(
        CASE
            WHEN split IS NOT NULL THEN split - formed
            ELSE YEAR(2022) - formed
        END,
        0
    ) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
