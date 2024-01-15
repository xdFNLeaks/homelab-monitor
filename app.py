from flask import Flask, render_template
import psutil
import datetime
import time

app = Flask(__name__)

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime = str(datetime.timedelta(seconds=uptime_seconds))
    return uptime

def format_uptime(uptime):
    days, remainder = divmod(uptime.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(days), int(hours), int(minutes), int(seconds)

@app.route('/')
def home():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    uptime_seconds = psutil.boot_time()
    uptime = format_uptime(datetime.datetime.now() - datetime.datetime.fromtimestamp(uptime_seconds))
    return render_template('index.html', cpu_percent=cpu_percent, memory_info=memory_info, uptime=uptime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
