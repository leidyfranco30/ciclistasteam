Feature: crear un equipo de ciclismo
 Como usuario
 quiero poder agregar ciclistas de diferenres tipos (velocistas,montañistas y contrareloj)
 para que se ajusten a las necesidades de cada competencia
 
 Como usuario
 quiero recibir un mensaje de error claro si intento agregar un ciciista como un tipo desconocido
 para poder corregir el error rapidamente

 Como usuario 
 quiero poder verificar que mi equipo tiene la cantidad correcta de ciclistas despues de agregar

 Como usuario
 quiero poder verificar que cada ciclista tiene el tipo de correcto y esta correctamente registrado

Scenario: Agregar diferentes tipos de ciclistas al equipo
 Given un equipo vacio de ciclistas llamado "Team Bora"
  When yo agrego lo siguientes ciclistas al equipo
  |  tipo           | nombre          | edad   | nacionalidad | atributo especifico|
  | Velocista       |Peter Sagan      | 37     | Irlanda      |         65         |
  | Montanista      |Nairo Quintana   | 35     | Colombia     |         Alta       |
  | Contrarelojista |Tony Martin      | 30     | UK           |         40         |
  Then el equipo debe tener 3 ciclistas
  And el equipo debe tener un ciclista llamado "Peter Sagan" con el tipo velocista
  And el equipo debe tener un ciclista llamado "Nairo Quintana" con el tipo Montanista
  And el equipo debe tener un ciclista llamado "Tony Martin" con el tipo Contrarelojista


Scenario: Agregar un ciclista con un tipo desconocido
 Given un equipo vacio de ciclista llamado "Team Bora"
  When yo agrego lo siguientes ciclistas con un tipo desconocido
  |  tipo           | nombre          | edad   | nacionalidad | atributo especifico|
  | Desconocido     |Rigoberto Uran   | 42     | Colombia     |         70         |
  Then testable outcomehen debe ocurrir un error con el mensaje "Tipo ciclista desconocido"
 
 

 

 
 

 