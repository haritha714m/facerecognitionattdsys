import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-86bfb-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "JANANI",
            "major": "Artificial Intelligence And Data Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "2":
        {
            "name": "HARITHA",
            "major": "Artificial Intelligence And Data Science",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "3":
        {
            "name": "DEEPIKA",
            "major": "Artificial Intelligence And Data Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "4":
        {
            "name": "JAYA",
            "major": "Artificial Intelligence And Data Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "5":
        {
            "name": "DAYANA",
            "major": "Artificial Intelligence And Data Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)