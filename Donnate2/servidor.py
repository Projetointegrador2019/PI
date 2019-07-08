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
    return render_template("cadastro.html")

@app.route("/inserir", methods=["POST"])
def inserir():
    Pessoa.create(nome=request.form["nome_completo"], 
    idade=request.form["idade"], 
    tipo_sanguineo=request.form["tipo_sanguineo"], 
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

    #dados da verificacao


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


    if ferida == "sim": 
        return "impossivel doar no momento devido a feridas"    
    return redirect("/listar_pessoas")



@app.route("/excluir_pessoa")
def excluir_pessoa():
   Pessoa.delete_by_id(request.args.get("id"))
   return redirect("/")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    quem=Pessoa.get_by_id(request.args.get("id"))
    return render_template("form_alterar_pessoa.html", pessoa=quem)

@app.route("/alterar_pessoa", methods = ['POST'])
def alterar_pessoa():
    quem = Pessoa.get_by_id(request.form["id_original"])
    quem.nome = request.form["nome_completo"]
    quem.idade = request.form["idade"]
    quem.tipo_sanguineo = request.form["tipo_sanguineo"]
    quem.login = request.form["login"]
    quem.senha = request.form["senha"]
    quem.CPF = request.form["cpf"]
    quem.data_nasc = request.form ["data_nasc"]
    quem.peso = request.form ["peso"]
    quem.altura = request.form ["altura"]

    quem.save()
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
