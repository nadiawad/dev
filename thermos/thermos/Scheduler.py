# http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html

from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print "Hello World"

sched = BlockingScheduler()
sched.add_job(job_function, 'cron', day_of_week ='Mon-Sun', hour='20', minute='29')
sched.start()