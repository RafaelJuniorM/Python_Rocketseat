from flask import Flask

app = Flask(__name__) # inicializa a aplicação Flask

@app.route('/')
def home():
    return "Hello Wolrd!!"



if __name__ == '__main__': # verifica se o script está sendo executado diretamente - ou importado 
    app.run(debug=True)  # executa a aplicação em modo de depuração