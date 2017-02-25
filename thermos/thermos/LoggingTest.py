from testfixtures import log_capture
import logging
from Scheduler import job_function
import datetime


@log_capture()
def test_function(l):
    logger = logging.getLogger(job_function())
    print "I am in the test func"
    l.check(
        ('root', 'INFO', 'a message'),
        ('root', 'ERROR', 'an error'),
        )


print "hi"
log_capture()
