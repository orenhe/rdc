import logging
import os
import gtk
import settings

ALLOWED_GENERAL_CONF_KEYS = ["readonly"]

ENTRY_FIELDS = ["name", "address", "domain", "user"]

REQUIRED_FIELDS = ["address" , "user"]

FIELD_DESCRIPTION = {
                     "name": "Display Name",
                     "address": "IP/Hostname",
                     "user": "User",
                     "domain": "Domain",
                     }


def create_liststore():
    return gtk.ListStore(str, str, str, str)

def populate(liststore):
    conf_file = os.path.expanduser(settings.CONNECTIONS_CONF_FILE)

    if not os.path.exists(conf_file):
        # File doesn't exist, return the empty liststore
        return liststore

    with file(conf_file) as f:
        lines = f.readlines()
        rdp_settings_reader = RdpSettingsReader(lines)
        return rdp_settings_reader.populate_liststore(liststore)

def dump_settings_to_file(liststore):
    conf_file = os.path.expanduser(settings.CONNECTIONS_CONF_FILE)
    rdp_settings_writer = RdpSettingsWriter(liststore)
    with file(conf_file, "w") as f:
        out = str(rdp_settings_writer)
        logging.info("Writing to file %s:\n%s", conf_file, out)
        logging.info("EOF")
        f.write(str(rdp_settings_writer))
        logging.info("Configuration was written successfully")


class ListEntry(object):
    def __init__(self, name, address, user="", domain=""):
        self.name = name
        self.address = address
        self.user = user
        self.domain = domain

    @classmethod
    def init_by_iter(cls, iter, model):
        name = model.get_value(iter, 0)
        address = model.get_value(iter, 1)
        user = model.get_value(iter, 2)
        domain = model.get_value(iter, 3)
        logging.info("Clicked entry %s (%s)", name, address)

        return cls(name=name, address=address, user=user, domain=domain)

    @classmethod
    def init_empty(cls):
        return cls("", "", "", "", "")

    def to_liststore_row_format(self):
        return [self.name, self.address, self.user, self.domain]

class RdpSettingsReader(object):
    def __init__(self, lines):
        self.lines = lines

    def populate_liststore(self, liststore):
        for line in self.lines:
            line = line.strip()
            values = line.split(":")
            if len(values) != len(ENTRY_FIELDS):
                raise AssertionError("Settings has an unexpected number of fields")
            assert len(values) == len(ENTRY_FIELDS)
            logging.info("Input settings: %s", values)
            liststore.append(values)
        
        return liststore
            
class RdpSettingsWriter(object):
    def __init__(self, liststore):
        self.liststore = liststore

    def __str__(self):
        out = []
        iter = self.liststore.get_iter_first()
        while iter is not None:
            entry = []
            for i in range(len(ENTRY_FIELDS)):
                entry.append(self.liststore.get_value(iter, i))
                
            out.append(":".join(entry))
            iter = self.liststore.iter_next(iter)

        logging.info("Output settings: '%s'", out)

        return "\n".join(out)

def load_general_settings_from_file(conf):
    """Tries to load settings from GENERAL_CONF_FILE and returns a dict
    
    Returns an empty dict if no settings"""
    filename = os.path.expanduser(settings.GENERAL_CONF_FILE)
    logging.info("Checking for general config file '%s'", filename)
    if not os.path.exists(filename):
        logging.info("General config file not found")
        return conf

    logging.info("Trying to open '%s' for read...", filename)
    with file(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            keyval = line.split("=")
            if len(keyval) != 2:
                logging.warning("Bad line '%s'", line)
                continue

            (key, value) = keyval
            if key not in ALLOWED_GENERAL_CONF_KEYS:
                logging.warning("Bad key '%s'", key)
                continue
            logging.info("config: updating '%s' = '%s'", key, value)
            conf[key] = value
    
    return None # updates the provided dict
