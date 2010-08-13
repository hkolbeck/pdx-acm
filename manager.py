from flaskext.script import Manager, Server, Shell

from pdxacm.webapp import app, db


def _make_context():
    return dict(app=app, db=db)


manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server())


@manager.command
def initdb():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()
