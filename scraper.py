import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
import time
import csv
import re

# tell Chrome to use the browser in incognito mode and ignore teh errors
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument('--ignore-certificate-errors')

# create an instance of our browser
browser = webdriver.Chrome(
    executable_path=r'C:\Users\greta\Documents\chromedriver.exe')


def koreancleanser():

    # tell Selenium to open Chrome and load this url; tell Python to wait for 2 seconds before going to the next task. This allows our browser to have the time it needs to fully load the page.
    url = "https://www.stylekorean.com/search/cleanser.html"
    browser.get(url)
    time.sleep(2)

    # Create list of URLs we need to open
    i = 2
    url_list = []

    # add the first URL to the list
    url_list.append(url)

    # Iterate in order to create URls
    while i < 4:

        url_to_add = "https://www.stylekorean.com/search/cleanser/page" + \
            str(i) + ".html"
        url_list.append(url_to_add)
        i += 1

    # Print the resulting list
    print(url_list)

    # Create blank frame - this is where we add the data we scrap
    listing_frame = pd.DataFrame(columns=["listing"])

    # First loop: we iterate over the different webpages we created previously
    for webpage in url_list:

        # We open the page
        browser.get(webpage)

        # On the webpage that is currently open, we create a list of all the listings
        listings = browser.find_elements_by_xpath(
            "//*[@class = 'sct sct_910']//*[@class='sct_li']")

        # Second loop: we iterate over the listings in order to find each listing's details
        for listing in listings:

            # Extract the text from each listing
            listing_data = listing.text

            # Create a dictionary
            listing_data = {"listing": listing_data}

            # Add dictionary to a dataframe
            frame = pd.DataFrame(listing_data, columns=["listing"], index=[0])

            # Append frame to main dataframe
            listing_frame = listing_frame.append(frame, ignore_index=True)

            # Wait time
            time.sleep(1)

            # Print frame (Work in progress)
            print(listing_frame)

        # Now that the second loop is closed, go over to the first loop and open the second URL
        # then launch the second loop over the second URL

    # Print final main frame
    print(listing_frame)

    # Our taks is exectued, we quit the browser
    browser.quit()


# excute the function
koreancleanser()
