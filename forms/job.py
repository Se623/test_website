from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Название работы', validators=[DataRequired()])
    leader = StringField('id лидера', validators=[DataRequired()])
    work_size = StringField('Продолжительность', validators=[DataRequired()])
    collaborators = StringField('Участники работы', validators=[DataRequired()])
    is_finish = BooleanField('Запомнить меня')
    submit = SubmitField('Добавить')