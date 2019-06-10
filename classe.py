from peewee import *

class Pessoa():
    nome= CharField()
    idade= CharField()
    tipo_sanguineo =CharField()
    email =CharField()
    login=CharField()
    senha=CharField()
    CPF=CharField()
    data_nasc=CharField()
    peso=CharField()
    altura=CharField()

class PerguntasDoDoador():
	ferida=CharField()
	alimento=CharField()