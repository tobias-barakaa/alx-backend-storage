-- Calculate the total number of non-unique fans for each country
CREATE TEMPORARY TABLE temp_origin_fans AS
SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin;

-- Rank the countries based on total non-unique fans
SET @rank = 0;
SELECT
    origin,
    nb_fans,
    @rank := @rank + 1 AS rank
FROM
    temp_origin_fans
ORDER BY
    nb_fans DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temp_origin_fans;
