#!/usr/bin/env python
import configparser
import logging
from lib.vendors.spotify import Spotify


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.cfg')

    logging.basicConfig(
        filename=config['LOGGING']['filename'],
        level=config['LOGGING']['level'],
        format="%(asctime)s | %(name)-16s | %(levelname)s | %(message)s"
    )

    spotify = Spotify(config['SPOTIFY'])
