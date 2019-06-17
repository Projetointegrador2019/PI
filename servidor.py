from flask import Flask, render_template, request, redirect, session
from classe import * 
from peewee import *

app= Flask(__name__)

lista = [ ]
app.config["SECRET_KEY"]="1fb8465gfb"

@app.route("/")
def iniciar():
    return render_template ("index.html")

@app.route("/listar_pessoas")
def listar_pessoas(): 
    return render_template("perfil.html", lista = Pessoa.select())

@app.route("/form_inserir_pessoas")
def form_inserir_pessoas():
    return render_template("questionario.html")

@app.route("/inserir", methods=["POST"])
def inserir_pessoas():
    Pessoa.create(nome=request.form["nome_completo"], 
    idade=request.form["idade"], 
    tipo_sanguineo=request.form["tipo_sanguineo"], 
    email=request.form["email"],
    login=request.form["login"], 
    senha=request.form["senha"], 
    CPF=request.form["cpf"],
    data_nasc=request.form["data_nasc"], 
    peso=request.form["peso"],
    altura=request.form["altura"], 
    ferida = request.form ["ferida"], 
    alimento=request.form ["alimento"], 
    bebidas=request.form ["bebidas"],
    parceiros=request.form ["parceiros"], 
    repouso=request.form ["repouso"],
    droga=request.form ["droga"],
    gravidez=request.form ["gravidez"] ,
    dente=request.form  ["dente"], 
    transfusao=request.form  ["transfusao"],
    tatuagens=request.form ["tatuagens"], 
    gripe=request.form ["gripe"], 
    intestino=request.form ["intestino"], 
    parto=request.form ["parto"] ,
    cirurgia=request.form ["cirurgia"],
    vacina=request.form ["vacina"], 
    convulsao=request.form ["convulsao"], 
    medicamento=request.form ["medicamento"],
    doenca=request.form ["doenca"])



    return redirect ("/")


@app.route("/excluir_pessoa", methods=["POST"])
def excluir_pessoa():
    excluir=None
    nome=request.args.get("nome")
    
    for pessoa in lista:
        if nome==pessoa.nome:
            excluir=pessoa
            break
    
    if excluir != None:
        lista.remove(excluir)
    
    return redirect("/listar_pessoas")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    nome = request.args.get("nome")
    for pessoa in lista:
        if nome==pessoa.nome:
            return render_template("form_alterar_pessoa.html", pessoa=pessoa)
        else:
            return redirect("/listar_pessoas")

@app.route("/alterar_pessoa")
def alterar_pessoa():
    nome=request.form["nome"]
    idade= request.form["idade"]
    tipo_sanguineo = request.form["tipo_sanguineo"]
    email = request.form["email"]
    login= request.form["login"]
    senha= request.form["senha"]
    CPF= request.form["cpf"]
    data_nasc= request.form ["data_nasc"]
    peso = request.form ["peso"]
    altura = request.form ["altura"]
    ferida = request.form ["ferida"]
    alimento=request.form ["alimento"]
    bebidas=request.form ["bebidas"]
    parceiros=request.form ["parceiros"]
    repouso=request.form ["repouso"]
    droga=request.form ["droga"]
    gravidez=request.form ["gravidez"]
    dente=request.form  ["dente"]
    transfusao=request.form  ["transfusao"]
    tatuagens=request.form ["tatuagens"]
    gripe=request.form ["gripe"]
    intestino=request.form ["intestino"]
    parto=request.form ["parto"]
    cirurgia=request.form ["cirurgia"]
    vacina=request.form ["vacina"]
    convulsao=request.form ["convulsao"]
    medicamento=request.form ["medicamento"]
    doenca=request.form ["doenca"]
    
    indice= -2
    for i in range(len(lista)):
        if lista[i].nome==nome_original:
            indice=i
            break
    
    if indice>=0:
        lista[indice]= Pessoa(nome,telefone, tipo_sanguineo)
    
    return redirect("/listar_pessoas")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=["POST"])
def login():
    login=request.form["login"]
    senha=request.form["senha"]
    if login == "adm" and senha=="adm":
        session["usuario"]=login
        return redirect ("/")
    else:
        return "Login/Senha invalidos!"

@app.route("/logout")
def logout():
    session.pop("usuario")

@app.route("/dados_pessoais")
def dados_pessoais():
    return render_template("questionario.html")

@app.route("/perguntas")
def perguntas():
    pass

app.run(debug=True)
