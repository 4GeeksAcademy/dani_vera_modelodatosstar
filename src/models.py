from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Table, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

usuario_personaje=Table (
    "usuario_personaje",
    db.Model.metadata,
    db.Column("user_id",db.Integer,ForeignKey("user.id")),
    db.Column("personajes_id",db.Integer,ForeignKey("personajes.id"))    
)

usuario_planetas=Table(
    "usuario_planetas",
    db.Model.metadata,
    db.Column("user_id",db.Integer,ForeignKey("user.id")),
    db.Column("planetas_id",db.Integer,ForeignKey("planetas.id"))            
)

class User(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str]=mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)#mail obligatorio y que no se repite
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_personajes=relationship("Personaje",secondary=usuario_personaje, backref="personajes_favoritos")
    favorite_planetas=relationship("Planetas",secondary=usuario_planetas, backref="planetas_favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planetas(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str]=mapped_column(String(25))
    clima: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)#mail obligatorio y que no se repite
    dimension: Mapped[str] = mapped_column(nullable=False)
  
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima":self.clima,
            "dimension":self.dimension,
        }    
    
class Personajes(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str]=mapped_column(String(25))
    especie: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)#mail obligatorio y que no se repite
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"))
  
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie":self.especie,
            "planeta_id":self.planeta_id,
        }    
    