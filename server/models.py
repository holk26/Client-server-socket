from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Ciudad(Base):
    __tablename__ = 'ciudades'
    ciud_id = Column(Integer, primary_key=True)
    ciud_nombre = Column(String, nullable=False)


class Persona(Base):
    __tablename__ = 'personas'
    dir_tel = Column(String, primary_key=True)
    dir_tipo_tel = Column(String)
    dir_nombre = Column(String, nullable=False)
    dir_direccion = Column(String, nullable=False)
    dir_ciud_id = Column(Integer, ForeignKey(
        'ciudades.ciud_id'), nullable=False)

    ciudad = relationship("Ciudad", back_populates="personas")


Ciudad.personas = relationship(
    "Persona", order_by=Persona.dir_tel, back_populates="ciudad")
