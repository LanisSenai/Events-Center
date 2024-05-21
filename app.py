import click
from flask import Flask, render_template, request, flash, redirect, url_for
from flask.cli import with_appcontext
from connection import db

app = Flask(__name__)
app.secret_key = "abax"

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:5e5i#123@localhost:3306/flaskola"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flaskola.db"

# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://dbo:5e5i_123@10.134.75.121:1433/eventcenter/?charset=utf8"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
def init_db():
    db.drop_all()
    # db.create_all()
    db.reflect()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""

    init_db()
    click.echo("Initialized the database.")

app.cli.add_command(init_db_command)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/compra", methods=('GET', 'POST'))
def compra():
    
    erros = []
    message = ""

    if request.method=="POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        idade = request.form.get("idade")
        evento = request.form.get("evento")
        valor = request.form.get("valor")

        # Validações 
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")

        if len(erros) == 0:
            #altera usuário no banco de dados
            from model import Inscricao
            inscricao = Inscricao(**{"nome": nome, "email": email, "cpf": cpf, "idade": idade, "evento": evento, "valor": valor, "telefone": telefone, })
            db.session.add(inscricao)
            db.session.commit() # persiste no banco

            message = "Sua reserva for feita com sucesso! Realize o pagamento no local."

    return render_template("compra.html", message=message)

@app.route("/contato", methods=("POST",)) 
def contato():
    import json
    from model import Contato
    erros = []

    # if request.method=="POST":
    nome = request.form.get("nome")
    email = request.form.get("email")
    assunto = request.form.get("assunto")
    mensagem = request.form.get("mensagem")

    # Validações 
    if not nome: erros.append("Nome é um campo obrigatório")
    if not email: erros.append("Email é um campo obrigatório")
    if not assunto: erros.append("Assunto é um campo obrigatório")
    if not mensagem: erros.append("Mensagem é um campo obrigatório")
    
    if len(erros) == 0:
        #altera usuário no banco de dados
        contato = Contato(**{"nome": nome, "email": email, "assunto": assunto, "mensagem": mensagem})
        # Outra forma
        # contato = Contato()
        # contato.nome = nome
        # contato.email = email
        # contato.assunto = assunto
        # contato.mensagem = mensagem

        db.session.add(contato)
        db.session.commit() # persiste no banco

        return "OK"
        # return json.dumps({"status": "OK", "message":f"Sua mensagem, {nome}, foi enviada com sucesso!"})
        # return redirect(url_for('index'))
    return erros
    # return render_template("index.html", erros=erros)

@app.route("/login", methods = ('GET', 'POST'))
def login():
    return render_template("login.html")