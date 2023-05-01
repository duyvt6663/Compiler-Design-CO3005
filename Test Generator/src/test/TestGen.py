import sys
import os 
import subprocess 
import shutil
import re
# import typing
import unittest
import random

TEMP_DIR = './tests'
TEST_DIR = './testcases'
SOL_DIR = './solutions'
GEN_DIR = '../../generator/'

class TestGen:
    def __init__(self, testMode, GEN_DIR, TEMP_DIR, SOL_DIR, TEST_DIR, CURR_DIR='./'):
        self.testMode = testMode
        self.GEN_DIR = GEN_DIR
        self.TEMP_DIR = TEMP_DIR
        self.SOL_DIR = SOL_DIR
        self.TEST_DIR = TEST_DIR
        self.CURR_DIR = CURR_DIR

    def generate(self):
        # install grammarinator if havnt already
        try:
            import grammarinator
        except ModuleNotFoundError:
            subprocess.run(["python", '-m', 'pip', 'install', "grammarinator"])

        # first delete the directory if it already exists
        if os.path.isdir(self.TEMP_DIR):
            shutil.rmtree(self.TEMP_DIR)
        # generate raw test cases/ depth = 20/ num_of_cases = 100
        # alredy reduce complexity by appending "1" after keywords, no need for loop anymore
        if self.testMode == "CheckerSuite":
            subprocess.run(["grammarinator-generate", "-r", "program", "-o", os.path.join(self.TEMP_DIR, 'test_%d'), "-d", "50", "-n", "100", 
                    "-p", self.GEN_DIR+"MT22UnparserChecker.py", "-l", self.GEN_DIR+"MT22UnlexerChecker.py",
                    "-t", "grammarinator.runtime.simple_space_transformer"], check=True)
        else:
            subprocess.run(["grammarinator-generate", "-r", "program", "-o", os.path.join(self.TEMP_DIR, 'test_%d'), "-d", "12", "-n", "500", 
                    "-p", self.GEN_DIR+"MT22Unparser.py", "-l", self.GEN_DIR+"MT22Unlexer.py",
                    "-t", "grammarinator.runtime.simple_space_transformer"], check=True)
        if self.testMode == "LexerSuite":
            pass 
        elif self.testMode == "ParserSuite":
            self.ParserGen()
        elif self.testMode == "ASTGenSuite":
            self.ASTGen()
        elif self.testMode == "CheckerSuite":
            self.CheckerGen()
    
    def ParserGen(self):
        # from raw cases output a ParserSuite.py of 100 parser cases
        res = open(self.CURR_DIR+"ParserSuite.py", 'w', encoding='utf-8')
        res.write( # import and class declaration
            "import unittest\nfrom TestUtils import TestParser\n\n"
            "class ParserSuite(unittest.TestCase):\n"
        )
        for i, filename in enumerate(os.listdir(self.TEMP_DIR)):
            f = os.path.join(self.TEMP_DIR, filename)
            content = open(f, 'r',encoding='utf-8')
            content_str = content.read().encode('ascii', 'ignore').decode()
            filename = re.sub(r'\d+', str(i+201), filename)
            res.write(
                f"\tdef {filename}(self):\n"
                f"\t\tinput = \"\"\"{content_str}\"\"\"\n"
                "\t\texpect = \"successful\"\n"
                f"\t\tself.assertTrue(TestParser.test(input, expect, {i+201}))\n\n"
            )
            content.close()
        shutil.rmtree(self.TEMP_DIR)
    def ASTGen(self):
        # from raw cases output a ASTGenSuite.py of 100 AST cases
        file = open(self.CURR_DIR+"ASTGenSuite.py", 'w', encoding='utf-8')
        file.write( # import and class declaration
            "import unittest\nfrom TestUtils import TestAST\n\n"
            "class ASTGenSuite(unittest.TestCase):\n"
        )
        for i, filename in enumerate(os.listdir(self.TEMP_DIR)):
            f = os.path.join(self.TEMP_DIR, filename)
            content = open(f, 'r',encoding='utf-8')
            content_str = content.read().encode('ascii', 'ignore').decode()
            filename = re.sub(r'\d+', str(i+301), filename)
            file.write(
                f"\tdef {filename}(self):\n"
                f"\t\tinput = \"\"\"{content_str}\"\"\"\n"
                "\t\texpect = \"successful\"\n"
                f"\t\tself.assertTrue(TestAST.test(input, expect, {i+301}))\n\n"
            )
            content.close()
        file.close()
        # now the hard part, run run.py on ASTGenSuite to obtain solutions 
        # and then write them back to the file
        from ASTGenSuite import ASTGenSuite
        self.getAndTest(ASTGenSuite)
        # while(len(os.listdir(SOL_DIR)) < 100):
        #     getAndTest(ASTGenSuite)
        file = open(self.CURR_DIR+"ASTGenSuite.py", 'r+',encoding='utf-8')
        lines = file.readlines()
        sols = os.listdir(self.SOL_DIR)
        ind = 0
        # print(lines)
        for i in range(len(lines)):
            if '\t\texpect = \"successful\"' in lines[i] and ind < len(sols):
                f = os.path.join(self.SOL_DIR, sols[ind])
                content = open(f, 'r',encoding='utf-8')
                content_str = content.read().replace('\\', '\\\\')
                lines[i] = f'''\t\texpect = """{content_str}"""\n'''
                content.close()
                ind += 1
        # print(lines)
        file.seek(0)
        file.truncate()
        file.write("".join(lines))
        file.close()
        shutil.rmtree(self.TEMP_DIR)

    def CheckerGen(self):
        # from raw cases output a CheckerSuite.py of 500 cases
        file = open(self.CURR_DIR+"CheckerSuite.py", 'w', encoding='utf-8')
        file.write( # import and class declaration
            "import unittest\nfrom TestUtils import TestChecker\n\n"
            "class CheckerSuite(unittest.TestCase):\n"
        )
        for i, filename in enumerate(os.listdir(self.TEMP_DIR)):
            f = os.path.join(self.TEMP_DIR, filename)
            content = open(f, 'r',encoding='utf-8')
            content_str = content.read().encode('ascii', 'ignore').decode()
            filename = re.sub(r'\d+', str(i+401), filename)
            file.write(
                f"\tdef {filename}(self):\n"
                f"\t\tinput = \"\"\"{content_str}\"\"\"\n"
                "\t\texpect = \"successful\"\n"
                f"\t\tself.assertTrue(TestChecker.test(input, expect, {i+401}))\n\n"
            )
            content.close()
        file.close()
        # now the hard part, run run.py on CheckerSuite to obtain solutions 
        # and then write them back to the file
        from CheckerSuite import CheckerSuite
        self.getAndTest(CheckerSuite)

        file = open(self.CURR_DIR+"CheckerSuite.py", 'r+',encoding='utf-8')
        lines = file.readlines()
        sols = os.listdir(self.SOL_DIR)
        ind = 0
        i = 0
        while i < len(lines):
            if '\t\texpect = \"successful\"' in lines[i] and ind < len(sols):
                f = os.path.join(self.SOL_DIR, sols[ind])
                content = open(f, 'r',encoding='utf-8')
                content_str = content.read().replace('\\', '\\\\')
                if 'Undeclared' not in content_str or\
                    ('Undeclared' in content_str and random.random() < 0.1):
                    lines[i] = f'''\t\texpect = """{content_str}"""\n'''
                else:
                    # pop undeclared cases
                    j = i-1 # start deleting from assert line
                    while('def test_' not in lines[j]): j -= 1
                    del lines[j:i+2]
                content.close()
                ind += 1
            i += 1
        # print(lines)
        file.seek(0)
        file.truncate()
        file.write("".join(lines))
        file.close()
        shutil.rmtree(self.TEMP_DIR)

    def getAndTest(self, cls):
        suite = unittest.makeSuite(cls)
        self.test(suite)

    def test(self, suite):
        from pprint import pprint
        from io import StringIO
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream)
        result = runner.run(suite)

    def cleanTest(self):
        shutil.rmtree(self.TEST_DIR)
        os.makedirs(self.TEST_DIR)
        shutil.rmtree(self.SOL_DIR)
        os.makedirs(self.SOL_DIR)

if __name__ == "__main__":
    # GEN = TestGen("ParserSuite", GEN_DIR, TEMP_DIR, SOL_DIR, TEST_DIR)
    GEN = TestGen("CheckerSuite", GEN_DIR, TEMP_DIR, SOL_DIR, TEST_DIR)
    GEN.cleanTest()
    GEN.generate()