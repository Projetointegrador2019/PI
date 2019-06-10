from flask import Flask, render_template, request, redirect, session
from classe import Pessoa

app= Flask(__name__)

lista = [ ]
app.config["SECRET_KEY"]="1fb8465gfb"

@app.route("/")
def iniciar():
    return render_template ("index.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", lista = lista)

@app.route("/form_inserir_pessoas")
def form_inserir_pessoas():
    return render_template("inserir_pessoas.html")

@app.route("/inserir_pessoas")
def inserir_pessoas():
    nome=request.args.get("nome")
    telefone=request.args.get("telefone")
    tipo_sanguineo=request.args.get("tipo_sanguineo")
    pessoa = Pessoa(nome,telefone,tipo_sanguineo)
    lista.append(pessoa)
    return redirect ("/")

@app.route("/excluir_pessoa")
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
    nome=request.args.get("nome")
    telefone=request.args.get("telefone")
    tipo_sanguineo=request.args.get("tipo_sanguineo")
    nome_original=request.args.get("nome_original")

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
