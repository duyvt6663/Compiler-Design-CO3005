import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    ##################################################################
    #                           TEST ID                              #
    ##################################################################
    def test_100_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 100))
    def test_102_uppercase_identifier(self):
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 102))

    def test_103_lower_upper_id1(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",103))
    def test_104_lower_upper_id2(self):
        self.assertTrue(TestLexer.test("AaBbCc", "AaBbCc,<EOF>",104))

    def test_105_mixed_lowercase_id(self):
        self.assertTrue(TestLexer.test("abc123", "abc123,<EOF>", 105))
    def test_106_mixed_uppercase_id(self):
        self.assertTrue(TestLexer.test("ABC123", "ABC123,<EOF>", 106))

    def test_107_mixed_id1(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",107))
    def test_108_mixed_id2(self):
        self.assertTrue(TestLexer.test("AaSvn3", "AaSvn3,<EOF>", 108))

    def test_109_underscore_id1(self):
        self.assertTrue(TestLexer.test("abc_123", "abc_123,<EOF>", 109))
    def test_110_underscore_id2(self):
        self.assertTrue(TestLexer.test("ABC_123", "ABC_123,<EOF>", 110))
    def test_111_underscore_id3(self):
        self.assertTrue(TestLexer.test("aBc_d123", "aBc_d123,<EOF>", 111))
    def test_112_underscore_id4(self):
        self.assertTrue(TestLexer.test("abC_D123", "abC_D123,<EOF>", 112))
    def test_113_underscore_id5(self):
        self.assertTrue(TestLexer.test("_abc", "_abc,<EOF>", 113))
    def test_114_underscore_id6(self):
        self.assertTrue(TestLexer.test("abc_", "abc_,<EOF>", 114))
    def test_115_underscore_id7(self):
        self.assertTrue(TestLexer.test("__ABC", "__ABC,<EOF>", 115))
    def test_116_underscore_id8(self):
        self.assertTrue(TestLexer.test("__123", "__123,<EOF>", 116))
    def test_117_underscore_id9(self):
        self.assertTrue(TestLexer.test("abc_123", "abc_123,<EOF>", 117))
    def test_118_underscore_id10(self):
        self.assertTrue(TestLexer.test("_123abc", "_123abc,<EOF>", 118))
    def test_119_underscore_id11(self):
        self.assertTrue(TestLexer.test("______", "______,<EOF>", 119))
    def test_120_underscore_id12(self):
        self.assertTrue(TestLexer.test("a123_", "a123_,<EOF>", 120))
    ##################################################################
    #                           TEST INTLIT                          #
    ##################################################################
    def test_121_integer(self):
        self.assertTrue(TestLexer.test("00001", "0,0,0,0,1,<EOF>",121))
    def test_122_integer(self):
        self.assertTrue(TestLexer.test("00010", "0,0,0,10,<EOF>", 122))
    def test_123_integer(self):
        self.assertTrue(TestLexer.test("00_0", "0,0,_0,<EOF>", 123))
    def test_124_integer(self):
        self.assertTrue(TestLexer.test("000_", "0,0,0,_,<EOF>", 124))
    def test_125_integer(self):
        self.assertTrue(TestLexer.test("0_0_0", "0,_0_0,<EOF>", 125))
    def test_126_integer(self):
        self.assertTrue(TestLexer.test("0_00", "0,_00,<EOF>", 126))

    def test_127_integer(self):
        self.assertTrue(TestLexer.test("01234567", "0,1234567,<EOF>", 127))
    def test_128_integer(self):
        self.assertTrue(TestLexer.test("00000", "0,0,0,0,0,<EOF>", 128))
    def test_129_integer(self):
        self.assertTrue(TestLexer.test("000123", "0,0,0,123,<EOF>", 129))
    def test_130_integer(self):
        self.assertTrue(TestLexer.test("00_00_", "0,0,_00_,<EOF>", 130))
    def test_131_integer(self):
        self.assertTrue(TestLexer.test("0012_8", "0,0,128,<EOF>", 131))
    
    def test_132_integer(self):
        self.assertTrue(TestLexer.test("-123", "-,123,<EOF>", 132))
    def test_133_integer(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 133))
    def test_134_integer(self):
        self.assertTrue(TestLexer.test("1_234_567_", "1234567,_,<EOF>", 134))
    def test_135_integer(self):
        self.assertTrue(TestLexer.test("00123_456_789_ABC_DEF", "0,0,123456789,_ABC_DEF,<EOF>", 135))
    def test_136_integer(self):
        self.assertTrue(TestLexer.test("00123A", "0,0,123,A,<EOF>", 136))
    def test_137_integer(self):
        self.assertTrue(TestLexer.test("00_01", "0,0,_01,<EOF>", 137))
    def test_138_integer(self):
        self.assertTrue(TestLexer.test("0,ABC_DEF", "0,,,ABC_DEF,<EOF>", 138))
    def test_139_integer(self):
        self.assertTrue(TestLexer.test("0_01AB", "0,_01AB,<EOF>", 139))
    def test_140_integer(self):
        self.assertTrue(TestLexer.test("001_AB_", "0,0,1,_AB_,<EOF>", 140))
    def test_141_integer(self):
        self.assertTrue(TestLexer.test("0_F11", "0,_F11,<EOF>", 141))
    def test_142_integer(self):
        self.assertTrue(TestLexer.test("0F11_", "0,F11_,<EOF>", 142))
    def test_143_integer(self):
        self.assertTrue(TestLexer.test("0abcd", "0,abcd,<EOF>", 143))
    def test_144_integer(self):
        self.assertTrue(TestLexer.test("01A1a_b", "0,1,A1a_b,<EOF>", 144))
    #####################################################################
    #                           TEST FLOATLIT                           #
    #####################################################################
    def test_145_float1(self):
        self.assertTrue(TestLexer.test("1.0234", "1.0234,<EOF>", 145))
    def test_146_float2(self):
        self.assertTrue(TestLexer.test("000000.000","0,0,0,0,0,0.000,<EOF>",146))
    def test_147_float3(self):
        self.assertTrue(TestLexer.test("1.001", "1.001,<EOF>", 147))
    def test_148_float4(self):
        self.assertTrue(TestLexer.test("1.0e01", "1.0e01,<EOF>", 148))
    def test_149_float5(self):
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 149))
    def test_150_float6(self):
        self.assertTrue(TestLexer.test("0.200000", "0.200000,<EOF>", 150))
        # self.assertTrue(TestLexer.test("0.00000000", "0.00000000,<EOF>", 150))
    def test_151_float7(self):
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 151))
    def test_152_float8(self):
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 152))
    def test_153_float9(self):
        self.assertTrue(TestLexer.test("1_2.E-1_0", "12.E-1,_0,<EOF>", 153))
    def test_154_float10(self):
        self.assertTrue(TestLexer.test("1_.23", "1,_,.,23,<EOF>", 154))
    def test_155_float11(self):
        self.assertTrue(TestLexer.test("12e01","12e01,<EOF>",155))
    def test_156_float12(self):
        self.assertTrue(TestLexer.test(".e3", ".e3,<EOF>", 156))
    def test_157_float13(self):
        self.assertTrue(TestLexer.test(".E+10", ".E+10,<EOF>", 157))
    def test_158_float14(self):
        self.assertTrue(TestLexer.test(".e-101230xA_F", ".e-101230,xA_F,<EOF>", 158))
    def test_159_float15(self):
        self.assertTrue(TestLexer.test(".E0b001", ".E0,b001,<EOF>", 159))
    def test_160_float16(self):
        self.assertTrue(TestLexer.test(".E00b001", ".E00,b001,<EOF>", 160))
    def test_161_float17(self):
        self.assertTrue(TestLexer.test(".e000X01AB", ".e000,X01AB,<EOF>", 161))
    #####################################################################
    #                           TEST BOOLEAN                            #
    #####################################################################
    def test_162_boolean1(self):
        self.assertTrue(TestLexer.test("True", "True,<EOF>", 162))
    def test_163_boolean2(self):
        self.assertTrue(TestLexer.test("False", "False,<EOF>", 163))
    def test_164_boolean3(self):
        self.assertTrue(TestLexer.test("trueFalse", "trueFalse,<EOF>", 164))
    #####################################################################
    #                           TEST STRING                             #
    #####################################################################
    def test_165_string1(self):
        self.assertTrue(TestLexer.test("\\\"","Error Token \\", 165))
    def test_166_string2(self):
        self.assertTrue(TestLexer.test("\"Hello World!\"", "Hello World!,<EOF>", 166))
    def test_167_string3(self):
        self.assertTrue(TestLexer.test("\"He asked me\\\"", "Unclosed String: He asked me\\\"", 167))
    def test_168_string4(self):
        self.assertTrue(TestLexer.test("\"Nguyen \\b \\f Minh \\r \\n \\t \\\' \\\\ Tam\"", "Nguyen \\b \\f Minh \\r \\n \\t \\\' \\\\ Tam,<EOF>", 168))
    def test_169_string5(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 169))
    def test_170_string6(self):
        self.assertTrue(TestLexer.test("\"\\b \\' He is my ex's man\"", "\\b \\' He is my ex's man,<EOF>", 170))
    def test_171_string7(self):
        self.assertTrue(TestLexer.test("\"She is Tam\'s girlfriend.\"", "She is Tam\'s girlfriend.,<EOF>", 171))

    def test_172_string_unclose1(self):
        self.assertTrue(TestLexer.test("\"He is a man", "Unclosed String: He is a man", 172))
    def test_173_string_unclosed2(self):
        self.assertTrue(TestLexer.test("\"abc \\n \\f 's def", "Unclosed String: abc \\n \\f 's def", 173))
    def test_174_string_unclose3(self):
        self.assertTrue(TestLexer.test("\"He is \\b a man", "Unclosed String: He is \\b a man", 174))
    def test_175_string_unclosed4(self):
        self.assertTrue(TestLexer.test("\"It is a unclosed \\n string", "Unclosed String: It is a unclosed \\n string", 175))
    def test_176_string_unclosed5(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: \\\"Where \\\"is\\\" John?\\\"\" \"I am not closed", "This is a \\t string \\n containing tab ,He asked \\n me: \\\"Where \\\"is\\\" John?\\\",Unclosed String: I am not closed", 176))
    
    def test_177_string_illegal_esc1(self):
        self.assertTrue(TestLexer.test("\"I have an escape sequence \\\"Here it is \\k\\\"\"", "Illegal Escape In String: I have an escape sequence \\\"Here it is \k", 177))
    def test_178_string_illegal_esc2(self):
        self.assertTrue(TestLexer.test("\"\\a He is a man\"", "Illegal Escape In String: \\a", 178))
    def test_179_string_illegal_esc3(self):
        self.assertTrue(TestLexer.test("\"\\\\ He is a \\\\ \\\' 19-year-old man \\a\"", "Illegal Escape In String: \\\\ He is a \\\\ \\\' 19-year-old man \\a", 179))
    def test_101_string_random(self):
        input = """ "whflke+32-403rfre\\b\\f\\"hellothere\\"" """
        expect = """whflke+32-403rfre\\b\\f\\"hellothere\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))
    #####################################################################
    #                           TEST OPERATOR                           #
    #####################################################################
    def test_180_operator1(self):
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 180))
    def test_181_operator2(self):
        self.assertTrue(TestLexer.test("====", "==,==,<EOF>", 181))
    def test_182_operator3(self):
        self.assertTrue(TestLexer.test("||||", "||,||,<EOF>", 182))
    def test_183_operator4(self):
        self.assertTrue(TestLexer.test("[a,1,b]", "[,a,,,1,,,b,],<EOF>", 183))
    def test_184_operator5(self):
        self.assertTrue(TestLexer.test("*/%::!=!<><===.+.", "*,/,%,::,!=,!,<,>,<=,==,.,+,.,<EOF>", 184))
    def test_185_operator6(self):
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 185))
    def test_186_operator7(self):
        self.assertTrue(TestLexer.test("-12_3", "-,123,<EOF>", 186))
    def test_187_operator8(self):
        self.assertTrue(TestLexer.test("-00123_AEF", "-,0,0,123,_AEF,<EOF>", 187))
    def test_188_operator9(self):
        self.assertTrue(TestLexer.test("-0000_1238", "-,0,0,0,0,_1238,<EOF>", 188))
    def test_189_operator10(self):
        self.assertTrue(TestLexer.test("-0123043520b10", "-,0,123043520,b10,<EOF>", 189))
    #####################################################################
    #                           TEST KEYWORD                            #
    #####################################################################
    def test_190_keyword1(self):
        self.assertTrue(TestLexer.test("Break, Continue, If, Elseif", "Break,,,Continue,,,If,,,Elseif,<EOF>", 190))
    def test_191_keyword2(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 191))
    def test_192_keyword3(self):
        self.assertTrue(TestLexer.test("NULL", "NULL,<EOF>", 192))
    #####################################################################
    #                           TEST SEPARATOR                          #
    #####################################################################
    def test_193_separator(self):
        self.assertTrue(TestLexer.test("()[].,;{}", "(,),[,],.,,,;,{,},<EOF>", 193))
    #####################################################################
    #                           TEST MIXED CASES                        #
    #####################################################################
    def test_194_for_stmt(self):
        input = """Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }"""
        expected = "Foreach,(,i,In,1,.,.,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 194))

    def test_195_method_invocation_stmt(self):
        input = """Shape::$getNumOfShape();"""
        expected = "Shape,::,Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 195))

    def test_196_block_stmt(self):
        input = """{
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        }"""
        expected = "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 196))

    def test_197_comment1(self):
        input = """/* This is a 
            multi-line 
            comment.*/"""
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 197))

    def test_198_comment2(self):
        input = "### This is a comment. ###"
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 198))
    
    def test_199_dot(self):
        self.assertTrue(TestLexer.test("1.....1", "1.,.,.,.,.,1,<EOF>", 199))
    def test_500(self):
        input = """ "hello
abc """
        expect = """Unclosed String: hello\n"""
        self.assertTrue(TestLexer.test(input, expect, 500))
    def test_501(self):
        input = """ "\\f" """
        expect = """\\f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 501))
        