from flask import (
    g,
    Module,
    redirect,
    render_template,
    request,
    url_for,
)

from flatland.out.markup import Generator

from pdxacm.models.schema import db, Page
from .util import login_required

from .forms.pages import PageForm

page = Module(__name__)


@page.route('/', defaults={'title': 'home'})
@page.route('/<any(about, contact, events, minutes):title>')
@page.route('/view/<int:id>')
def view(id=None, title=None):
    if id:
        md = Page.query.filter_by(id=id).one()
    elif title:
        md = Page.query.filter_by(title=title).one()
    else:
        return redirect('/404.html')

    return render_template("md.html",
                           md=md.text)


@page.route('/pages/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        form = PageForm.from_flat(request.form)
        page = Page(title=form['title'].value,
                    text=form['text'].value,
                    last_edited_by=g.user.id)
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('view', title=page.title))

    form = PageForm()
    gen = Generator()

    return render_template("edit_page.html",
                           func='add',
                           form=form,
                           html=gen)


@page.route('/pages/edit/<int:id>', methods=['GET', 'POST'])
@page.route('/pages/edit/<string:title>', methods=['GET', 'POST'])
@login_required
def edit(id=None, title=None):
    if request.method == 'POST':
        form = PageForm.from_flat(request.form)
        page = Page.query.filter_by(title=form['title'].value).one()
        page.text = form['text'].value
        page.last_edited_by = g.user.id
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('view', title=page.title))

    if id:
        page = Page.query.filter_by(id=id).one()
    elif title:
        page = Page.query.filter_by(title=title).one()

    form = PageForm({'title': page.title,
                     'text': page.text})
    gen = Generator()

    return render_template("edit_page.html",
                           func='edit',
                           form=form,
                           html=gen)
