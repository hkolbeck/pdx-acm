from flatland import String
from flatland.validation import Present

from .pages import PageAddForm, PageEditForm


class EventAddForm(PageAddForm):
    title = String.using(label='Title',
                        validators=[Present()])
    text = String.using(label='Content',
                        validators=[Present()])
    location = String.using(label='Location',
                        validators=[Present()])


class EventEditForm(PageEditForm):
    text = String.using(label='Content',
                        validators=[Present()])
    location = String.using(label='Location',
                        validators=[Present()])
