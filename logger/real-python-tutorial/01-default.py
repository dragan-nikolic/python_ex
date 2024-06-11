"""
The logging module provides you with a default logger that allows you to get started without needing to do much configuration.

The output of this program would look like this:

---
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
---

The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger. (Loggers are discussed in detail in later sections.) This format, which shows the level, name, and message separated by a colon (:), is the default output format that can be configured to include things like timestamp, line number, and other details.

Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels if you want. You can also define your own severity levels by changing configurations, but it is generally not recommended as it can cause confusion with logs of some third-party libraries that you might be using.
"""

import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
