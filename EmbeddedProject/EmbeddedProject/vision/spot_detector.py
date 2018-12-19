import glob
import os
import cv2
import numpy as np
from EmbeddedProject.managers.configmanager import ConfigManager


class SpotDetector:
    # define the list of boundaries
    boundaries = ([46, 5, 5], [255, 50, 80])


    def __init__(self, config):
        self.config = config

    def detect_spot(self):
        list_of_files = glob.glob(self.config["img_folder"] + '/*.jpg')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)

        image = cv2.imread(latest_file)
        image = cv2.resize(image, (300, 300))

        (lower, upper)  = self.boundaries
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        (thresh, output) = cv2.threshold(output, 10, 255, cv2.THRESH_BINARY_INV)

        params = cv2.SimpleBlobDetector_Params()
        # Change thresholds
        params.minThreshold = 0;
        params.maxThreshold = 256;

        # Filter by Area.
        params.filterByArea = True
        params.minArea = 20

        # Filter by Circularity
        params.filterByCircularity = False
        params.minCircularity = 0.1

        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0.05

        # Filter by Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.1

        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(output)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
        # the size of the circle corresponds to the size of blob
        if self.config["debug"] is True:
            im_with_keypoints = cv2.drawKeypoints(output, keypoints, np.array([]), (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            # Show blobs
            cv2.imshow(latest_file, im_with_keypoints)
            cv2.waitKey(0)

        if len(keypoints) > 0:
            return True

        return False


if __name__ == "__main__":
    config = ConfigManager.read_config("../embeddedproject.json")
    detector = SpotDetector(config["vision"])