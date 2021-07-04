from flask_script import Manager, prompt_bool, Shell, Server
from termcolor import colored

from app import app, db

manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def initdb():
    """ Create the SQL database.
    """
    db.create_all()
    print(colored('The SQL database has been created', 'green'))


@manager.command
def dropdb():
    """ Delete the SQL database.
    """
    if prompt_bool('Are you sure you want to lose all your SQL data?'):
        db.drop_all()
        print(colored('The SQL database has been deleted', 'green'))


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=8880)
@manager.option('-w', '--workers', dest='workers', type=int, default=2)
def gunicorn(host, port, workers):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': '{0}:{1}'.format(host, port),
                'workers': workers
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


manager.add_command('runserver', Server(port=8880))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    print('Starting server')
    manager.run()

