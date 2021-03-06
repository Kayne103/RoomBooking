from flask import request, jsonify
from  config import app, mysql
import pymysql
import markdown
import markdown.extensions.fenced_code
from users import auth

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
    return jsonify("Welcome to Cookie Session Room Booking API!!")

"""
Specifies all the endpoints and how to send requests.
"""
@app.route('/guide')
def guide():
    """
    Renders GUIDE.md as an html file.
    """
    guide_md = open("GUIDE.md", "r")
    md_template_string = markdown.markdown(
        guide_md.read(), extensions=["fenced_code"]
    )
    return md_template_string
"""
Create operations
"""
@app.route('/user/add', methods=['POST'])
@auth.login_required()
@auth.login_required()
def addUser():
    """
    Create a new user
    """
    connection = None
    cursor = None
    try:
        userId = request.args.get("userId")
        firstname = request.args.get("firstname")
        lastname = request.args.get("lastname")
        password = request.args.get("password")

        # Validate the received values
        if request.method == 'POST':
            sql = "INSERT INTO Users(userId, firstname, lastname, password) VALUES (%s, %s, %s, %s)"
            data = (userId, firstname, lastname, password)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('User Added Successfully!!!')
            response.status_code = 200
            return response
        return 'Nothing has happened'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/room/add', methods=['POST'])
@auth.login_required()
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
            sql = "insert into Rooms(roomId,floor, capacity) values (%s,%s, %s)"
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
@auth.login_required()
def addBooking():
    """
    Create a new room booking
    :return:
    """
    connection = None
    cursor = None
    try:
        userId = request.args.get("userId")
        roomId = request.args.get("roomId")

        if request.method == 'POST':
            sql = "insert into " \
                  "RoomBookings(userId, roomId) values (%s,%s)"
            data = (userId, roomId)
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
def getAllRooms():
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
@auth.login_required()
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
        cursor.execute("SELECT * FROM Rooms WHERE roomId=%s", roomId)
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
@auth.login_required()
def getAllBookings():
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
@auth.login_required()
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
        cursor.execute("SELECT * FROM RoomBookings WHERE roomId=%s", roomId)
        row = cursor.fetchall()
        if row is None:
            return 'Room not found'
        response = jsonify(row)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/users', methods=['GET'])
@auth.login_required()
def getAllUsers():
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

@app.route('/user/<int:userId>', methods=['GET'])
@auth.login_required()
def getUser(userId):
    """
    Retrieve details of a given user.
    :param userId: 💁 Not Obvious???
    :return: JSON object💁
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Users WHERE userId=%s", userId)
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

"""
Update operations.
"""
@app.route('/user/update/<int:userId>', methods=['UPDATE', 'PUT'])
@auth.login_required()
def updateUserPassword(userId):
    """
    Update user password.
    :return:
    """
    connection = None
    cursor = None
    try:
        password = request.args.get("password")
        if password and request.method == 'POST':
            sql = "UPDATE Users SET password=%s WHERE userId=%s"
            data = (userId, password)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('Password updated successfully!')
            response.status_code = 200
            return response
        return None
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/room/update/<int:roomId>', methods=['UPDATE', 'PUT'])
@auth.login_required()
def updateRoomCapacity(roomId):
    """
    Update room capacity.
    :return:
    """
    connection = None
    cursor = None
    try:
        capacity = request.args.get("password")
        if capacity and request.method == 'POST':
            sql = "UPDATE Rooms SET capactiy=%s WHERE roomId=%s"
            data = (roomId, capacity)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('Room updated successfully!')
            response.status_code = 200
            return response
        return None
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/booking/update/<int:bookingId>', methods=['UPDATE', 'PUT'])
@auth.login_required()
def updateBookingRoomNumber(bookingId):
    """
    Change room number.
    :return:
    """
    connection = None
    cursor = None
    try:
        roomId = request.args.get("roomId")
        if roomId and request.method == 'POST':
            sql = "UPDATE RoomBookings SET roomId=%s WHERE bookingId=%s"
            data = (bookingId, roomId)
            connection = mysql.connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            connection.commit()
            response = jsonify('Booking updated successfully!')
            response.status_code = 200
            return response
        return None
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

"""
Delete operations.
"""
@app.route('/users/delete/<int:userId>', methods=['DELETE'])
@auth.login_required()
def deleteUser(userId):
    """
    Delete a given user
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Users WHERE userId = %s", (userId,))
        connection.commit()
        if resultValue > 0:
            response = jsonify('deleted successfully!!!')
            response.status_code = 200
            return response
        return 'No such user exists...'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/rooms/delete/<int:roomId>', methods=['DELETE'])
@auth.login_required()
def deleteRoom(roomId):
    """
    Delete a specific room by roomId
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM Rooms WHERE roomId = %s", roomId)
        connection.commit()
        if resultValue > 0:
            response = jsonify('Room deleted Successfully!!!'.format(roomId))
            response.status_code = 200
            return response
        return 'No such room exists...'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/bookings/delete/<int:bookingId>', methods=['DELETE'])
@auth.login_required()
def deleteBooking(bookingId):
    """
    Delete all bookings made by a given user
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        resultValue = cursor.execute("DELETE FROM RoomBookings WHERE bookingId = %s", bookingId)
        connection.commit()
        if resultValue > 0:
            response = jsonify('Booking deleted Successfully!!!'.format(bookingId))
            response.status_code = 200
            return response
        return 'No such booking'
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