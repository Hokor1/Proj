from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///бібліотека.db'
app.config['SECRET_KEY'] = 'секретний_ключ'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'вхід'

@app.route('/')
def головна():
    книги = Book.query.all()
    return render_template('головна.html', книги=книги)

@app.route('/вхід', methods=['GET', 'POST'])
def вхід():
    if request.method == 'POST':
        email = request.form['email']
        пароль = request.form['пароль']
        користувач = User.query.filter_by(email=email).first()
        if користувач and check_password_hash(користувач.пароль, пароль):
            login_user(користувач)
            return redirect(url_for('панель_контролю'))
        else:
            flash('Невірний email або пароль')
    return render_template('вхід.html')

@app.route('/реєстрація', methods=['GET', 'POST'])
def реєстрація():
    if request.method == 'POST':
        ім’я = request.form['ім’я']
        email = request.form['email']
        пароль = generate_password_hash(request.form['пароль'])
        користувач = User(ім’я=ім’я, email=email, пароль=пароль)
        db.session.add(користувач)
        db.session.commit()
        flash('Реєстрація пройшла успішно')
        return redirect(url_for('вхід'))
    return render_template('реєстрація.html')

@app.route('/вихід')
@login_required
def вихід():
    logout_user()
    return redirect(url_for('головна'))

@app.route('/панель_контролю')
@login_required
def панель_контролю():
    книги = Book.query.all()
    return render_template('панель_контролю.html', книги=книги)

@app.route('/додати_книгу', methods=['GET', 'POST'])
@login_required
def додати_книгу():
    if request.method == 'POST':
        назва = request.form['назва']
        автор = request.form['автор']
        isbn = request.form['isbn']
        категорія_id = request.form['категорія']
        автор_id = request.form['автор']
        книга = Book(назва=назва, автор=автор, isbn=isbn, категорія_id=категорія_id, автор_id=автор_id)
        db.session.add(книга)
        db.session.commit()
        flash('Книга додана успішно')
        return redirect(url_for('панель_контролю'))
    категорії = Category.query.all()
    автори = Author.query.all()
    return render_template('додати_книгу.html', категорії=категорії, автори=автори)

if __name__ == '__main__':
    app.run(debug=True)