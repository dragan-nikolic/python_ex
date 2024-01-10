import signal
import time
import sys

def cb_signal_handler(signum, frame):
    """
    called when signal is received
    """
    print 'signum=%s, frame=%s' % (str(signum), str(frame))
    print 'BYE, BYE...'
    sys.exit(1)
    

signal.signal(signal.CTRL_C_EVENT, cb_signal_handler)
signal.signal(signal.CTRL_BREAK_EVENT, cb_signal_handler)
#signal.signal(signal.SIGINT, cb_signal_handler)
#signal.signal(signal.SIGBREAK, cb_signal_handler)
#signal.signal(signal.SIGABRT, cb_signal_handler)

start_time = time.time()
while(time.time() - start_time < 30):
    print time.time()
    time.sleep(2)
