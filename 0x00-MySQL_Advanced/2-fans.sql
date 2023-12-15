-- cript that ranks country origins of bands

DELIMITER //

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
//

DELIMITER ;
