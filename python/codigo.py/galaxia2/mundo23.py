from datetime import timedelta
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import pytz

def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

separador('A partir da função date')

data_sem_horas = date(2022, 8, 31) # ano, mês, dia
print(data_sem_horas)

separador('A partir da função datetime')

data_completa = datetime(2022, 8, 31, 20, 30, 56) # ano, mês, dia, hora, minuto, segundo

print(data_completa)

separador('A partir de uma string')

data_texto = "18/04/1987"

data_python = datetime.strptime(data_texto, '%d/%m/%Y')
print(data_python)

separador('A partir de um datetime')

data_python = data_python.date()

print(data_python)

separador('extraindo informações de datas')

lista_datas = [date(2020, 3, 5), date(2021, 3, 5), date(2021, 4, 5)]

for data in lista_datas:

    print(data.year)
    print(data.month)
    print(data.day)

separador('pegando o horário de agora')

data_agora = datetime.now()

print(data_agora)

separador('Criando timedeltas')

timedelta_teste = timedelta(days = 7, minutes = 10)

print(timedelta_teste)

amanha = datetime.now() + timedelta_teste

print(amanha)

separador('usando relativedelta')

final_desse_ano = date(2022, 12, 31)

final_ano_que_vem = final_desse_ano + relativedelta(years = 1)

print(final_ano_que_vem)

separador('formatação de datas (gráficos, leituras, etc)')

data_texto = "18/04/1987"
data_texto2 = "18-04-87"
data_texo3 = "jan-01"

data_python = datetime.strptime(data_texto, '%d/%m/%Y')
data_python2 = datetime.strptime(data_texto2, '%d-%m-%y')
data_python3 = datetime.strptime(data_texo3, '%b-%y')   

print(data_python)
print(data_python2)
print(data_python3)

separador('fuso horarios')

for tz in pytz.all_timezones:
    print(tz)  

tz_sp = pytz.timezone('America/Sao_Paulo')
tz_ny = pytz.timezone('America/New_York')

data_agora_sp = datetime.now(tz_sp)
data_agora_ny = datetime.now(tz_ny)

print(data_agora_sp)  
print(data_agora_ny)

separador('Exercício 28')

dia_da_data = datetime.now().day
mes_da_data = datetime.now().month
ano_da_data = datetime.now().year
hora_da_data = datetime.now().hour
minuto_da_data = datetime.now().minute
segundo_da_data = datetime.now().second

separador('exercicio 29')

data = input("Digite a data no formato dd/mm/yyyy: ")
data = datetime.strptime(data, '%d/%m/%Y')
data_ontem = timedelta(days = 1) - data
data_ano_que_vem = relativedelta(years = 1) - data
print(data)
