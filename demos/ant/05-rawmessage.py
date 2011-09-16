"""
Do a system reset using raw messages.

"""

import sys
import time

from codinghyde.ant import driver
from codinghyde.ant import message
from codinghyde.ant.constants import *

from config import *

# Initialize
stick = driver.USB1Driver(SERIAL, debug=DEBUG)
stick.open()

# Prepare system reset message
msg = message.Message()
msg.setType(MESSAGE_SYSTEM_RESET)
msg.setPayload('\x00')

# Send
stick.write(msg.encode())

# Wait for reset to complete
time.sleep(1)

# Alternatively, we could have done this:
msg = message.SystemResetMessage()
stick.write(msg.encode())
time.sleep(1)

# Shutdown
stick.close()
