from . import bp as app
from flask import render_template, redirect


user_data = {


}

@app.route('/users/')
def users():
    return user_data

@app.route('/user/username/<username>')
def user(username):
    if username not in user_data:
        return 'User not found'

    return user_data[username]


@app.route('/user/id/<id>')
def user_by_id(id):
    for key, user in user_data.items():
        if user['user_id'] == int(id):
            return user

    return 'User not found'


@app.route('/')
@app.route('/index')
def index():
    user_info = {
        'name':'User'
    }
    return render_template('index.html', user=user_info)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user_name.data == 'admin' and form.password.data == 'admin':
            flash('login successful')
            return redirect('index')
    return render_template('login.html', form=form)