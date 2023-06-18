import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-13617-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "3216540":
        {
            "name": "Shreyansh Shukla",
            "major": "CS",
            "starting_year": 2021,
            "total_attendance":7,
            "standing": "F",
            "year": 3,
            "last_attendance_time": "2023-6-18 10:54:34"

        },
    "8527410":
        {
            "name": "Steve Wozniak",
            "major": "CS",
            "starting_year": 1980,
            "total_attendance":79,
            "standing": "O",
            "year": 40,
            "last_attendance_time": "1998-6-18 10:54:34"

        },
    "9638520":
        {
            "name": "Mark Zuckerberg",
            "major": "CS",
            "starting_year": 2003,
            "total_attendance":50,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2004-6-18 10:54:34"

        },
}
for key,value in  data.items():
    ref.child(key).set(value)