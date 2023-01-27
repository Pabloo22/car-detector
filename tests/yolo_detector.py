# import cv2

from src.car_detectors import YoloDetector
# from src.data_structures import Frame
from src import Processor


def main():

    car_detector = YoloDetector()

    # # read image with numpy
    # image = cv2.imread("data/highway.jpg")
    # frame = Frame(image)
    #
    # # detect cars
    # cars = car_detector.detect(frame)
    #
    # # draw rectangles
    # frame.draw_rectangles(cars)
    #
    # # show image
    # frame.show()

    processor = Processor(car_detector)
    video = processor.process_video("data/video.avi")
    video.visualize()
    video.save("data/new_video_yolo.avi")


if __name__ == "__main__":
    main()
