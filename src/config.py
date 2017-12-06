"""
Loads and exports the PiHub configuratation.
"""

import os

filename = os.getenv('PIHUB_CONFIG', 'pihub.config.py')
config = require(os.path.abspath(filename))

config.setdefault = vars(config).setdefault
config.setdefault('components', [])
config.setdefault('react_routes', [])

module.exports = config