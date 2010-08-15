from flask import (
    flash,
    g,
    Module,
    redirect,
    render_template,
    request,
    url_for,
)

# from flatland.out.markup import Generator

from pdxacm.models.schema import db, Meeting
# from .util import login_required

# from .forms.pages import PageAddForm, PageEditForm

meetings = Module(__name__)


@meetings.route('/meetings')
def index():
    meetings = Meeting.query.all()
    return render_template("meetings/index.html", meetings=meetings)


@meetings.route('/meetings/view/<int:id>')
def view(id=id):
    meeting = Meeting.query.filter_by(id=id).one()
    from pdb import set_trace; set_trace()
    return render_template("meetings/view.html", md=meeting)
