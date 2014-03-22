import abc


class Cracker(metaclass=abc.ABCMeta):
  """A class that can test a password on a file and tell if it's correct."""

  @abc.abstractmethod
  def can_crack(self, pwd):
    """Tries to open a file with the given password.

    Returns:
      True on success, False otherwise.
    """
