from crontab import CronTab

cron = CronTab(user='root')

job = cron.new(command='python3 /home/asterisk/ipodata/smdrproxy.py')

job.minute.every(10)

job1 = cron.new(command='python3 /home/asterisk/ipodata/smdrproxy.py')

job1.every_reboot()

cron.write()

print(cron)