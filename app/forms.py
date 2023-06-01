from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

from . import app
from .models import Category


with app.app_context():
    class NewsForm(FlaskForm):
        title = StringField(
            'Название',
            validators=[
                DataRequired('Поле должно быть заполнено'),
                Length(max=256, message='Название не должно быть длиннее 256 символов')
            ]
        )
        text = TextAreaField('Текст', validators=[DataRequired('Поле должно быть заполнено')])
        category = SelectField(
            'Категория',
            choices=[(category.id, category.title) for category in Category.query.all()]
        )
        submit = SubmitField('Добавить')