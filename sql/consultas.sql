
-- 1. Top 10 cultivos por valor en 2013
SELECT cultivo, ROUND((SUM(valor)/1000000000.0)::numeric, 2) AS valor_mmdp
FROM produccion
WHERE anio = 2013
GROUP BY cultivo
ORDER BY valor_mmdp DESC
LIMIT 10;

-- 2. Valor y % siniestrado por año
SELECT anio,
       ROUND((SUM(valor)/1000000000.0)::numeric, 2) AS valor_mmdp,
       ROUND((SUM(siniestrada)/SUM(sembrada)*100)::numeric, 1) AS pct_siniestrada
FROM produccion
GROUP BY anio
ORDER BY anio;

-- 3. % siniestrado por año y ciclo
SELECT anio, ciclo,
       ROUND((SUM(siniestrada)/SUM(sembrada)*100)::numeric, 1) AS pct_siniestrada
FROM produccion
GROUP BY anio, ciclo
ORDER BY anio, ciclo;

-- 4. Municipios con más de 40% siniestrado en 2011
SELECT municipio,
       ROUND((SUM(siniestrada)/SUM(sembrada)*100)::numeric, 1) AS pct_siniestrada
FROM produccion
WHERE anio = 2011
GROUP BY municipio
HAVING SUM(siniestrada)/SUM(sembrada) > 0.4
ORDER BY pct_siniestrada DESC;

-- 5. Cultivo principal de cada municipio en 2013 (CTE + ventana)
WITH ranking AS (
    SELECT municipio, cultivo, SUM(valor) AS valor,
           RANK() OVER (PARTITION BY municipio ORDER BY SUM(valor) DESC) AS posicion
    FROM produccion
    WHERE anio = 2013
    GROUP BY municipio, cultivo
)
SELECT municipio, cultivo, ROUND((valor/1000000.0)::numeric, 1) AS valor_millones
FROM ranking
WHERE posicion = 1
ORDER BY valor DESC;

-- 6. Cambio anual del valor en cultivos clave (LAG)
WITH anual AS (
    SELECT cultivo, anio, SUM(valor) AS valor
    FROM produccion
    GROUP BY cultivo, anio
)
SELECT cultivo, anio,
       ROUND((valor/1000000.0)::numeric, 1) AS valor_millones,
       ROUND(((valor - LAG(valor) OVER (PARTITION BY cultivo ORDER BY anio))
              / NULLIF(LAG(valor) OVER (PARTITION BY cultivo ORDER BY anio), 0) * 100)::numeric, 1) AS cambio_pct
FROM anual
WHERE cultivo IN ('MAIZ GRANO', 'TOMATE ROJO (JITOMATE)', 'FRIJOL', 'SORGO GRANO')
ORDER BY cultivo, anio;

