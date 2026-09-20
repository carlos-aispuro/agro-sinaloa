# Producción agrícola de Sinaloa, 2011-2013

Análisis exploratorio con Python, PostgreSQL y Streamlit.

## Pregunta
¿Cómo cambió el valor de la producción agrícola de Sinaloa entre 2011 y 2013, y qué explica esos cambios?

## Datos
Cierre de la producción agrícola del SIAP (Secretaría de Agricultura): archivos `agt-cierre-2011-2012` y `agt-cierre-2013`, de https://www.agricultura.gob.mx/siap/estadistica. El valor está en pesos corrientes, sin ajustar por inflación. Solo se incluye en el repositorio el CSV filtrado de Sinaloa que usa el dashboard.

## Hallazgos
- El valor total pasó de 23.8 mil millones de pesos en 2011 a 35.6 en 2012 y 33.7 en 2013.
- En 2011 se siniestró el 39.8% de la superficie sembrada, contra 5.6% en 2012 y 11.0% en 2013.
- Alrededor del 89% de esa superficie perdida en 2011 corresponde al ciclo otoño-invierno (45.7% de lo sembrado en ese ciclo). Coincide con las heladas del 2 al 4 de febrero de 2011 descritas en prensa e informes del gobierno estatal (ver fuentes). Los datos muestran cuándo y dónde se dio la pérdida; la causa proviene de esas fuentes externas.
- Las pérdidas de 2011 se concentraron en el norte y centro (Guasave, Culiacán, Navolato, Ahome, Angostura, entre otros). El sur casi no se afectó.
- Maíz: la producción subió de 2.93 a 3.65 millones de toneladas de 2011 a 2012, y el precio implícito (valor entre producción) de 3,671 a 4,038 pesos por tonelada. En 2013 la producción se mantuvo (3.63 millones) y el precio cayó a 3,315, así que la baja de valor de ese año se debe casi por completo al precio.
- En 2012 se sembró menos en otoño-invierno; un informe estatal lo relaciona con el agua usada en la resiembra tras la helada.

## Limitaciones
- Solo tres años y valores nominales (sin inflación).
- El catálogo de cultivos cambia en 2013 (70 cultivos contra 57 en 2012, con menos filas), así que no se comparan cultivos individuales de 2013 con años anteriores sin revisarlo.
- Sumar hectáreas de todos los cultivos puede contar dos veces terreno sembrado en dos ciclos.
- Un informe estatal reporta 194,748 hectáreas siniestradas por la helada de enero de 2013, contra unas 81 mil en otoño-invierno en estos datos. No se investigó la diferencia.

## Cómo reproducirlo
1. Descarga los CSV a la carpeta `data/`.
2. Crea la base `agro_sinaloa` en PostgreSQL y un archivo `.env` con `DB_URL=postgresql+psycopg2://USUARIO:CONTRASEÑA@localhost:5432/agro_sinaloa`.
3. Instala dependencias con `pip install -r requirements.txt` y ejecuta `notebooks/01_exploracion.ipynb`.
4. Consultas SQL en `sql/consultas.sql`. Dashboard con `streamlit run app.py`.

## Fuentes
- La Jornada, 11 de febrero de 2011: https://www.jornada.com.mx/2011/02/11/estados/042n1est
- Portal Frutícola: https://www.portalfruticola.com/?p=8064
- Segundo informe de gobierno de Sinaloa, desarrollo agropecuario: https://media.transparencia.sinaloa.gob.mx/uploads/files/7/SAGYP.2do.informe%20de%20gob.desarrollo%20agropecuario.pdf
