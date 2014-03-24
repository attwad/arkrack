import logging
import re
import urllib
import urllib.request

import bs4

class Crawler(object):
  """Very basic web crawler, don't expect fancy things happening here."""

  def __init__(self, archive_name):
    """Initializes the web crawler with the given archive name as origin.

    Args:
      archive_name: The original archive name to use as a crawl search seed.
    """
    self._origin = archive_name
    self._logger = logging.getLogger(__name__)
    self._google_link_pattern = re.compile(r'^/url\?q=(.*?)&')
    self._words = set()

  def crawl(self):
    self._logger.debug('Started crawling')

    for link in self._get_google_search_results():
      url = self._fetch_url(link)
      soup = bs4.BeautifulSoup(url.read())
      for words in soup.stripped_strings:
        for word in words.split(' '):
          if word not in self._words:
            self._words.add(word)
            yield word

  def _fetch_url(self, url):
    self._logger.debug('Fetching {}'.format(url))
    request = urllib.request.Request(
        url.format(self._origin),
        headers={
            "User-Agent": ("Mozilla/5.0 (X11; U; Linux i686) "
                           "Gecko/20071127 Firefox/2.0.0.11"),
        })
    try: 
      return urllib.request.urlopen(request)
    except urllib.error.URLError as urle:
      self._logger.debug('Error opening URL: %s', urle)

  def _get_google_search_results(self):
    self._logger.debug('Fetching results page from google.com...')
    url = self._fetch_url(
        'https://www.google.com/search?q="{}&safe=off"'.format(self._origin))
    if not url:
      return []
    links = self._get_links_from_page(
        url.read(), pattern=self._google_link_pattern)
    return [urllib.parse.unquote(link) for link in links]

  def _get_links_from_page(self, raw, pattern=None):
    soup = bs4.BeautifulSoup(raw)
    links = [
        link.attrs['href'] for link in (
            soup.find_all('a', attrs={'href': pattern or True}))]
    if pattern:
      links = [pattern.search(link).group(1) for link in links]
    self._logger.debug('Found {} links'.format(len(links)))
    return links
