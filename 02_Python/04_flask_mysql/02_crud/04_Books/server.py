from flask_app.controllers import authors_cont
from flask_app.controllers import books_cont

from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)