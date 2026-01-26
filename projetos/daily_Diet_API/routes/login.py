import app

@app.route('/login', methods=['POST'])
def login():
    return "Login route"
    