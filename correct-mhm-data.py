#!/usr/bin/env python

#this script flips the data in the mhm output so that it is oriented correctly.
#i.e. no longer upside down.
#warning: changes the file in-place, does not create a new file

from netCDF4 import Dataset
import numpy as np

rootgrp = Dataset('mhm_30min_efas_AET_2008.nc', "a")

variable = rootgrp.variables['aET']

data = variable

#print data.shape
#print data[0][0]

inverted = data[::,::-1,::]

variable[:,:,:] = inverted

rootgrp.close()
