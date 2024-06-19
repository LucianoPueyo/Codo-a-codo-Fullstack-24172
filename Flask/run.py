from flask import Flask
from app.views import *
from app.database import *

app = Flask(__name__)

#Rutas
app.route('/', methods=['GET'])(index)

# Database
# test_connection()
create_table_tareas()
init_app(app)


if __name__ == '__main__':
    app.run(debug=True)