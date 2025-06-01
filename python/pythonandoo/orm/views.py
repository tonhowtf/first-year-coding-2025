from models import Cursos, engine
from sqlmodel import Session, select, or_



with Session(engine) as session:
    statement = select(Cursos).where(Cursos.id == 1)
    results = session.exec(statement).first()
    results.nome = "Arcane"
    results.descricao = "Curso de Python"
    session.add(results)