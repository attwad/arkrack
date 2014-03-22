import zipfile
import logging

from crackers import cracker

class ZipCracker(cracker.Cracker):

  def __init__(self, filename):
    """Initialize the zip cracker with the archive filename to crack.

    Args:
      filename: The zip filename.
    """
    self._zip = zipfile.ZipFile(filename)
    files = self._zip.filelist
    self._file_in_archive= files[0].filename
    self._logger = logging.getLogger(__name__)

  def can_crack(self, pwd):
    # Logging has some problems with unicode strings it seems, convert to bytes
    # as that's what we'll use for password anyway.
    bytes_pwd = bytes(pwd, 'utf-8')
    try:
      self._logger.debug(
          'Trying to open {0} with {1}'.format(self._file_in_archive, bytes_pwd))
    except UnicodeEncodeError as uee:
      self._logger.error('Cannot display unicode for pwd: {}'.format(uee))
    try:
      with self._zip.open(self._file_in_archive, pwd=bytes_pwd):
        return True
    except RuntimeError as re:
      return False
