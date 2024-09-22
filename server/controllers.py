from models import Persona, Ciudad
from db import session


def buscar_persona_por_telefono(telefono):
    persona = session.query(Persona).filter_by(dir_tel=telefono).first()
    if persona:
        ciudad = session.query(Ciudad).filter_by(
            ciud_id=persona.dir_ciud_id).first()
        return persona, ciudad
    return None, None


def obtener_todas_las_personas():
    personas = session.query(Persona).all()
    registros = []
    for persona in personas:
        ciudad = session.query(Ciudad).filter(
            Ciudad.ciud_id == persona.dir_ciud_id).first()
        registros.append((persona, ciudad))
    return registros
