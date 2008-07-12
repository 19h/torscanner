#!/usr/bin/env python

'''


    Exit statuses:
        -1:    Serious runtime error.
        0:     Program finished on unexpected point, but not on exception.
        1:     Program finished on unhandled exception. Please REPORT to author.
        42:    Program finished succesfully.
'''

import sys
sys.path.append('lib')

try:
    # Specialities
    import TorCtl       # https://www.torproject.org/svn/torflow/TorCtl/
    import GeoIPSupport # -||-
    import socks        # http://socksipy.sourceforge.net/
    import common

    # Standard Python modules
    import ConfigParser
    import socket
    import time
    import random
    import pickle
    import os
    import time
except ImportError, e:
    print "%s found, please install it and run again." % e
    sys.exit(-1)

# Will use first directory with "write" permission as data directory
DATADIR_PATHS = ['/var/lib/torscanner', '~/.torscanner', '.']

# Config files with priorities. First file with higher priority.
CONFIG_PATHS = ['torscanner.conf',               # Current directory
                '~/.torscanner/torscanner.conf', # User directory
                '/etc/torscanner.conf']          # System directory

# Use this settings when config file not found or any directive missing.
CONFIG_DEFAULTS = {}

if __name__ == '__main__':
    
    # Parsing command line arguments
    (options, args) = common.parseOptions()
    
    common.log('Starting TorScanner program at %s UTC...' % \
               time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()), 'CMD')
    
    #Joining cmdline param 'config' and list of default places
    cfgs = []
    if options.config: cfgs.extend([options.config])
    cfgs.extend(CONFIG_PATHS)

    # Loading configuration file
    config = ConfigParser.SafeConfigParser(CONFIG_DEFAULTS)
    for cfg in cfgs:
        cfg = os.path.abspath(os.path.expanduser(cfg))
        if os.path.exists(cfg):
            common.log("Using config file\t '%s'." % cfg)
            try:
                config.read(cfg)
            except Exception, e:
                common.log(e, 'ERROR')
                common.log("Config file corrupted, using built-in defaults.")
            break
        
    #Joining cmdline param 'data' and list of default datadir places
    datadirs = []
    if options.data: datadirs.extend([options.data])
    datadirs.extend(DATADIR_PATHS)

    # Selecting data directory
    for ddir in datadirs:
        ddir = os.path.abspath(os.path.expanduser(ddir))
        if os.path.exists(ddir) and os.path.os.access(ddir, os.W_OK):
            common.log("Using data directory '%s'." % ddir)
            break

    #print config.getint('preparation', 'max_download')
    if options.preparation:
        common.log('Starting preparation phase', 'CMD')

    if options.execution:
        common.log('Starting execution phase', 'CMD')

    if options.analysis:
        common.log('Starting analysis phase', 'CMD')
        
    # DO EVERYTHING HERE

    common.log('TorScanner succesfully finished at %s UTC.' %\
               time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()), 'CMD')
    sys.exit(42)
 