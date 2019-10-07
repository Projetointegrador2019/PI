from flask import Flask, redirect, render_template, request, session
from peewee import *

from classe import *
from verificar import *

app= Flask(__name__, static_url_path="", static_folder="templates")

lista = [ ]
app.config["SECRET_KEY"]="1fb8465gfb"

@app.route("/")
def iniciar():
    return render_template ("index.html")

@app.route("/abrir_perfil")
def perfil():
    x = session["usuario"]
    return render_template("perfil.html", pessoa=Pessoa.select().where(Pessoa.login==x))

@app.route("/form_inserir_pessoas")
def form_inserir_pessoas():
    return render_template("cadastro.html")

# inserir uma pessoa
@app.route("/inserir", methods=["POST"])
def inserir():
    
    p = Pessoa.select()
    for i in p:
        if i.login == request.form["login"]:
            return "Já existe uma pessoa com este login. Por favor, tente novamente!" 
   
            
    
        
    # cria uma pessoa com os parâmetros recebidos
    Pessoa.create(nome=request.form["nome_completo"], 
    idade=request.form["idade"], 
    tipo_sanguineo=request.form["tipo_sanguineo"], 
    login=request.form["login"], 
    senha=request.form["senha"], 
    cpf=request.form["cpf"],
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

    # inicializa possível conjunto de inaptidões
    motivos_inaptidao=[]

    #
    # executar uma série de verificações (If's) de possíveis inaptidões
    # (um monte de IFs a seguir)

    if request.form ["ferida"] == "sim":
        motivos_inaptidao.append("Impossível realizar a doação enquanto houverem feridas abertas;")
    
    if request.form ["alimento"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a ingeestão de alimentos inadequados;")
    
    if request.form ["bebidas"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a ingestão de bebidas alcólicas;")

    if request.form ["parceiros"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a existência de mais de um parceiro sexual no período de um ano;")

    if request.form ["repouso"]=="nao":
        motivos_inaptidao.append("Impossível realizar a doação devido ao pouco repouso durante a noite anterior;")

    if request.form ["droga"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido ao uso de drogas ílicita;")

    if request.form ["gravidez"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a gravides ou período de amamentação;")
    
    if request.form  ["dente"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a prodecimentos dentários realizados nos últimos 30 dias;")

    if request.form  ["transfusao"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido transfusão de sangue de pacientes que receberam sangue ou que fazem hemodiálise no período de 1 ano;")

    if request.form ["tatuagens"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a tatuagens, maquiagem definitiva, piercing ou micro pigmentação, no período de 1 ano que antecede o exame;")
    
    if request.form ["gripe"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a sintomas da gripe;")
    
    if request.form ["intestino"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a problemas intestinais;")
    
    if request.form ["parto"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a parto normal ou aborto nos últimos 3 meses que antecedem o exame")

    if request.form ["cirurgia"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a realização de alguma cirurgia nos 12 meses que antecedem o exame")

    if request.form ["vacina"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a vacinação recente;")
    
    if request.form ["convulsao"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a convulsão;")

    if request.form ["medicamento"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a ingestão de medicamentos;")
    
    if request.form ["doenca"]=="sim":
        motivos_inaptidao.append("Impossível realizar a doação devido a Hepatite (após 11 anos de idade),Câncer, AIDS, Doenças autoimunes, Problemas cardíacos, Diabetes, Doença de Chagas ou Hipertireoidismo, tireoidite de Hashimoto")

    # se NÃO houver inaptidões (ou seja, se a pessoa estiver apta :-)
    if motivos_inaptidao==[]:
        return redirect("/listar_pessoas")
    
    # encaminha para a página inicial, mostrando motivos de inaptidão
    return render_template("index.html", lista=motivos_inaptidao)




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
    quem.cpf = request.form["cpf"]
    quem.data_nasc = request.form ["data_nasc"]
    quem.peso = request.form ["peso"]
    quem.altura = request.form ["altura"]

    quem.save()
    return redirect("/")

@app.route("/form_login")
def form_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    login=request.form["login"]
    senha=request.form["senha"]
    if Pessoa.select().where(Pessoa.login==login and Pessoa.senha==senha):
        session["usuario"]=login
    else:
        return "Verifique sua senha"
    return render_template("perfil.html", pessoa=Pessoa.select().where(Pessoa.login==login and Pessoa.senha==senha))
    

@app.route("/logout")
def logout():
    session.pop("usuario")
    return render_template("index.html")

@app.route("/dados_pessoais")
def dados_pessoais():
    return render_template("questionario.html")

@app.route("/perguntas")
def perguntas():
    pass



app.run(debug=True)
