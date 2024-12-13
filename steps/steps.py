from behave import given, when, then
from ciclista import EquipoCiclista,Velocista,Montanista,Contrarelojista

@given ('un equipo vacio de ciclistas llamado"(team_name)"')
def step_given_empty_cycling_team(context,team_name):
    context.teams = EquipoCiclista(team_name)
    
@when('yo agrego los siguientes ciclistas al equipo')
def step_when_add_cyclist(context):
    for row in context.table:
        tipo = row['tipo']
        nombre = row['nombre']
        edad = row['edad']
        nacionalidad = row['nacionalidad']
        atributo_especifico = row['atributo especifico']
        try:
            if tipo =='velocista':
                ciclista = Velocista(nombre,edad,nacionalidad, int (atributo_especifico))
            elif tipo == 'Montanista':
                ciclista = Montanista(nombre,edad,nacionalidad, int (atributo_especifico))
            elif tipo == 'Contrarelojista':
                ciclista = Contrarelojista(nombre,edad,nacionalidad, int (atributo_especifico))
            else:
                raise ValueError("Tipo de ciclista desconocido")
            context.team.agregar_ciclista(ciclista)
        except ValueError as e:
            context.error_message = str(e)
@then('el equipo debe tener{expected_count:d} ciclistas')
def step_then_team_should_have_cyclists(context, expected_count):
    assert len(context.team.ciclistas) == expected_count, f"El valor esperado era {expected_count} pero se encontró{len(context.team.ciclistas)}"

@then('el equipo debe tener un clicista llamado "{nombre}" con el tipo {tipo}"')
def step_then_team_should_include_cyclist(context,nombre,tipo):
    found=False
    for ciclista in context.team.ciclistas:
        if ciclista.nombre == nombre and ciclista.__class__.__name__==tipo:
            found = True
            break
    assert found, f"Cilista llamado{nombre} con el tipo {tipo} no encontrado en el equipo"

@then('debe ocurrir un error con el mensaje"Tipo de ciclista desconocido"{expected_message}')
def step_then_error_message(context, expected_message):
    assert context.error_messaged == expected_message, f"El mensaje de error esperado era'{expected_message}' pero se encontro '{context.error_message}'"
            
        
    
        
    