from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

mysql = MySQL(app)

CORS(app, resources={r'/*': {"origins": "*"}})

@app.route('/appointments', methods=['GET'])
def getAppointments():
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = 'SELECT id, rut, name, email, date, created_at FROM appointment'
        cursor.execute(sql)
        data = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print(data)
        if data != ():
            rest = []
            for element in data:
                rest_element = {'created_at': element[5], 'date': element[4],
                                'email': element[3], 'name': element[2], 'rut': element[1], 'id': element[0]}
                rest.append(rest_element)
            return jsonify({'appointments': rest, 'message': 'successful request'})

        else:
            return jsonify({'message': 'there is no appointments'})

    except Exception as ex:
        return jsonify({'message': 'Error getting appointments'})


@app.route('/appointments/<rut>', methods=['GET'])
def getAppointmentByRut(rut):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = 'SELECT id, rut, name, email, date, created_at FROM appointment WHERE rut = "{0}"'.format(
            rut)
        cursor.execute(sql)
        data = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        if data != ():
            rest = []
            for element in data:
                rest_element = {'created_at': element[5], 'date': element[4],
                                'email': element[3], 'name': element[2], 'rut': element[1], 'id': element[0]}
                rest.append(rest_element)

            return jsonify({'appointment': rest, 'message': 'successful request'})

        else:
            return jsonify({'message': 'there is no appointment'})

    except Exception as ex:
        return jsonify({'message': 'error getting the appointments'})


@app.route('/not-available-hours/<date>', methods=['GET'])
def getNotAvailableHours(date):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = "SELECT convert(time(date),char) FROM appointment WHERE date(appointment.date) = '{0}'".format(
            date)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        mysql.connection.commit()
        cursor.close()
        rest = []
        for element in data:
            rest.append(element[0])

        return jsonify({'not_available_hours': rest, 'message': 'successful request'})

    except Exception as ex:

        return jsonify({'message': 'error getting available hours'})


@app.route('/schedule', methods=['POST'])
def postAppointment():
    print(request.json['date'])
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = '''INSERT INTO appointment(rut, name, email, date, created_at) 
                    VALUES ('{0}','{1}','{2}','{3}',now())'''.format(request.json['rut'], request.json['name'], request.json['email'], request.json['date'])
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'successfully scheduled appointment'})

    except Exception as ex:
        return jsonify({'message': 'error posting appointment'})
        # This exception can be caused because of rut, email and/or date already does exist in the table, whitch means,
        # the person is trying to take a second appointnment or the date that wanted is already taken.


@app.route('/change-appointment', methods=['PUT'])
def updateAppointment():
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = "UPDATE appointment SET appointment.date = '{0}' WHERE rut = '{1}'".format(
            request.json['date'], request.json['rut'])
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'successfully re-scheduled appointment'})

    except Exception as ex:
        return jsonify({'message': 'error updating appointment'})
        # This error can be caused because of the rut even doesn't exist, whitch means the person don't even have an appointment,
        # or the date is already taken.


@app.route('/cancel-appointment/<rut>', methods=['DELETE'])
def deleteAppointment(rut):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('ExpiredAppointments', args=())
        sql = "DELETE FROM appointment WHERE rut = '{0}'".format(
            rut)
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'successfully canceled appointment'})

    except Exception as ex:
        return jsonify({'message': 'error deleting date'})


if __name__ == '__main__':
    app.run()