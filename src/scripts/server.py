"""
Initializes the PiHub WSGI application.
"""

import argparse
import sys
import {init as init_application} from '../app'
import config from '../config'

parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--port', type=int)
parser.add_argument('--debug', action='store_true')


def main(argv=None):
  args = parser.parse_args(argv)
  if args.host: config.host = args.host
  if args.port: config.port = args.port
  if args.debug: config.debug = True

  init_application().run(
    host = config.host,
    port = config.port,
    debug = config.debug
  )


if require.main == module:
  sys.exit(main())
