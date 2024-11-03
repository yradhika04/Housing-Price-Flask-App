from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import joblib
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)


def return_prediction(model, input_json):

    input_data = pd.DataFrame([[input_json[k] for k in input_json.keys()]], columns=["area", "bedrooms", "bathrooms", "parking"])
    prediction = model.predict(input_data)[0]

    return prediction


model = joblib.load('decision_tree.joblib')


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    parking = db.Column(db.Integer, nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        parking = float(request.form['parking'])
        prediction = return_prediction(model, {"area": area, "bedrooms": bedrooms,
                                               "bathrooms": bathrooms, "parking": parking})
        new_task = Price(area=area, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking, prediction=prediction)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your prediction"

    else:
        tasks = Price.query.order_by(Price.date_created).all()
        return render_template("home.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Price.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting your prediction"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Price.query.get_or_404(id)
    if request.method == "POST":
        task_to_update.area = float(request.form['area'])
        task_to_update.bedrooms = float(request.form['bedrooms'])
        task_to_update.bathrooms = float(request.form['bathrooms'])
        task_to_update.parking = float(request.form['parking'])
        task_to_update.prediction = return_prediction(model, {"area": task_to_update.area, "bedrooms": task_to_update.bedrooms,
                                                              "bathrooms": task_to_update.bathrooms, "parking": task_to_update.parking})
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating that task"
    else:
        return render_template("update.html", task=task_to_update)


if __name__ == "__main__":
    app.run(debug=True)
