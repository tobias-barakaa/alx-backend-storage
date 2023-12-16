SELECT band_name, 
       CASE 
           WHEN formed = 0 OR split = 0 THEN 0
           ELSE 2022 - GREATEST(formed, split)
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;

