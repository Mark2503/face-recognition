# from discovery_face_video import start_stream
# from face_recognition_during_live_webcam_broadcast import start_stream
from discovery_face_video import start_stream


def main():

   start_stream('rtsp://admin:192168102Abc@192.168.3.253:554/ISAPI/Streaming/Channels/4402')


if __name__ == '__main__':
    main()

