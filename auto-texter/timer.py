from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from Auto_message import love_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(love_message, 'interval', hours=1)

sched.start()
