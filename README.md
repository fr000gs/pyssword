# pyssword
Python password manager based on tkinter and sha512 hash.
The majority of password generators available use an encryption to lock the database of password you keep with yourself. You are required to supply the database to the program for it to unlock the passwords. This one doesn't make a database. It adds up the 'master password', the username and the website name, and takes a sha512 hash and then truncates it to fit in the password field. It appends @A to the last to take care of password requirements. People can get their passwords remotely only by putting their username and 'master password'.

## Setting a Master Password
pyssword requires a master password for hash generation. It is set by default to 'foo' on line number 6. You are strongly recommended to change it.

## Copy to clipboard
pyssword has an option to copy the password to clipboard.

## Installing
Download the executable from the releases section.

OR

Run the file with python 3.

    python pyssword-0.2.py


