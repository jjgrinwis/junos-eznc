# some pyez script to get some routes using Tables and Views
# you can create your own tables and views
# first import some modules
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from pprint import pprint as pp

# define device object and use open method to connect
# netconf used to connect to device
dev = Device(host='vsrx04.t-i.demo',user='ncs',password='UCS@dmin01')
dev.open()

# now bind this table to dev and get all routes from this device
# we could be looking for specific route but we're just loading complete route table for now.
routes = RouteTable(dev)
routes.get()

# every route is a View.RouteTableView object from this routes OpTable.RouteTable class.
# now loop through this list and print View.RouteTableView object elements
for route in routes:
    pp (route.items())
    pp (route.via)

# close netconf connection
dev.close()