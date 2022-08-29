from Deeproad import db

class car_plate(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    plate = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.String(20), nullable=False)
