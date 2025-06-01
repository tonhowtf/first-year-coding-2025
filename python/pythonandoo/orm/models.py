from sqlmodel import Field, SQLModel, create_engine
from typing import Optional

class Cursos(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    descricao: Optional[str]
    carga_horaria: int
    qtd_exercicios: int

engine = create_engine("sqlite:///meu_banco.db", echo=True)
SQLModel.metadata.create_all(engine)
