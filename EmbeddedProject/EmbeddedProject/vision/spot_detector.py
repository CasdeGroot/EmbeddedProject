import cv2
import glob
import os


class SpotDetector():
    def __init__(self, img_folder_path):
        self.img_folder_path = img_folder_path

    def detect_spot(self):
        list_of_files = glob.glob(self.img_folder_path + '/*.py')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)


if __name__ == "__main__":
    detector = SpotDetector("../../EmbeddedProject/drivers")
    detector.detect_spot()