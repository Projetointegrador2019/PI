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
	ferida=BooleanField()
	alimento=BooleanField()
    bebidas=BooleanField()
    parceiros=BooleanField()
    repouso=BooleanField()
    droga=BooleanField()
    gravidez=BooleanField()
    dente=BooleanField() 
    transfusao=BooleanField() 
    tatuagens=BooleanField()
    gripe=BooleanField()
    intestino=BooleanField()
    parto=BooleanField()
    cirurgia=BooleanField()
    vacina=BooleanField()
    convulsao=BooleanField()
    medicamento=BooleanField()
    doenca=BooleanField()

