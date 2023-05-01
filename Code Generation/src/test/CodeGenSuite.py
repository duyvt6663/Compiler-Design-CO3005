import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """
            main: function void(){
                x = 1000;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(V), FloatLit(3.3))"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
