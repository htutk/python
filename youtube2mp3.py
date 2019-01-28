#! python3

"""
youtube2mp3.py -- converts a given youtube link to mp3 file
and downloads it (via ytmp3.cc)

To use youtube-mp3.py,
Enter youtube-mp3 <full Youtube link>

"""

import sys, time, requests, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# returns: 1 for successful download
#          0 if an error occurs
def youtube2mp3_converter(ytLink):
    if not ytLink.startswith('http'):
        print('Please enter a valid link...')
        return 0

    print()
    print('Converting the link to mp3...')
    browser = webdriver.Firefox()
    browser.get('https://ytmp3.cc')
    idElem = browser.find_element_by_id('input')
    idElem.send_keys(ytLink)
    idElem.send_keys(Keys.ENTER)


    print('Initializing...')
    # check if the link is valid
    try:
        downloadElem = browser.find_element_by_id('download')
        downloadLink = downloadElem.get_attribute('href')
    except:
        print()
        browser.close()
        print('Please enter a valid link...')
        return 0

    while not downloadLink:
        time.sleep(2)
        downloadElem = browser.find_element_by_id('download')
        downloadLink = downloadElem.get_attribute('href')

    title = browser.find_element_by_id('title')
    title = title.text
    print('Downloading...')
    res = requests.get(downloadElem.get_attribute('href'))
    browser.close()
    try:
        res.raise_for_status()
    except:
        print('Network error!...')
        return 0

    # all download files should go to C:\\Users\\Alex Htut\\downloads
    os.chdir('C:\\Users\\Alex Htut\\Downloads')
    # output file by user
    print()
    title = title + '.mp3'

    while True:
        try:
            mp3Output = open(title, 'wb')
            break
        except:
            print(title)
            print('The given title has naming issues...')
            print('Please include .mp3 extension..')
            print('Enter a title name: ', end='')
            title = input()

    print(title + ' is now added to Downloads folder!')
    for chunk in res.iter_content(100000):
        discard = mp3Output.write(chunk)

    mp3Output.close()
    return 1

###############################################################################

if len(sys.argv) < 2:
    print("""
    To use youtube-mp3.py,
    Enter youtube-mp3 <full Youtube link>

    """)
else:
    ytLinks = sys.argv[1:]
    linkResults = []
    for ytLink in ytLinks:
        youtube2mp3_converter(ytLink)
