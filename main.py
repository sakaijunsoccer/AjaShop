from flask import Flask
from flask import Response
from flask import request
from flask import abort

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Top Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'user1' and password == 'pass':
            return '''
             <ul>
              <li>What is AJAIL? $10</li>
              <li>SCRUM Story $5</li>
              <li>How to use JIRA $7</li>
            </ul> 
            '''
        else:
            return abort(401)
    else:
        return Response('''
            <form action="" method="post">
                <p>Username: <input type=text name=username></p>
                <p>Password: <input type=password name=password></p>
                <p><input type=submit></p>
            </form>
        ''')


if __name__ == '__main__':
    app.run()
