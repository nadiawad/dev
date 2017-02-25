import logging
from unittest import TestCase
from testfixtures import log_capture

@log_capture()
def test_function(l):
    logger = logging.getLogger()
    logger.info('a message')
    logger.error('an error')

    l.check(
        ('root', 'INFO', 'a message'),
        ('root', 'ERROR', 'an error'),
        )


class TestJob_function(TestCase):
    def test_job_function(self):
        self.fail()

