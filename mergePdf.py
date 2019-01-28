#! python3
# mergePdf.py - merges PDF files together to make a single pdf

import PyPDF2, os, sys

if len(sys.argv) < 2:
    print("""
    To use mergePdf.py,
    Enter mergePdf <pdf1.pdf> <pdf2.pdf> ... <pdfn.pdf>.

    NOTES:
    1. Make sure to include .pdf extension.
    2. Merge the files in order given.
    """)
else:
    pdfList = sys.argv[1:]

    # check to see if .pdf extension are added
    for file in pdfList:
        if not file.endswith('.pdf'):
            sys.exit('Make sure to include .pdf extension...')

    print()
    print('Where are the files located?')
    print("Enter in the format of C:\\\\folder\\\\folder...")
    directory = input()

    while True:
        try:
            os.chdir(directory)
            break
        except:
            print('Please enter a valid directory... Enter \'q\' to exit...')
            directory = input()
            if directory.lower() == 'q':
                sys.exit()

    # check to see every file is in the directory given
    print()
    for file in pdfList:
        print('Checking...')
        if file not in os.listdir():
            sys.exit(file + ' cannot be found in ' + str(os.getcwd()))

    pdfWriter = PyPDF2.PdfFileWriter()

    # loop thru all the pdf files
    print('Initializing...')
    print()
    for file in pdfList:
        pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))

        # if the file is encrypted
        if pdfReader.isEncrypted:
            print('Oh O!, ' + file + ' is encrypted...')
            print('Do you happen to know the password? (Y/N): ', end='')
            knownPassword = input()

            while True:
                if knownPassword.upper() == 'Y':
                    print('Enter the password: ', end='')
                    password = input()

                    while not pdfReader.decrypt(password):
                        print('Sorry, the password is incorrect... '
                        + 'Enter \'q\' to exit...')
                        password = input()
                        if password.lower() == 'q':
                            sys.exit()
                    break
                elif knownPassword.upper() == 'N':
                    print('Sorry, the encrypted pdf requires a password...')
                    sys.exit()
                else:
                    print('Please enter Y/N: ', end='')
                    knownPassword = input()
        # get all pages
        for page in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(page))

        print()
        print(file + ' is now added...')
        print()

    # name the merged file
    print()
    print('How would you like to name the merged file? '
    + 'Please include .pdf extension: ')
    outputFileName = input()

    # check two things:
    # 1. ends with .pdf
    # 2. is valid filename
    while True:
        try:
            while not outputFileName.endswith('.pdf'):
                print('Please include .pdf extension...')
                outputFileName = input()

            pdfOutput = open(outputFileName, 'wb')
            break
        except:
            print('Please enter a valid file name...')
            outputFileName = input()

    print()
    print('Done....!')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
