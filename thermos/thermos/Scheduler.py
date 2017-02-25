# http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import logging


def job_function():
    logger = logging.getLogger('Scheduler')
    hdlr = logging.FileHandler('/Users/Nadi/dev/thermos/Scheduler.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    logger.info('Checking details now....') #20 for info
    print "The scheduled job is running now..."


def schedule(cronHour, cronMinute):
    sched = BlockingScheduler()
    sched.add_job(job_function, 'cron', day_of_week ='Mon-Sun', hour=cronHour, minute=cronMinute)
    sched.start()


#schedule(23, 35)