# https://www.youtube.com/watch?v=7RWro4VF_9c
#https://www.youtube.com/watch?v=IolxqkL7cD8
import os

from flask import Flask
# import os

db_user = 'my_db_user'
# db_password = 'my_db_pass__123!'

db_user = os.environ.get('DB_USER')

db_password = os.environ.get('DB_PASS')



app = Flask(__name__)
# app.config.from_envvar('APP_SETTINGS')
# app.config['DEBUG']= False

@app.route('/')
def index():
    return db_password

if __name__ == '__main__' :
    app.run()
