import logging
from micro_utilities.config import ConfigManager


def execute_main():
    test_config = ConfigManager.get_value('test-config')
    logging.info('Started: {}'.format(test_config))
