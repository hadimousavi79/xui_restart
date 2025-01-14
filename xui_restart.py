import time
import datetime
import os
import psutil  

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'restart_log.txt')

t1 = datetime.datetime.now()

while(True):
    time.sleep(10)
    p_mem = psutil.virtual_memory().percent
    p_cpu = psutil.cpu_percent(interval=1)
    # print(p_mem)
    if(p_mem > 90):
        with open(file_path, 'a') as f:
            t2 = datetime.datetime.now()
            print(str(p_mem) + "    time: " + t2.strftime("%Y-%m-%d %H:%M:%S") + "    delta: " + str(t2-t1), file=f)
            t1 = t2
        os.system("xrayr restart")
    if(p_cpu >= 80):
        with open(file_path, 'a') as f:
            t2 = datetime.datetime.now()
            print("CPU: " + str(p_cpu) + "    time: " + t2.strftime("%Y-%m-%d %H:%M:%S") + "    delta: " + str(t2-t1), file=f)
            t1 = t2
        os.system("xrayr restart")
