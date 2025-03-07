from flask import current_app as app

# Creating the home route
@app.route('/')
def home():
    return 'Deploying Flask App'
# Creating the hello route
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello from GET request'