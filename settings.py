import logging

############### SETTINGS ###########################

# General
LOG_LEVEL = logging.DEBUG

# Users' configuration files - "~" means underneath the user's home directory
GENERAL_CONF_FILE = "~/.rdc_general"
CONNECTIONS_CONF_FILE = "~/.rdc_connections"

# Resolution
HEIGHT_OFFSET = 50 # Pixel size wasted by window manager  (taskbar + window decoration) - used for the "best fit" resolution autodetection 
AVAILABLE_RESOLUTIONS = ["640x480", "1024x768", "1280x1024"]

# RDP
RDP_PORT = 3389
CONNECTION_TEST_TIMEOUT = 2 # Seconds of timeout when testing if target is accessible. Can also be a fraction

# XFreeRDP
XFREERDP_BIN = "xfreerdp"
XFREERDP_STATIC_PARAMS = [ "-a" , "32" , "-x", "l", "--no-nla", "--no-osb", "--no-tls" , "--gdi", "sw" , "--composition" ]

# GUI Configuration
LIST_WIDTH = 400
DISABLE_CLOSE_BUTTON = True
WINDOW_TITLE = "Remote Desktop Connection"
WINDOW_WIDTH = 0 # 0=Use minimum
WINDOW_HEIGHT = 0 # 0=Use minimum
ENABLE_BUTTONS_HAVE_ICONS = True # Update gnome configuration to enable icons on buttons
############### SETTINGS ###########################


