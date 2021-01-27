from singleton.example.logger import Logger
LOG_FILE = 'file.log'

# First setup.
Logger(LOG_FILE).info('Initial message.')

if __name__ == '__main__':
    other_log_file = 'other.log'

    logger = Logger(other_log_file)
    logger.info('Log file is the same.')

    with open(LOG_FILE) as log_file:
        log_len = len(log_file.readlines())

    assert log_len == 2
