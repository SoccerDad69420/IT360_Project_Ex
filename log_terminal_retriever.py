import os


def get_Syslog(self):
    print(os.system('sudo cat /var/log/syslog', shell=True))

get_Syslog()