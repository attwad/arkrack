=======
Arkrack
=======

Give Arkrack an encrypted archive and it will try to crack it with words taken
from pages that came up while searching for this archive file name on the
internet.

Simple, but effective.
(Alright, sometimes too simple so not that effective let's admit it...)

.. code-block:: bash

  $ python arkrack_cli.py --log=test.log arkrack/test/crackers/testdata/testzip.zip
  Starting crawl&crack...
  Found password: recognised

Yes you'll see that the zip passwords using zipcrypto are just so broken that
a zip encrypted with the password "password" can be opened with "recognized",
".minecraft" or even better: "A"... yes really... So it's even a bit fun to run arkrack
to find out new possible passwords ;-)

You can also have a look at the log file to check which passwords were tried:

.. code-block::

  ...
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'also'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'works'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'with'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'/vsizip/vsicurl//file.zip'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b','
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'but'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'server'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'supports'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'download'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'parts.'
  03-31 18:24:58 arkrack.crackers.zip_cracker DEBUG    Trying to open test.txt with b'example'
  ...
