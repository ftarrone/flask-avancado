from flask import Flask, render_template, request,redirect, session, flash, url_for


class Jogos:
    def __init__ (self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogos('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogos('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogos('Mortal Kombat', 'Luta', 'PS2')
list = [jogo1,jogo2,jogo3]


class Usuario:
    def __init__(self,nome,user,password):
        self.nome = nome
        self.user = user
        self.password = password

class Titulo:
    def __init__(self,titulo):
        self.titulo = titulo

app = Flask(__name__)
app.secret_key = 'nando'

@app.route('/')
def home():
    cabecalho = {
        'Nome' : 'Nome'
        ,'Categoria' : 'Categoria'
        ,'Console' : 'Console'
    }
    titulo = Titulo('Jogos')
    return render_template('list.html',titulo = titulo,cabecalho = cabecalho, jogos = list)

titulo = Titulo('Cadastrar Novos Jogos')
@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('logar'))
    else:
        return render_template('cadastro.html',titulo = titulo)
    
@app.route('/criar', methods=['POST',])
def criar():
    titulo = Titulo('Jogos')
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    list.append(jogo)
    return redirect('/') 

titulo = Titulo('Faça seu Login')
@app.route('/login')
def logar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('login.html',titulo = titulo)
    else:    
        return render_template('cadastro.html',titulo = titulo)
        flash(session['usuario_logado'])

mensagem = ''
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'teste123'== request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect(url_for('cadastro'))
    else:
        flash('Usuário ou senha incorretos')
        return redirect(url_for('home'))

@app.route('/loggout', methods=['POST',])
def deslogar ():
    session['usuario_logado'] = None
    return redirect(url_for('home'))        

app.run()
