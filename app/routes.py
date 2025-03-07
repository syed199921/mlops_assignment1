from flask import current_app as app

@app.route('/')
def home():
    return 'Deploying Flask App'

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello from GET request'

# @app.route('/hello1post', methods=['GET'])
# def hello_post():
#     return 'Hello from another GET request'