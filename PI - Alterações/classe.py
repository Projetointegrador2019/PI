from peewee import *



db=SqliteDatabase("doacao_sangue5.db")


class Modelo(Model):
    class Meta:
        database=db



class Pessoa(Modelo):
    nome= CharField()
    idade= CharField()
    tipo_sanguineo =CharField()
    login=CharField()
    senha=CharField()
    cpf=CharField()
    data_nasc=CharField()
    peso=CharField()
    altura=CharField()
    

    ferida = CharField()
    alimento = CharField()
    bebidas = CharField()
    parceiros = CharField()
    repouso = CharField()
    droga = CharField()
    gravidez = CharField()
    dente = CharField() 
    transfusao = CharField() 
    tatuagens = CharField()
    gripe = CharField()
    intestino = CharField()
    parto = CharField()
    cirurgia = CharField()
    vacina = CharField()
    convulsao = CharField()
    medicamento = CharField()
    doenca = CharField()
    apto=CharField(default="nao")


db.connect()
db.create_tables([Pessoa])