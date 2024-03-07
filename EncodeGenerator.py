import cv2
import face_recognition
import pickle
import os
from firebase_admin import  storage
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-86bfb-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-86bfb.appspot.com"
})


# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    #encodeList = []
    #for img in imagesList:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #encode = face_recognition.face_encodings(img)[0]
        #encodeList.append(encode)

    #return encodeList
    encodeList = []
    for img in imagesList:
        # Find all face locations in the image
        face_locations = face_recognition.face_locations(img)
        #if len(face_locations) == 0:
            # No faces found in the image
            #print("No faces found in the image.")
            #continue
        # If faces are found, encode the first one
        #encode = face_recognition.face_encodings(img, face_locations)[0]
        encode = face_recognition.face_encodings(img)
        encodeList.append(encode)
    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")