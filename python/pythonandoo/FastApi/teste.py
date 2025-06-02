from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {'mensagem': '/'}

@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'Cadastro'}


@app.get("/login")
def login():
    return {'mensagem': 'Login'}