from flaskext.script import Manager, Server, Shell

from pdxacm.webapp import app, db
from pdxacm.models.fixtures import home, about, contact


def _make_context():
    return dict(app=app, db=db)


manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server())


@manager.command
def initdb():
    db.drop_all()
    db.create_all()
    db.session.add(about)
    db.session.add(contact)
    db.session.add(home)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
