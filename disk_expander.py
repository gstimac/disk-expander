__author__ = 'gstimac'
import os
import subprocess
from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults

# define our default configuration options
defaults = init_defaults('disk_expander')
defaults['disk_expander']['debug'] = False

# define the application class
class MyApp(CementApp):
    class Meta:
        label = 'disk_expander'
        config_defaults = defaults

def expand_physical(volume):
    print subprocess.Popen("(echo d; echo 3; echo n; echo p; echo 3; echo ; echo ; echo t; echo 3; echo 8e; echo w;) | fdisk /dev/sda", shell=True, stdout=subprocess.PIPE).stdout.read()
    return

def expand_logical():
    return

with MyApp() as app:
    # add arguments to the parser
    app.args.add_argument('-pv', '--physical_volume', action='store', dest='physical_volume',
                          help='expand the last added physical volume')
    app.args.add_argument('-lv', '--logical_volume', action='store', dest='logical_volume',
                          help='expand the last added logical volume')
    app.run()

    if app.pargs.physical_volume is not None:
        expand_physical(app.pargs.physical_volume)
    elif app.pargs.logical_volume is not None:
        expand_logical(app.pargs.logical_volume)
    else:
        print "Please choose (wisely) between a physical and logical volume expansion!"

