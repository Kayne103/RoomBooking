# Room Booking Database
_We assume that you have mysql server install and running in your computer.
If not, check out: [How to install MySql Server](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)_

**NB: You'll need to log into the MySql Shell to perform the following.**
### Create User
* Create a user.
    >create user 'cookie'@'localhost' identified by 'password';
  > 
* Grant user privileges.
    > grant all privileges on * . * to  'cookie'@'localhost';
### Create Database
* Create database called "roombooking"
    > create database roombooking
  
    Select database to use it.
    > use roombooking;
### Create Tables
* Execute the following commands following the order to create tables.
    >create table if not exists SystemAdmin(
        username varchar(15) not null,
        password varchar(45) not null
    );

    >create table if not exists Users(
        userId varchar(15),
        firstname varchar(15) not null,
        lastname varchar(15) not null,
        password varchar(45) not null,
        primary key (username)
    );

    >create table if not exists Rooms(
        roomId varchar(8) ,
        floor int not null check ( floor >= 0 ),
        capacity int not null check ( capacity > 0 ),
        primary key (roomId)
    );

    >create table if not exists RoomBookings(
       bookingId int auto_increment,
       userId varchar(15),
       roomId varchar(8),
       primary key (bookingId),
       foreign key (userId) references Users(userId) on delete cascade,
       foreign key (roomId) references Rooms(roomId) on delete cascade
    );

    >create table if not exists RoomBookingDetails(
       bookingId int not null ,
       bookingDay date not null,
       startTime time not null ,
       endTime time not null ,
       bookedFor varchar(45) not null,
       meetingStatus varchar(10) not null,
       foreign key (bookingId) references RoomBookings(bookingId) on delete cascade
    );
