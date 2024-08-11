/* =============================================================================
                      -- Maestría en Ciencia de Datos --
============================================================================= */

/* Utiliza la función TO_CHAR para generar un mensaje con el detalle de las 
   órdenes. El mensaje debe de decir:
   
   "La orden <id_orden> se creó el <dia de la semana, completo> <dia del mes> 
   <mes, completo> de <año> a las <hora a 24>:<minuto> y se entregó el día 
   <dia de la semana, completo> <dia del mes> <mes, abreviado> de <año>"
   
   El mensaje se crea a partir de dos fechas: la fecha de generación de la orden 
   (fecha_orden) y la fecha de la entrega. fecha_orden es de tipo TIMESTAMP, 
   por lo que puedes usar mensajes con hora, minuto y segundo. La fecha de entrega 
   es de tipo DATE y sólo contiene el año, mes y día de la fecha de entrega.
   
   Por ejemplo, si una orden tiene fecha_orden 2012-07-29 17:17:30 y
   fecha_entrega 2020-08-26, la cadena resultante debe de ser la siguiente:
   
   "La orden 10267 se creó el domingo 29 julio de 2012 a las 17:17 y se entregó el día domingo 26 ago de 2012"
   
   Tu consulta debe de generar sólo una columna de nombre "mensaje".
   
   Usa el operador || para concatenar cadenas de texto en el resultado. Por
   ejemplo 'id: ' || id_orden genera la cadena "id: 12345" (para la orden 12345)
   
   Consulta la documentación de los formatos que puedes usar aquí:
   https://www.postgresql.org/docs/10/functions-formatting.html
   
   TIPS:
      - Para formar las cadenas con texto fijo, usa comillas simples, por
        ejemplo: ' la fecha es: ' No uses comillas dobles
      - Asegúrate de cerrar todas las cadenas de texto fijo, por ejemplo
        'la fecha es || fecha
        va a generar un error.
      - Asegurate de usar correctamente el operador de concatenación (||), 
        por ejemplo:
        'la fecha es ' || TO_CHAR(fecha, 'DD/MM/YYYY') ' de la orden'
        la segunda cadena generará un error, ya que no está el operador de
        concatenación entre la cadena que devuelve TO_CHAR y ' de la orden'
      - Revisa bien los espacios en blanco al principio y al final de los
        bloques de texto fijo.
        
   NOTA: No todos los formatos están soportados en este ejercicio.
*/

SELECT 'La orden ' || id_orden || ' se creó el ' || 
    TO_CHAR(fecha_orden, 'FMDay FMDD FMMonth de YYYY') || ' a las ' ||
    TO_CHAR(fecha_orden, 'HH24:MI') || ' y se entregó el día ' ||
    TO_CHAR(fecha_entrega, 'FMDay FMDD FMMon de YYYY') AS mensaje 
FROM ordenes;



