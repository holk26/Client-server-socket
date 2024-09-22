from models import Ciudad, Persona
from db import session

ciudades = [
    Ciudad(ciud_id=1, ciud_nombre='Bogotá'),
    Ciudad(ciud_id=2, ciud_nombre='Medellín'),
    Ciudad(ciud_id=3, ciud_nombre='Cali'),
    Ciudad(ciud_id=4, ciud_nombre='Barranquilla'),
    Ciudad(ciud_id=5, ciud_nombre='Cartagena')
]

personas = [
    Persona(dir_tel='1234567890', dir_tipo_tel='Móvil',
            dir_nombre='Juan Pérez', dir_direccion='Calle 1', dir_ciud_id=1),
    Persona(dir_tel='0987654321', dir_tipo_tel='Móvil',
            dir_nombre='María López', dir_direccion='Calle 2', dir_ciud_id=2),
    Persona(dir_tel='5551234567', dir_tipo_tel='Fijo',
            dir_nombre='Carlos Gómez', dir_direccion='Calle 3', dir_ciud_id=3),
    Persona(dir_tel='4449876543', dir_tipo_tel='Fijo',
            dir_nombre='Ana Martínez', dir_direccion='Calle 4', dir_ciud_id=4),
    Persona(dir_tel='7776543210', dir_tipo_tel='Móvil',
            dir_nombre='Luis Torres', dir_direccion='Calle 5', dir_ciud_id=5)
]

session.add_all(ciudades)
session.add_all(personas)
session.commit()
