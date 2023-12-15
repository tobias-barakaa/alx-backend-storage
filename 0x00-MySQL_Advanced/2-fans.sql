-- create temporary table

DELIMITER //

CREATE TEMPORARY TABLE band_counts (
  origin VARCHAR(255) PRIMARY KEY,
  fan_count INT NOT NULL DEFAULT 0
);

INSERT INTO band_counts (origin, fan_count)
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin;
//

DELIMITER ;
