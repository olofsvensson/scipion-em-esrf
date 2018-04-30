# coding: utf-8
# **************************************************************************
# *
# * Author:     Olof Svensson (svensson@esrf.fr) [1]
# *
# * [1] European Synchrotron Radiation Facility
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import os
import json
import time
import pprint
import unittest

from esrf_utils_icat import UtilsIcat

class Test(unittest.TestCase):


    def test_findGridSquaresNotUploaded(self):
        allParams = json.loads(open("/scisoft/pxsoft/data/cryoem/testRunData/20180423/allParams.json").read())
        dictGridSquares = UtilsIcat.findGridSquaresNotUploaded(allParams)
        pprint.pprint(dictGridSquares)

    def test_getStackTraceLog(self):
        errorMessage = None
        try:
            print(1/0)
        except:
            errorMessage = UtilsIcat.getStackTraceLog()
        print(errorMessage)
        self.assertNotEquals(errorMessage, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()