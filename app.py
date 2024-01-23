from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

app = Flask(__name__)

#create the database
#db = SQLAlchemy(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admindb:72656770@localhost:3306/salessystem'

#login start here
#login = LoginManager(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
