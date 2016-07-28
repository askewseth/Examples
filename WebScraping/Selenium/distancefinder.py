"""Python module for finding the driving time between two locations."""

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def find_driving_time(start_location, end_location):
    """Find the driving time between two locations using mapqust."""
    driver = webdriver.Firefox()
    driver.get("https://www.mapquest.com/directions")
    start_box = driver.find_element_by_id("input-directions-0")
    end_box = driver.find_element_by_id("input-directions-1")
    submit_button = driver.find_element_by_class_name("get-directions")
    start_box.send_keys(start_location)
    end_box.send_keys(end_location)
    # end_box.send_keys(Keys.RETURN)
    # end_box.submit()
    time.sleep(3)
    submit_button.click()
    submit_button.click()

    time.sleep(3)
    time_ = driver.find_element_by_class_name("time").text
    distance = driver.find_element_by_class_name("distance").text
    print time_, distance

def get_args():
    args = sys.argv
    if len(args) is 2:
        # Only one argument was given, assume starting at apartment
        return "750 Fulton Street, Greensboro NC", args[1]
    elif len(args) is 3:
        # Given start and end
        return args[1:]
    else:
        # Given either 0 or more than 2 arguments
        raise Exception("Must give at least a ending location...")


def main():
    """Run main method."""
    start, end = get_args()
    print start, end
    find_driving_time("2022 Thad Carey Road, Oxford NC",
                      "750 Fulton Street, Greensboro NC")


if __name__ == "__main__":
    main()
