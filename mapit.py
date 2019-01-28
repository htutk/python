#! python3
# mapit.py - Launches a map in the browser using an address from
# the command line or clipboard

# a few more commands to try: dir, search
# home and work are saved.

import webbrowser, pyperclip, sys
if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])

# otherwise, get it from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
