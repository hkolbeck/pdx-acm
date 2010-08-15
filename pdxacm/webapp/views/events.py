from flask import (
    flash,
    g,
    Module,
    redirect,
    render_template,
    request,
    url_for,
)

from flatland.out.markup import Generator

from pdxacm.models.schema import db, Event

from .util import login_required
from .forms.events import EventAddForm, EventEditForm

events = Module(__name__)


@events.route('/events')
def index():
    events = Event.query.all()
    return render_template("events/index.html", events=events)


@events.route('/events/view/<int:id>')
def view(id=id):
    event = Event.query.filter_by(id=id).one()
    return render_template("pages/md.html", md=event)


@events.route('/events/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        form = EventAddForm.from_flat(request.form)
        if form.validate():
            event = Event(title=form['title'].value,
                         text=form['text'].value,
                         location=form['location'].value,
                         last_edited_by=g.user.id)
            db.session.add(event)
            db.session.commit()
            flash("Your page was successfully added", "success")
            return redirect(url_for('view', id=event.id))
        else:
            if event.text == None:
                form['text'].add_error('Text content is required')
                gen = Generator()
                flash("Form submission failed, see errors", "failure")
                return render_template("events/edit.html", form=form, html=gen)

    form = EventAddForm()
    gen = Generator()

    return render_template("events/edit.html",
                           func='add',
                           form=form,
                           html=gen)

# @events.route('/events/add')
# def add(id=id):
#     event = Event.query.filter_by(id=id).one()
#     return render_template("pages/md.html", page=event)
