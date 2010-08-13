from flatland import Form, String
from flatland.validation import Present


class PageForm(Form):
    title = String.using(label='Title',
                        validators=[Present()])
    text = String.using(label='Content',
                        validators=[Present()])
