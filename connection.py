import socket
import time
import subprocess
import logging
import settings

class ConnectionFailedError(Exception):
    pass

def is_address_accessible(address):
    try:
        s = socket.create_connection((address, settings.RDP_PORT), settings.CONNECTION_TEST_TIMEOUT)
        s.close()
    except socket.error, e:
        logging.error("Connection to '%s:%s' has failed (%s)", address, settings.RDP_PORT, e)
        return False

    return True

def rdp_connect(address, user="", domain="", resolution="", fullscreen=False):
    if not is_address_accessible(address):
        raise ConnectionFailedError()

    cmdline = [settings.XFREERDP_BIN]
    cmdline.extend(settings.XFREERDP_STATIC_PARAMS)

    if user:
        cmdline.extend(["-u", user])

    if domain:
        cmdline.extend(["-d", domain])

    if resolution:
        cmdline.extend(["-g", resolution])

    if fullscreen:
        cmdline.extend(["-f"])

    cmdline.append(address)

    logging.info("Running %s", cmdline)
    proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if process died too quickly
    time.sleep(1)
    rc = proc.poll()
    logging.debug("poll() returned %s", rc)
    if rc is not None:
        logging.error("Process had died too quickly, rc=%d", rc)
        raise ConnectionFailedError()

    return
