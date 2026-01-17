from flask import Flask


app = Flask(__name__) # isntancia do Flask 


@app.route('/')
def teste():
    return "Isso é um testeeeee!!!"


if __name__ == '__main__':
    app.run(debug=True)  # executa o servidor Flask em modo de depuração