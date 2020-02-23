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
                Username: <input type=text name=username> <br>
                Password: <input type=password name=password> <br>
                <input type=submit>
            </form>
        ''')


if __name__ == '__main__':
    app.run()
