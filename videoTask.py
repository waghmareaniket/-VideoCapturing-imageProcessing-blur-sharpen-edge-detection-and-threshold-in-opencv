import cv2
import os

def record_video(filename='recorded_video.avi'):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam.")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

    print("Recording... Press 'q' to stop.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame.")
            break
        out.write(frame)
        cv2.imshow("Recording - Press 'q' to stop", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped.")
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def play_video(filename='recorded_video.avi'):
    if not os.path.exists(filename):
        print("Video file does not exist.")
        return

    cap = cv2.VideoCapture(filename)
    print("Playing video. Press 'q' to quit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Playback - Press 'q' to quit", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def menu():
    while True:
        print("\n===== Video Capture Mini App =====")
        print("1. Record Video")
        print("2. Play Recorded Video")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            record_video()
        elif choice == '2':
            play_video()
        elif choice == '3':
            print("Exiting app.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    menu()
