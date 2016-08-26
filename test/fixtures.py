import os
import signal
import time

_BEANSTALKD_PID = None


def setup(module):
    beanstalkd = os.getenv('BEANSTALKD', 'beanstalkd')
    module._BEANSTALKD_PID = os.spawnlp(
        os.P_NOWAIT,
        beanstalkd,
        beanstalkd, '-l', '127.0.0.1', '-p', '11300')
    time.sleep(0.5)  # Give beanstalkd some time to ready.


def teardown(module):
    os.kill(module._BEANSTALKD_PID, signal.SIGTERM)
