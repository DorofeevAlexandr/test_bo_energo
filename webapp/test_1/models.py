from webapp.db import db


class Koeficients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    koef_a = db.Column(db.Float, nullable=True)
    koef_b = db.Column(db.Float, nullable=True)
    koef_c = db.Column(db.Float, nullable=True)

    def __repr__(self):
        result = f'{self.id}, '
        result += f'a = {self.koef_a}, '
        result += f'b = {self.koef_b}, '
        result += f'c = {self.koef_c}'
        return result
