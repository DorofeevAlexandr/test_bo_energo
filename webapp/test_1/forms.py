from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired


class KoeficientsForm(FlaskForm):
    koef_a = FloatField('a', validators=[InputRequired()],
                        render_kw={"class": "form-control"})
    koef_b = FloatField('b', validators=[InputRequired()],
                        render_kw={"class": "form-control"})
    koef_c = FloatField('c', validators=[InputRequired()],
                        render_kw={"class": "form-control"})
    submit = SubmitField('Найти корни уравнения',
                         render_kw={"class": "btn btn-primary"})
