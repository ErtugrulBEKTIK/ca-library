from enum import Enum 

BookingStatus = Enum('BookingStatus', 'BORROWED RETURNED')

BookStatus = Enum('BookStatus', 'AVAILABLE BORROWED')

UserType = Enum('UserType', 'ADMIN EDITOR BASIC_USER')