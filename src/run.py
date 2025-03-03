# Running the flask application from the run.py file
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# End of run.py code :)
