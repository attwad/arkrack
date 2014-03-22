import logging

from crackers import zip_cracker

class CrackerFactory(object):

  def __init__(self):
    self._logger = logging.getLogger(__name__)

  def get_cracker(self, archive_name):
    if archive_name.endswith('zip'):
      self._logger.debug('Filename ends with zip, using ZipCracker')
      return zip_cracker.ZipCracker(archive_name)
