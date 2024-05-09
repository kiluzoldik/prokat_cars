from flask import Flask, render_template, request, flash, get_flashed_messages, url_for, redirect
from src.orm import create_tables, insert_persons, insert_orders
import datetime
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('/index.html')


@app.route('/modal', methods=["POST"])
def add_db():
    if request.method == "POST":
        fio = request.form['full_name']
        email = request.form['email_person']
        phone = request.form['phone_number']
        # passport1 = request.form['passport1']
        # passport2 = request.form['passport2']
        # drive1 = request.form['driverLicense1']
        # drive2 = request.form['driverLicense2']
        mark = request.form['mark']
        model = request.form['model']
        place_in = request.form['place_in']
        place_out = request.form['place_out']
        date_in = datetime.datetime.strptime(
            request.form['date_in'], '%Y-%m-%d')
        date_out = datetime.datetime.strptime(
            request.form['date_out'], '%Y-%m-%d')
        comments = request.form['comments']
        insert_persons(fio, email, phone)
        insert_orders(mark, model,
                      place_in,
                      place_out,
                      date_in,
                      date_out,
                      comments,
                      )
    else:
        print('error')
    return redirect(url_for('index'))


@app.route('/cars.html')
def cars():
    return render_template('/cars.html')


@app.route('/about_car_golf_r.html')
def about_golf_r():
    return render_template('/about_car.html', mark='Vagen', model='golf r-line', price='50$', money='5000 rub', places='5 мест', hp='250',
                           first_photo='/static/images/golf_r_first.jpg', second_photo='/static/images/golf_r_second.jpg', third_photo='/static/images/golf_r_third.jpg')


@app.route('/about_car_passat_cc.html')
def about_passat_cc():
    return render_template('/about_car.html', mark='Vagen', model='Passat CC', price='30$', money='5000 rub', places='5 мест', hp='165',
                           first_photo='/static/images/pasat_first.jpg', second_photo='/static/images/pasat_second.jpg', third_photo='/static/images/pasat_third.jpeg')


@app.route('/about_company.html')
def about_company():
    return render_template('/about_company.html')


@app.route('/contacts.html')
def contacts():
    return render_template('/contacts.html')


if __name__ == '__main__':
    # create_tables()
    app.run(debug=True)
