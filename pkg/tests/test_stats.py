import sys
import subprocess
import numpy as np
relativeHome='../'
srcDir=relativeHome+'labelSrc/'
#outDir=relativeHome+'output/'
sys.path.insert(0,'.')
sys.path.insert(0,relativeHome)
sys.path.insert(0,srcDir)
from labelSrc import *
from genPoints import *
import stats
class TestClass:
    def test_stats(capsys):
        expectedV,expectedCOM = genROI()
        proc=subprocess.run(['../labelSrc/stats.py', 'test3Dcubes.nii.gz', '-v','--stats','volume','com'],stdout=subprocess.PIPE)
        outputBuff=proc.stdout.decode("utf-8")
        lines=outputBuff.split('\n')[1:]
        for line in lines:
            if line!='':
                results=line.split(' ')
                results=list(filter(None, results))
                runV=results[1]
                runCOM=results[2:5]
                runV=float(runV)
                assert expectedV==float(runV)
                assert np.array_equal(list(map(lambda v:float(v),runCOM)),expectedCOM)
