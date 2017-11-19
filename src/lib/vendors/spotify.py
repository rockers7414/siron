import logging


class Spotify(object):
    logger = logging.getLogger(__name__)

    def __init__(self, config):
        self.logger.info(config['client_id'])
        self.logger.info(config['client_secret'])
