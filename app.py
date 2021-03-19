from flask import request, jsonify, render_template
from  config import app, mysql
import pymysql

"""
Root endpoint.
It doesnt matter in the API design.
"""
@app.route('/')
def index():
    """
    This is the root endpoint.
    :return: The landing page 🛬 of the platform.
    """
    return render_template('index.html')

"""
Create operations
"""
@app.route('/user/add', methods=['POST'])
def addUser():
    """
    Create a new user
    """
    connection = None
    cursor = None
    try:
        username = request.args.get("username")
        firstname = request.args.get("firstname")
        lastname = request.args.get("lastname")
        password = request.args.get("password")

        # Validate the received values
        if request.method == 'POST':
            sql = "INSERT INTO Users(username, firstname, lastname, password) VALUES (%s, %s, %s, %s)"
            data = (username, firstname, lastname, password)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('User Added Successfully!!!')
            response.status_code = 200
            return response
        else:
            return 'Nothing has happened'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/room/add', methods=['POST'])
def addRoom():
    """
    Create a new room.
    :return:
    """
    connection = None
    cursor = None
    try:
        roomId = request.args.get("roomId")
        floor = request.args.get("capacity")
        capacity = request.args.get("floor")

        if request.method == 'POST':
            sql = "insert into Rooms(room_id,floor, capacity) values (%s,%s, %s)"
            data = (roomId, floor, capacity)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('Room created.')
            response.status_code = 200
            return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/booking/add', methods=['POST'])
def addBooking():
    """
    Create a new room booking
    :return:
    """
    connection = None
    cursor = None
    try:
        username = request.args.get("username")
        roomId = request.args.get("roomId")
        bookingDay = request.args.get("bookingDay")
        startTime = request.args.get("startTime")
        endTime = request.args.get("endTime")
        bookedFor = request.args.get("bookedFor")
        meetingStatus = request.args.get("meetingStatus")

        if request.method == 'POST':
            sql = "insert into " \
                  "RoomBookings(username, room_id, booking_day, start_time, end_time, booked_for, meeting_status) values (%s,%s, %s, %s)"
            data = (username, roomId, bookingDay, startTime, endTime, bookedFor, meetingStatus)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('Room Booked')
            response.status_code = 200
            return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

"""
Read operations.
"""

@app.route('/rooms', methods=['GET'])
def rooms():
    """
    Retrieve details of all rooms.
    :return: JSON object.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("select * from Rooms")
        if resultValue > 0:
            rows = cursor.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/rooms/<int:roomId>', methods=['GET'])
def getRoom(roomId):
    """
    Retrieve all details of a given room.
    :param roomId: Room id.
    :return: details about the room.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Rooms WHERE room_id=%s", str(roomId))
        row = cursor.fetchone()
        response = jsonify(row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/bookings', methods=['GET'])
def bookings():
    """
    Retrieve details of all bookings
    :return: JSON object
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from RoomBookings")
        rows = cursor.fetchall()
        response = jsonify(str(rows))
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/room/bookings/<int:roomId>', methods=['GET'])
def getBookingsMadeOnARoom(roomId):
    """
    Retrieve booking details made on a given room.
    :param roomId: obvious too.
    :return: JSON object💁
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM RoomBookings WHERE room_id=%s", str(roomId))
        row = cursor.fetchone()
        if row is None:
            return 'Room not found'
        response = jsonify(str(row))
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/users', methods=['GET'])
def users():
    """
    Retrieve all users.
    :return: JSON object💁
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("SELECT * FROM Users")
        if resultValue > 0:
            rows = cursor.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/user/<int:username>', methods=['GET'])
def getUser(username):
    """
    Retrieve details of a given user.
    :param username: 💁 Not Obvious???
    :return: JSON object💁
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Users WHERE username=%s", str(username))
        row = cursor.fetchone()
        if row is None:
            return 'User not found'
        response = jsonify(row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/user/bookings/<string:username>', methods=['GET'])
def getBookingsMadeByUser(username):
    """
    Retrieve all bookings made by a given user.
    :param username:
    :return: JSON object💁
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Room_bookings WHERE username=%s", username)
        row = cursor.fetchone()
        if row is None:
            return 'No bookings made by such user'
        response = jsonify(row)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

"""
Delete operations.
"""

@app.route('/users/delete/<string:username>', methods=['DELETE'])
def deleteUser(username):
    """
    Delete a given user by username
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Users WHERE username = %s", (username,))
        connection.commit()
        if resultValue > 0:
            response = jsonify('{username} deleted successfully!!!')
            response.status_code = 200
            return response
        else:
            return 'No such user exists...'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/rooms/delete/<string:roomId>', methods=['DELETE'])
def deleteRoom(roomId):
    """
    Delete a specific room by roomId
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Rooms WHERE room_number = %s", roomId)
        connection.commit()
        if resultValue > 0:
            response = jsonify('Room details of room {} deleted Successfully!!!'.format(roomId))
            response.status_code = 200
            return response
        else:
            return 'No such room exists...'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/bookings/delete/<string:username>', methods=['DELETE'])
def deleteBookings(username):
    """
    Delete all bookings made by a given user
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Room_bookings WHERE username = %s", username)
        connection.commit()
        if resultValue > 0:
            response = jsonify('All bookings made by {} Deleted Successfully!!!'.format(username))
            response.status_code = 200
            return response
        else:
            return 'No bookings made by such user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/bookings/delete <string:roomId>', methods=['DELETE'])
def deleteBooking(roomId):
    """
    Delete all bookings hosted in a specific room
    """
    cursor = None
    connection = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Room_bookings WHERE room_number = %s", roomId)
        connection.commit()
        if resultValue > 0:
            response = jsonify('All bookings in room {} deleted successfully!!!'.format(roomId))
            response.status_code = 200
            return response
        else:
            return 'No bookings made in that room'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

"""
Run app.
"""
if __name__ == '__main__':

    app.run(threaded=True, port=5000)