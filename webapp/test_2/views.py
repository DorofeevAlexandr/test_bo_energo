from flask import Blueprint, render_template, redirect, url_for
from webapp.db import db
from webapp.test_2.forms import PredictionForm
from webapp.test_2.models import ColoredOjects, ProbabilityColoredObjects


blueprint = Blueprint('test_2', __name__)


@blueprint.route('/test_2_create', methods=['GET'])
def prediction_create_new_objects():
    create_new_objects()
    return redirect(url_for('test_2.prediction'))


@blueprint.route('/test_2', methods=['GET', 'POST'])
def prediction():
    answer = ''
    form = PredictionForm()
    if form.validate_on_submit():
        answer = prediction_color()
        n = form.number.data
        c_obj = ColoredOjects.query.filter_by(number=n).first()
        if c_obj:
            if not(c_obj.selected):
                update_probability(c_obj.obj_color)
                c_obj.selected = True
                db.session.add(c_obj)
                db.session.commit()
    list_col_obj = []
    for c_obj in ColoredOjects.query.order_by(ColoredOjects.number).all():
        list_col_obj.append({'number': c_obj.number,
                             'obj_color': c_obj.obj_color,
                             'selected': c_obj.selected})
    title = "Предсказание цвета предметов"
    if form.errors:
        answer += str(form.errors)
    return render_template('test_2/index.html',
                           page_title=title,
                           form=form,
                           answer=answer,
                           list_col_obj=list_col_obj)


def update_probability(color_name):
    prob_col_obj = ProbabilityColoredObjects.query.order_by(ProbabilityColoredObjects.id.asc()).first()
    if prob_col_obj:
        prob_col_obj.number_samples += 1
        if color_name == 'blue':
            prob_col_obj.number_blue_samples += 1
        elif color_name == 'green':
            prob_col_obj.number_green_samples += 1
        elif color_name == 'red':
            prob_col_obj.number_red_samples += 1
        db.session.add(prob_col_obj)
        db.session.commit()


def prediction_color():
    prob_col_obj = ProbabilityColoredObjects.query.order_by(ProbabilityColoredObjects.id.asc()).first()
    if prob_col_obj:
        number_samples = prob_col_obj.number_samples
        number_blue_samples = prob_col_obj.number_blue_samples
        number_green_samples = prob_col_obj.number_green_samples
        number_red_samples = prob_col_obj.number_red_samples
        if number_samples and number_samples != 0:
            probability_blue = number_blue_samples / number_samples
            probability_green = number_green_samples / number_samples
            probability_red = number_red_samples / number_samples
        else:
            probability_blue = 1
            probability_green = 0
            probability_red = 0
        comment = ' b=' + str(probability_blue) + ' g=' + str(probability_green) + ' r=' + str(probability_red)
        comment = ''
        if probability_blue >= max(probability_green, probability_red):
            return 'Синий' + comment
        if probability_green >= max(probability_blue, probability_red):
            return 'Зеленый' + comment
        if probability_red >= max(probability_green, probability_blue):
            return 'Красный' + comment
    return None


class Colored_Object():
    def __init__(self, collor, number=None) -> None:
        self.number = number
        self.collor = collor
        self.selected = False

    def __repr__(self) -> str:
        return str(self.number) + str(self.color)


def create_100_objects():
    result = set()
    for n in range(1, 86):
        result.add(Colored_Object(collor='blue'))
    for n in range(86, 96):
        result.add(Colored_Object(collor='green'))
    for n in range(96, 101):
        result.add(Colored_Object(collor='red'))
    return result


def create_new_objects():
    _100_obj = create_100_objects()
    for n, obj in enumerate(_100_obj, start=1):
        write_obj = ColoredOjects(obj_color=obj.collor, number=n, selected = False)
        db.session.add(write_obj)
        if ColoredOjects.query.count() > 100:
            first_obj = ColoredOjects.query.order_by(ColoredOjects.id.asc()).first()
            db.session.delete(first_obj)
    db.session.commit()

    write_obj = ProbabilityColoredObjects(number_samples=0,
                                          number_blue_samples=0,
                                          number_green_samples=0,
                                          number_red_samples=0)
    db.session.add(write_obj)
    if ProbabilityColoredObjects.query.count() > 1:
        first_obj = ProbabilityColoredObjects.query.order_by(ProbabilityColoredObjects.id.asc()).first()
        db.session.delete(first_obj)
    db.session.commit()
