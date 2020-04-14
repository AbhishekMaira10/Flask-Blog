from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# secret keys help protect the forms from modifying cookies, cross-site request forgery attack
app.config['SECRET_KEY'] = '6fa73538fe5688211055ed30dd556b17'

posts = [
    {
        'author': 'Abhishek Maira',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 8, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 9, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/Login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
