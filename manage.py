from flask.ext.script import Manager

from cosmos import create_app

from flask_failsafe import failsafe

app_factory = failsafe(create_app)
app = app_factory()
manager = Manager(app)

@manager.command
def url_map():
    """Shows registered urls in the application."""
    print app.url_map


@manager.command
def runserver():
    """Runs web application in normal mode."""
    app.run(host='0.0.0.0')


@manager.command
def runserver_debug():
    """Runs web application in debug mode."""
    app.run(host='0.0.0.0', debug=True)


@manager.command
def db_create_all():
    """Create all database tables"""
    from cosmos.framework.database import db
    db.create_all()


@manager.command
def db_drop_all():
    """Create all database tables"""
    from cosmos.framework.database import db
    from flask.ext.script import prompt_bool
    if prompt_bool('Are you sure you want to drop all the tables in the database'):
        db.drop_all()


if __name__ == "__main__":
    manager.run()
