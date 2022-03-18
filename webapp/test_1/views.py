from flask import Blueprint, render_template, redirect, url_for
from webapp.db import db
from webapp.test_1.forms import KoeficientsForm
from webapp.test_1.models import Koeficients

blueprint = Blueprint('test_1', __name__)


@blueprint.route('/test_1', methods=['GET', 'POST'])
def equation():
    form = KoeficientsForm()
    if form.validate_on_submit():
        write_koefs = Koeficients(koef_a=form.koef_a.data,
                                  koef_b=form.koef_b.data,
                                  koef_c=form.koef_c.data)
        db.session.add(write_koefs)
        if Koeficients.query.count() > 1 :
            first_koefs = Koeficients.query.order_by(Koeficients.id.asc()).first()
            db.session.delete(first_koefs)
        db.session.commit()
        return redirect(url_for('test_1.equation'))

    answer = ''
    koefs = Koeficients.query.order_by(Koeficients.id.desc()).first()
    if koefs:
        a = koefs.koef_a
        b = koefs.koef_b
        c = koefs.koef_c
        form.koef_a.data = a
        form.koef_b.data = b
        form.koef_c.data = c
        answer = calculate_equation(a, b, c)
    title = "Решение квадратного уравнения"
    if form.errors:
        answer = form.errors
    return render_template('test_1/index.html',
                           page_title=title, form=form, answer=answer)


def calculate_equation(a, b, c):
    if a == 0:
        return 'Коэфициент а не может быть равен 0'
    diskr = b**2 - 4 * a * c
    if diskr < 0:
        return 'Уравнение не имеет решений'
    elif diskr == 0:
        x = -b / (2 * a)
        return 'Уравнение имеет 1 решениe x = ' + str(x)
    elif diskr > 0:
        x1 = (-b + diskr**0.5) / (2 * a)
        x2 = (-b - diskr**0.5) / (2 * a)
        return 'Уравнение имеет 2 решения x1 = ' + str(x1) + " x2 = " + str(x2)
