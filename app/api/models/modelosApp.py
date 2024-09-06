from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.declarative import declarative_base

#Crea una instancia de la base para crear tablas
base=declarative_base()

#Lista de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))
    

#GASTO
class Gasto(Base):
    __tablename__='gasto'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(String(20))
    fecha=Column(Date)
    descripcion=Column(String(50))
    nombre=Column(String(50))
#CATEGORIA
class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer,primary_key=True, autoincrement=True )
    nombreCategoria=Column(String(50))
    descripcion=Column(String(50))
    fotoicono=Column(Integer)
#METODOS DE PAGO
class MetodoPago(Base):
    __tablename__='metodopago'
    id=Column(Integer,primary_key=True, autoincrement=True ) 
    nombreMetodo=Column(String(50))
    descripcion=Column(String(50))
#FACTURAS
class Factura(Base):
    pass