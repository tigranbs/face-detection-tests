import cv2
from pytube import YouTube
from rembg import remove
import face_recognition

(YouTube('https://www.youtube.com/watch?v=kl8Pd-k1yxE').streams
 .filter(file_extension='mp4')
 .order_by('resolution').desc()
 .first()
 .download(output_path=".", filename="video.mp4"))


vidcap = cv2.VideoCapture('video.mp4')


def face_encoding(img):
    face_enc = face_recognition.face_encodings(img)
    if len(face_enc) == 0:
        return None
    return face_enc[0]


if __name__ == "__main__":
    faces = []
    frame_index = 0
    while True:
        success, image = vidcap.read()
        frame_index += 1
        if not success:
            break
        if frame_index % 30 != 0:
            continue

        face_encodings = face_encoding(image)
        if face_encodings is not None:
            found_same = False
            for face in faces:
                is_same = face_recognition.compare_faces([face['encoding']], face_encodings)[0]
                if is_same:
                    face['counter'] += 1
                    found_same = True
                    break
            if not found_same:
                faces.append({
                    "frame": image,
                    "encoding": face_encodings,
                    "counter": 1
                })
                print("New face found as frame", frame_index)

    print("Total faces found", len(faces))
    print("Saving PNG Frames...")
    count = 0
    for face in faces:
        if face['counter'] > 10:
            face_frame = remove(face['frame'])
            cv2.imwrite("frame%d.png" % count, face_frame)
            count += 1
    print("Done!")

