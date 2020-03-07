from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run()


if __name__ == '__main__':
    #main()
    db_session.global_init("db/blogs.sqlite")
    user = User()
    user.name = "Настя"
    user.about = "Биография Насти"
    session = db_session.create_session()
    session.add(user)
    session.commit()