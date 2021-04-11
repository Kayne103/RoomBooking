# How To Send Request
* We advise testers to use [Postman](https://www.postman.com/downloads/) for sending requests.
* All request should be sent in the format: "_URL:/Port/Endpoint {Payload, If any}_"
E.g.
  > http://127.0.0.1:5000/guide
  > 
    And the request method should be specified.

# Endpoints
1. Registering a new RBS user.
    * Method: POST
    * Endpoint: /user/add
    * Payload: userId, firstname, lastname, password
    >http://127.0.0.1:5000/user/add?userId=110&firstname=Thor&lastname=Odin&password=1234
    
2. Create a new Room.
    * Method: POST
    * Endpoint: /room/add
    * Payload: roomId, capacity, floor
    >http://127.0.0.1:5000/room/add?roomId=247021&capacity=15&floor=3
   
3. Book a room.
    * Method: POST
    * Endpoint: /booking/add
    * Payload: userId, roomId
    >http://127.0.0.1:5000/booking/add?userId=103&roomId=247011
   
4. Get a list of all rooms.
    * Method: GET
    * Endpoint: /rooms
    * Payload: None
    >http://127.0.0.1:5000/rooms
   
5. Get details of a single room.
    * Method: GET
    * Endpoint: /rooms/{roomId}
    * Payload: None
    >http://127.0.0.1:5000/rooms/247011
   
6. Get a list of all bookings
    * Method: GET
    * Endpoint: /bookings
    * Payload: None
    >http://127.0.0.1:5000/bookings
    
7. Get booking details made on a room.
    * Method: GET
    * Endpoint: /room/bookings/{roomId}
    * Payload: None
    >http://127.0.0.1:5000/room/bookings/247011
    
8. Get a list of all users.
    * Method: GET
    * Endpoint: /users
    * Payload: None
    >http://127.0.0.1:5000/users
    
9. Get details of single user.
    * Method: GET
    * Endpoint: /users/{userId}
    * Payload: None
    >http://127.0.0.1:5000/user/123
   
10. Update user password.
    * Method: UPDATE, PUT
    * Endpoint: /user/update/{userId}
    * Payload: password
    >http://127.0.0.1:5000/user/update/{userId}
   
11. Update room capacity.
    * Method: UPDATE, PUT
    * Endpoint: /room/update/{roomId}
    * Payload: capacity
    >http://127.0.0.1:5000/room/update/{roomId}
   
12. Change room number.
    * Method: UPDATE, PUT
    * Endpoint: /booking/update/{bookingId}
    * Payload: roomId
    >http://127.0.0.1:5000/booking/update/1
   
13. Delete a user.
    * Method: DELETE
    * Endpoint: /users/delete/{userId}
    * Payload: None
    >http://127.0.0.1:5000/users/delete/123
   
14. Delete a room.
    * Method: DELETE
    * Endpoint: /rooms/delete/{roomId}
    * Payload: None
    >http://127.0.0.1:5000/rooms/delete/123
   
15. Delete booking.
    * Method: DELETE
    * Endpoint: /booking/delete/{bookingId}
    * Payload: None
    >http://127.0.0.1:5000/booking/delete/1
   