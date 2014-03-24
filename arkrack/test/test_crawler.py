import unittest
import os
import urllib
from urllib import response
from unittest import mock
import io

from arkrack import crawler


_RESULT_GOOGLE = (
    '<html><body>'
    '<a href="/url?q=http://link1.com&xxx=yyy">link1</a>'
    '<a href="/url?q=http://link2.com&xxx=yyy">link2</a>'
    '</body></html>')

_RESULT_1 = '<html><body><p>pas1</p></body></html>'
_RESULT_2 = '<html><body><p>pas2</p></body></html>'


class TestCrawler(unittest.TestCase):

  def setUp(self):
    self._crawler = crawler.Crawler('basename.zip')

  def _get_mock_response(self, content):
     return response.addinfourl(
         io.BytesIO(content.encode('utf-8')),
         {'content-encoding': 'utf-8'},
         '',
         200)

  @mock.patch.object(urllib.request, 'urlopen')
  def test_crawl_no_result(self, mock_urlopen):
    mock_urlopen.return_value = self._get_mock_response('')

    self.assertEqual([], list(self._crawler.crawl()))

  @mock.patch.object(urllib.request, 'urlopen')
  def test_urlopen_error(self, mock_urlopen):
    mock_urlopen.side_effect = urllib.error.URLError('Some error')

    self.assertEqual([], list(self._crawler.crawl()))

  @mock.patch.object(urllib.request, 'urlopen')
  def test_crawl_has_results(self, mock_urlopen):
    mock_urlopen.side_effect = (
        self._get_mock_response(_RESULT_GOOGLE),
        self._get_mock_response(_RESULT_1),
        self._get_mock_response(_RESULT_2))

    pwds = list(self._crawler.crawl())
    self.assertEqual(3, mock_urlopen.call_count)
    self.assertEqual(['pas1', 'pas2'], pwds)


if __name__ == "__main__":
  unittest.main()
