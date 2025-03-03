from flask import current_app as app

@app.route('/')
def home():
    return 'Deploying Flask App'