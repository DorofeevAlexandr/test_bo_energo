from webapp.db import db


class ColoredOjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=True)
    obj_color = db.Column(db.String, nullable=True)
    selected = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        result = f'id = {self.id}, '
        result += f'number = {self.number}, '
        result += f'obj_color = {self.obj_color}, '
        result += f'selected = {self.selected}'
        return result


class ProbabilityColoredObjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_samples = db.Column(db.Integer, nullable=False)
    number_blue_samples = db.Column(db.Integer, nullable=False)
    number_green_samples = db.Column(db.Integer, nullable=False)
    number_red_samples = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        result = f'number_samples = {self.number_samples}, '
        result += f'number_blue_samples = {self.number_blue_samples}, '
        result += f'number_green_samples = {self.number_green_samples}, '
        result += f'number_red_samples = {self.number_red_samples}'
        return result
