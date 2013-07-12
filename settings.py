import logging

############### SETTINGS ###########################

# General
LOG_LEVEL = logging.DEBUG

# Users' configuration files - "~" means underneath the user's home directory
GENERAL_CONF_FILE = "~/.rdc_general"
CONNECTIONS_CONF_FILE = "~/.rdc_connections"

# Resolution
HEIGHT_OFFSET = 0 # Pixel size wasted by FLUXBOX window manager  (taskbar + window decoration) - used for the "best fit" resolution autodetection (50pixels)
	          # Changed to Zero because the fluxbox windows manager  is disabled now. - Freiberg
		
AVAILABLE_RESOLUTIONS = ["640x480", "800x600", "1024x768", "1280x600", "1280x720", "1280x960", "1280x1024"]

# RDP
RDP_PORT = 3389
CONNECTION_TEST_TIMEOUT = 2 # Seconds of timeout when testing if target is accessible. Can also be a fraction

# XFreeRDP (Geva edit: XFREERDP_STATIC_PARAMS also contained "--sec" + "rdp", had to remove to support dualmon)
# example:  xfreerdp -a 32 -o --gdi sw --composition --sec rdp
# example dualmon:  xfreerdp /multimon /f /u:user /p:password /v:servername
XFREERDP_BIN = "xfreerdp"
XFREERDP_STATIC_PARAMS = [ "-x", "l", "/bpp:32", "-toggle-fullscreen", "/f", "/sound:sys:pulse","/cert-ignore","-sec-nla" ]

# GUI Configuration
LIST_WIDTH = 400
DISABLE_CLOSE_BUTTON = True
WINDOW_TITLE = "Remote Desktop Connection"
WINDOW_WIDTH = 0 # 0=Use minimum
WINDOW_HEIGHT = 0 # 0=Use minimum
ENABLE_BUTTONS_HAVE_ICONS = False # Update gnome configuration to enable icons on buttons
############### SETTINGS ###########################


