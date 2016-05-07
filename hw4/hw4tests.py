"""
Unit tests for Homework 4, CMPS101 Spring16

How do you test?
================

1) Copy this file to the folder where you saved hw4.py, rename this file to "hw4test.py"
2) Just run this on terminal (you can also click green button in Spyder)

    python3 hw2test.py

3) If the output is similar to

    ----------------------------------------------------------------------
    Ran 4 tests in 0.007s

    OK (expected failures=1)


    this means that you did not implement the bonus problem but are good to go.
    If you implemented the bonus problem, your test should show


    ----------------------------------------------------------------------
    Ran 4 tests in 0.006s

    OK (unexpected successes=1)


    If neither of these show up, look at the error messages and at the way
    we run the tests in order to figure out what might be wrong with your code.

4) Note that the file check will fail until you have created all the neccessary
files for submission.

5) Once you are done with all of this, don't forget to submit!

May the odds be ever in your favor!

"""
import hw4
import numpy as np
import numpy.testing as nt
from scipy import linalg
import unittest
import os.path

class Hw4Test(unittest.TestCase):
    def setUp(self):
        self.nxn= [
            np.random.randint(-5,50,[2,2]),
            np.random.randint(-5,50,[4,4]),
            np.random.randint(-5,50,[8,8]),
            np.random.randint(-5,50,[16,16])
        ]
        self.had = [
            linalg.hadamard(2),
            linalg.hadamard(4),
            linalg.hadamard(8),
            linalg.hadamard(16)
        ]
        self.vec = [
            np.random.randint(-5,50,[2]),
            np.random.randint(-5,50,[4]),
            np.random.randint(-5,50,[8]),
            np.random.randint(-5,50,[16])
        ]

    def testMatMult(self):
        """" Problem 1: matmult(A,x).

        Multiply a matrix with a vector."""
        for t in range(4):
            nt.assert_equal(hw4.matmult(self.nxn[t],self.vec[t]),
                            self.nxn[t].dot(self.vec[t]))

    def testHadMat(self):
        """ Problem 2: hadmat(k).

        Create hadamard of size 2^k calls student hadmat with t=1,2,3,4
        it is supposed to generate hadmat of size 2,4,8,16"""
        for t in range(4):
            nt.assert_equal(hw4.hadmat(t+1), self.had[t])

    def testHadMatMult(self):
        """ Problem 4: hadmatmult(H,x).

        Takes hadamart H and self.vector x, multiplies."""
        for t in range(4):
            nt.assert_equal(hw4.hadmatmult(self.had[t],self.vec[t]),
                            self.had[t].dot(self.vec[t]))

    @unittest.expectedFailure
    def testEfficientMatMult(self):
        """ Bonus problem: efficienthadmatmult(x) """
        for t in range(4):
            nt.assert_equal(hw4.efficienthadmatmult(self.vec[t]),
                            self.had[t].dot(self.vec[t]))

if __name__ == '__main__':
    #Assignment 4 file checks
    filesok=True
    if not os.path.isfile("../partners.txt"):
        filesok=False        
        print("\nCannot find ../partners.txt.\n")
    if not os.path.isfile("matmulttime.pdf"):
        filesok=False        
        print("\nCannot find matmulttime.pdf.\n")
    if not os.path.isfile("analysis.pdf"):
        filesok=False        
        print("\nCannot find analysis.pdf\n")
    if filesok:
        print("\nSeems like you have all your files placed correctly!\n")

    unittest.main(exit=False)