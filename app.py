from flask import Flask, url_for, render_template, request, abort, redirect, json, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'qwertyuiopasdfghjklzxcvbnm'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./news.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return 'hello flask'


@app.route('/users/')
def users():
    # 查询出来的东西都是什么煞笔玩意
    users = User.query.all()
    print(users)
    userlist = [u.__dict__ for u in users]
    return json.dump(users)


@app.route('/hello/', methods=['GET'])
@app.route('/hello/<name>', methods=['GET'])
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/hi')
@app.route('/hi/<name>')
def hi(name=None):
    if name:
        return redirect(url_for('hello', name=name))
    else:
        return redirect(url_for('hello'))


@app.route('/info/', methods=['GET'])
def info():
    app.logger.warn('someone tries to get info ! ')
    abort(404)


@app.route('/json/', methods=['GET'])
def json():
    return jsonify(name='shuai', age=25, pics=[])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
