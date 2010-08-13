from flatland import Form, String
from flatland.validation import Present


class PageAddForm(Form):
    title = String.using(label='Title',
                        validators=[Present()])
    text = String.using(label='Content',
                        validators=[Present()])


class PageEditForm(Form):
    text = String.using(label='Content',
                        validators=[Present()])
