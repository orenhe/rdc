import socket
import time
import subprocess
import logging
import settings
import getpass
import os
import datetime

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

def rdp_connect(address, user="", domain="", password="", dualmon=False):
    if not is_address_accessible(address):
        raise ConnectionFailedError()

    cmdline = [settings.XFREERDP_BIN]
    cmdline.extend(settings.XFREERDP_STATIC_PARAMS)

    if user:
        cmdline.extend(["/u:%s" %(user)])

    if password:
        cmdline.extend(["/p:%s" %(password)])

    if domain:
        cmdline.extend(["/d:%s" %(domain)])

    if dualmon:
        cmdline.extend(["/multimon"])

    cmdline.extend(["/v:%s" %(address)])
    #cmdline.append(address)

    proc = subprocess.Popen(cmdline)
    print  cmdline

    # Check if process died too quickly
    time.sleep(1)
    rc = proc.poll()
    logging.debug("poll() returned %s", rc)
    if rc is not None:
        logging.error("Process had died too quickly, rc=%d", rc)
        raise ConnectionFailedError()
    
    #straceline = "strace -tt -f -p {0} &> {1}".format(proc.pid, "{0}/{1}".format(folder, datestring))
    
    #logging.debug(straceline)
    #os.system(straceline)

    return proc.pid
