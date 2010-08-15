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

from pdxacm.models.schema import db, Page
from .util import login_required

from .forms.pages import PageAddForm, PageEditForm

pages = Module(__name__)


@pages.route('/', defaults={'title': 'home'})
@pages.route('/<any(about, contact):title>')
@pages.route('/view/<int:id>')
@pages.route('/view/<title>')
def view(id=None, title=None):

    if id:
        md = Page.query.filter_by(id=id).one()
    elif title:
        md = Page.query.filter_by(title=title).one()
    else:
        return redirect('/404.html')

    return render_template("pages/md.html",
                           md=md)


@pages.route('/pages/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        form = PageAddForm.from_flat(request.form)
        form.validate()
        page = Page(title=form['title'].value,
                    text=form['text'].value,
                    last_edited_by=g.user.id)
        db.session.add(page)
        db.session.commit()
        flash("Your page was successfully added", "success")
        return redirect(url_for('view', title=page.title))

    form = PageAddForm()
    gen = Generator()

    return render_template("edit_page.html",
                           func='add',
                           form=form,
                           html=gen)


@pages.route('/edit', defaults={'title': 'home'}, methods=['GET', 'POST'])
@pages.route('/<any(about, contact, home, minutes):title>/edit',
            methods=['GET', 'POST'])
@pages.route('/pages/edit/<int:id>', methods=['GET', 'POST'])
@pages.route('/pages/edit/<string:title>', methods=['GET', 'POST'])
@login_required
def edit(id=None, title=None):
    if request.method == 'POST':
        form = PageEditForm.from_flat(request.form)
        if form.validate():
            page = Page.query.filter_by(title=title).one()
            page.text = form['text'].value
            page.last_edited_by = g.user.id
            db.session.add(page)
            db.session.commit()
            flash("Your page was saved", "success")
            return redirect(url_for('view', title=page.title))

        else:
            if page.text == None:
                form['text'].add_error('Text content is required')
                gen = Generator()
                flash("Form submission failed, see errors", "failure")
                return render_template("edit_page.html", form=form, html=gen)

    if id:
        page = Page.query.filter_by(id=id).one()
    elif title:
        page = Page.query.filter_by(title=title).one()

    form = PageEditForm({'text': page.text})
    gen = Generator()

    return render_template("edit_page.html",
                           func='edit',
                           form=form,
                           html=gen,
                           page=page)
