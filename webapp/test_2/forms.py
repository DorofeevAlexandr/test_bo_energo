from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired


class PredictionForm(FlaskForm):
    number = IntegerField('a', validators=[InputRequired()],
                          render_kw={"class": "form-control"})
    submit = SubmitField('Предсказать цвет',
                         render_kw={"class": "btn btn-primary"})
