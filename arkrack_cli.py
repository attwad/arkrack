import sys
import os
import logging
import argparse

from arkrack.crackers import cracker_factory
from arkrack import crawler

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description=('Crawls the internet and tries crawled words as passwords '
                   'for a protected archive.'))
  parser.add_argument('file', metavar='FILE')
  parser.add_argument('--logfile', default='crack.log', help=(
      'Verbose logfile name, override with empty for no log file.'))
  args = parser.parse_args()

  if args.logfile:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M:%S',
        filename=args.logfile,
        filemode='w')
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  logging.getLogger('').addHandler(console)

  cracker = cracker_factory.CrackerFactory().get_cracker(args.file)

  basename = os.path.basename(args.file)

  if not cracker:
    logging.fatal('Could not find any suitable cracker for this file.')
    sys.exit(-1)
  crawl = crawler.Crawler(basename)
  logging.info('Starting crawl&crack...')
  for pwd in crawl.crawl():
    if cracker.can_crack(pwd):
      logging.info('Found password: {}'.format(pwd))
      break
  else:
    logging.info('Could not find password :(')
