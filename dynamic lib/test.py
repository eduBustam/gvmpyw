import sys
sys.settrace
import numpy as np
import numpy.testing as npt
import gvmpyw


def test2():
    print ("asdasd")
    obj_test=gvmpyw.PyTest(2,4)
    obj_test.py_setA(456)
    a=obj_test.py_getA()
    print(a)
def oftest():
    print("sad")
    of=gvmpyw.Py_ObjectiveFunction()
    print(of)
#def eltest():
#    print(gvmpyw.py_supermain())
def imagetest():
    a=np.float32([1.0,2.3,4.5])
    ig=gvmpyw.Py_Image(a,3)
    print(ig.py_getImage(3,a))
    print(ig.py_getImageCount())
    

imagetest()