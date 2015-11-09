# first python script to make changes to juniper device
# we're using simple set commands in set_config.set to configure device
from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config

# first create netconf device object and then open connection
device = Device(host='vsrx04.t-i.demo',user='ncs',passwd="xxxxx")
device.open()

# Now create config object and load candidate configuration
cfg = Config(device)
cfg.load(path="set_config.set",format="set")

# Lock candidate configuration
cfg.lock()

# now try to commit changes
if(cfg.commit(comment="eznc generated config")):
    print "changes made to %s" % device.hostname
else:
    print "failed"

# no unlock candidate configuration again
cfg.unlock()

# we're done, close netconf connection
device.close()
