# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\7\t\u00b4\n\t\f\t\16\t\u00b7\13\t\3")
        buf.write("\t\3\t\6\t\u00bb\n\t\r\t\16\t\u00bc\7\t\u00bf\n\t\f\t")
        buf.write("\16\t\u00c2\13\t\3\t\5\t\u00c5\n\t\3\n\3\n\3\n\5\n\u00ca")
        buf.write("\n\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d2\n\n\3\n\3\n\3\13")
        buf.write("\3\13\7\13\u00d8\n\13\f\13\16\13\u00db\13\13\3\f\3\f\5")
        buf.write("\f\u00df\n\f\3\f\6\f\u00e2\n\f\r\f\16\f\u00e3\3\r\3\r")
        buf.write("\3\16\3\16\5\16\u00ea\n\16\3\17\3\17\3\17\7\17\u00ef\n")
        buf.write("\17\f\17\16\17\u00f2\13\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\7\20\u00fb\n\20\f\20\16\20\u00fe\13\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u0109\n\21")
        buf.write("\f\21\16\21\u010c\13\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u01ad\n;\3<\3<\3<\3=\3=\7=\u01b4\n=\f=\16=\u01b7\13")
        buf.write("=\3>\6>\u01ba\n>\r>\16>\u01bb\3>\3>\3?\3?\3?\3@\3@\3@")
        buf.write("\7@\u01c6\n@\f@\16@\u01c9\13@\3@\5@\u01cc\n@\3@\3@\3A")
        buf.write("\3A\3A\7A\u01d3\nA\fA\16A\u01d6\13A\3A\3A\3A\4\u00fc\u010a")
        buf.write("\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2")
        buf.write("\31\2\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26")
        buf.write("\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#")
        buf.write("K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66")
        buf.write("q\67s\2u\2w\2y8{9}:\177;\u0081<\3\2\f\3\2\63;\4\2GGgg")
        buf.write("\4\2--//\3\2\62;\5\2\f\f$$^^\n\2$$))^^ddhhppttvv\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\3\f\f\2\u01ef")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u008b")
        buf.write("\3\2\2\2\7\u0091\3\2\2\2\t\u0099\3\2\2\2\13\u00a0\3\2")
        buf.write("\2\2\r\u00a6\3\2\2\2\17\u00ab\3\2\2\2\21\u00c4\3\2\2\2")
        buf.write("\23\u00d1\3\2\2\2\25\u00d5\3\2\2\2\27\u00dc\3\2\2\2\31")
        buf.write("\u00e5\3\2\2\2\33\u00e9\3\2\2\2\35\u00eb\3\2\2\2\37\u00f6")
        buf.write("\3\2\2\2!\u0104\3\2\2\2#\u0111\3\2\2\2%\u011a\3\2\2\2")
        buf.write("\'\u0120\3\2\2\2)\u0129\3\2\2\2+\u012c\3\2\2\2-\u0131")
        buf.write("\3\2\2\2/\u0135\3\2\2\2\61\u013b\3\2\2\2\63\u0142\3\2")
        buf.write("\2\2\65\u0145\3\2\2\2\67\u0148\3\2\2\29\u014c\3\2\2\2")
        buf.write(";\u0154\3\2\2\2=\u0159\3\2\2\2?\u015f\3\2\2\2A\u0161\3")
        buf.write("\2\2\2C\u0164\3\2\2\2E\u0167\3\2\2\2G\u016a\3\2\2\2I\u016d")
        buf.write("\3\2\2\2K\u016f\3\2\2\2M\u0171\3\2\2\2O\u0173\3\2\2\2")
        buf.write("Q\u0175\3\2\2\2S\u0177\3\2\2\2U\u0179\3\2\2\2W\u017c\3")
        buf.write("\2\2\2Y\u017e\3\2\2\2[\u0181\3\2\2\2]\u0184\3\2\2\2_\u0186")
        buf.write("\3\2\2\2a\u0188\3\2\2\2c\u018a\3\2\2\2e\u018c\3\2\2\2")
        buf.write("g\u018e\3\2\2\2i\u0190\3\2\2\2k\u0192\3\2\2\2m\u0194\3")
        buf.write("\2\2\2o\u0196\3\2\2\2q\u0198\3\2\2\2s\u019a\3\2\2\2u\u01ac")
        buf.write("\3\2\2\2w\u01ae\3\2\2\2y\u01b1\3\2\2\2{\u01b9\3\2\2\2")
        buf.write("}\u01bf\3\2\2\2\177\u01c2\3\2\2\2\u0081\u01cf\3\2\2\2")
        buf.write("\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086\7v")
        buf.write("\2\2\u0086\u0087\7g\2\2\u0087\u0088\7i\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089\u008a\7t\2\2\u008a\4\3\2\2\2\u008b\u008c")
        buf.write("\7h\2\2\u008c\u008d\7n\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7c\2\2\u008f\u0090\7v\2\2\u0090\6\3\2\2\2\u0091\u0092")
        buf.write("\7d\2\2\u0092\u0093\7q\2\2\u0093\u0094\7q\2\2\u0094\u0095")
        buf.write("\7n\2\2\u0095\u0096\7g\2\2\u0096\u0097\7c\2\2\u0097\u0098")
        buf.write("\7p\2\2\u0098\b\3\2\2\2\u0099\u009a\7u\2\2\u009a\u009b")
        buf.write("\7v\2\2\u009b\u009c\7t\2\2\u009c\u009d\7k\2\2\u009d\u009e")
        buf.write("\7p\2\2\u009e\u009f\7i\2\2\u009f\n\3\2\2\2\u00a0\u00a1")
        buf.write("\7c\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7{\2\2\u00a5\f\3\2\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\16\3\2\2\2\u00ab\u00ac\7x\2\2\u00ac\u00ad")
        buf.write("\7q\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7f\2\2\u00af\20")
        buf.write("\3\2\2\2\u00b0\u00c5\7\62\2\2\u00b1\u00b5\t\2\2\2\u00b2")
        buf.write("\u00b4\5\31\r\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00c0")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\7a\2\2\u00b9")
        buf.write("\u00bb\5\31\r\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2")
        buf.write("\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00b8\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c3\u00c5\b\t\2\2\u00c4\u00b0\3")
        buf.write("\2\2\2\u00c4\u00b1\3\2\2\2\u00c5\22\3\2\2\2\u00c6\u00c7")
        buf.write("\5\21\t\2\u00c7\u00c9\5\25\13\2\u00c8\u00ca\5\27\f\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00d2\3\2\2\2")
        buf.write("\u00cb\u00cc\5\21\t\2\u00cc\u00cd\5\27\f\2\u00cd\u00d2")
        buf.write("\3\2\2\2\u00ce\u00cf\5\25\13\2\u00cf\u00d0\5\27\f\2\u00d0")
        buf.write("\u00d2\3\2\2\2\u00d1\u00c6\3\2\2\2\u00d1\u00cb\3\2\2\2")
        buf.write("\u00d1\u00ce\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\b")
        buf.write("\n\3\2\u00d4\24\3\2\2\2\u00d5\u00d9\5q9\2\u00d6\u00d8")
        buf.write("\5\31\r\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\26\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00dc\u00de\t\3\2\2\u00dd\u00df\t\4\2\2")
        buf.write("\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3")
        buf.write("\2\2\2\u00e0\u00e2\5\31\r\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\30\3\2\2\2\u00e5\u00e6\t\5\2\2\u00e6\32\3\2\2\2")
        buf.write("\u00e7\u00ea\5;\36\2\u00e8\u00ea\5=\37\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\34\3\2\2\2\u00eb\u00f0")
        buf.write("\7$\2\2\u00ec\u00ef\5s:\2\u00ed\u00ef\5u;\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f3\3\2\2\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7$\2\2\u00f4\u00f5\b")
        buf.write("\17\4\2\u00f5\36\3\2\2\2\u00f6\u00f7\7\61\2\2\u00f7\u00f8")
        buf.write("\7,\2\2\u00f8\u00fc\3\2\2\2\u00f9\u00fb\13\2\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00ff\u0100\7,\2\2\u0100\u0101\7\61\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0103\b\20\5\2\u0103 \3\2\2\2\u0104\u0105")
        buf.write("\7\61\2\2\u0105\u0106\7\61\2\2\u0106\u010a\3\2\2\2\u0107")
        buf.write("\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2")
        buf.write("\2\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010d")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7\f\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\b\21\5\2\u0110\"\3\2\2\2\u0111")
        buf.write("\u0112\7h\2\2\u0112\u0113\7w\2\2\u0113\u0114\7p\2\2\u0114")
        buf.write("\u0115\7e\2\2\u0115\u0116\7v\2\2\u0116\u0117\7k\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7p\2\2\u0119$\3\2\2\2\u011a")
        buf.write("\u011b\7d\2\2\u011b\u011c\7t\2\2\u011c\u011d\7g\2\2\u011d")
        buf.write("\u011e\7c\2\2\u011e\u011f\7m\2\2\u011f&\3\2\2\2\u0120")
        buf.write("\u0121\7e\2\2\u0121\u0122\7q\2\2\u0122\u0123\7p\2\2\u0123")
        buf.write("\u0124\7v\2\2\u0124\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126")
        buf.write("\u0127\7w\2\2\u0127\u0128\7g\2\2\u0128(\3\2\2\2\u0129")
        buf.write("\u012a\7k\2\2\u012a\u012b\7h\2\2\u012b*\3\2\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d\u012e\7n\2\2\u012e\u012f\7u\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130,\3\2\2\2\u0131\u0132\7h\2\2\u0132")
        buf.write("\u0133\7q\2\2\u0133\u0134\7t\2\2\u0134.\3\2\2\2\u0135")
        buf.write("\u0136\7y\2\2\u0136\u0137\7j\2\2\u0137\u0138\7k\2\2\u0138")
        buf.write("\u0139\7n\2\2\u0139\u013a\7g\2\2\u013a\60\3\2\2\2\u013b")
        buf.write("\u013c\7t\2\2\u013c\u013d\7g\2\2\u013d\u013e\7v\2\2\u013e")
        buf.write("\u013f\7w\2\2\u013f\u0140\7t\2\2\u0140\u0141\7p\2\2\u0141")
        buf.write("\62\3\2\2\2\u0142\u0143\7q\2\2\u0143\u0144\7h\2\2\u0144")
        buf.write("\64\3\2\2\2\u0145\u0146\7f\2\2\u0146\u0147\7q\2\2\u0147")
        buf.write("\66\3\2\2\2\u0148\u0149\7q\2\2\u0149\u014a\7w\2\2\u014a")
        buf.write("\u014b\7v\2\2\u014b8\3\2\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7p\2\2\u014e\u014f\7j\2\2\u014f\u0150\7g\2\2\u0150")
        buf.write("\u0151\7t\2\2\u0151\u0152\7k\2\2\u0152\u0153\7v\2\2\u0153")
        buf.write(":\3\2\2\2\u0154\u0155\7v\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("\u0157\7w\2\2\u0157\u0158\7g\2\2\u0158<\3\2\2\2\u0159")
        buf.write("\u015a\7h\2\2\u015a\u015b\7c\2\2\u015b\u015c\7n\2\2\u015c")
        buf.write("\u015d\7u\2\2\u015d\u015e\7g\2\2\u015e>\3\2\2\2\u015f")
        buf.write("\u0160\7#\2\2\u0160@\3\2\2\2\u0161\u0162\7(\2\2\u0162")
        buf.write("\u0163\7(\2\2\u0163B\3\2\2\2\u0164\u0165\7~\2\2\u0165")
        buf.write("\u0166\7~\2\2\u0166D\3\2\2\2\u0167\u0168\7?\2\2\u0168")
        buf.write("\u0169\7?\2\2\u0169F\3\2\2\2\u016a\u016b\7#\2\2\u016b")
        buf.write("\u016c\7?\2\2\u016cH\3\2\2\2\u016d\u016e\7-\2\2\u016e")
        buf.write("J\3\2\2\2\u016f\u0170\7/\2\2\u0170L\3\2\2\2\u0171\u0172")
        buf.write("\7,\2\2\u0172N\3\2\2\2\u0173\u0174\7\61\2\2\u0174P\3\2")
        buf.write("\2\2\u0175\u0176\7\'\2\2\u0176R\3\2\2\2\u0177\u0178\7")
        buf.write("@\2\2\u0178T\3\2\2\2\u0179\u017a\7@\2\2\u017a\u017b\7")
        buf.write("?\2\2\u017bV\3\2\2\2\u017c\u017d\7>\2\2\u017dX\3\2\2\2")
        buf.write("\u017e\u017f\7>\2\2\u017f\u0180\7?\2\2\u0180Z\3\2\2\2")
        buf.write("\u0181\u0182\7<\2\2\u0182\u0183\7<\2\2\u0183\\\3\2\2\2")
        buf.write("\u0184\u0185\7?\2\2\u0185^\3\2\2\2\u0186\u0187\7*\2\2")
        buf.write("\u0187`\3\2\2\2\u0188\u0189\7+\2\2\u0189b\3\2\2\2\u018a")
        buf.write("\u018b\7}\2\2\u018bd\3\2\2\2\u018c\u018d\7\177\2\2\u018d")
        buf.write("f\3\2\2\2\u018e\u018f\7]\2\2\u018fh\3\2\2\2\u0190\u0191")
        buf.write("\7_\2\2\u0191j\3\2\2\2\u0192\u0193\7=\2\2\u0193l\3\2\2")
        buf.write("\2\u0194\u0195\7<\2\2\u0195n\3\2\2\2\u0196\u0197\7.\2")
        buf.write("\2\u0197p\3\2\2\2\u0198\u0199\7\60\2\2\u0199r\3\2\2\2")
        buf.write("\u019a\u019b\n\6\2\2\u019bt\3\2\2\2\u019c\u019d\7^\2\2")
        buf.write("\u019d\u01ad\7d\2\2\u019e\u019f\7^\2\2\u019f\u01ad\7h")
        buf.write("\2\2\u01a0\u01a1\7^\2\2\u01a1\u01ad\7t\2\2\u01a2\u01a3")
        buf.write("\7^\2\2\u01a3\u01ad\7p\2\2\u01a4\u01a5\7^\2\2\u01a5\u01ad")
        buf.write("\7v\2\2\u01a6\u01a7\7^\2\2\u01a7\u01ad\7)\2\2\u01a8\u01a9")
        buf.write("\7^\2\2\u01a9\u01ad\7^\2\2\u01aa\u01ab\7^\2\2\u01ab\u01ad")
        buf.write("\7$\2\2\u01ac\u019c\3\2\2\2\u01ac\u019e\3\2\2\2\u01ac")
        buf.write("\u01a0\3\2\2\2\u01ac\u01a2\3\2\2\2\u01ac\u01a4\3\2\2\2")
        buf.write("\u01ac\u01a6\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01adv\3\2\2\2\u01ae\u01af\7^\2\2\u01af\u01b0\n")
        buf.write("\7\2\2\u01b0x\3\2\2\2\u01b1\u01b5\t\b\2\2\u01b2\u01b4")
        buf.write("\t\t\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6z\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b8\u01ba\t\n\2\2\u01b9\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\b>\5\2\u01be|\3")
        buf.write("\2\2\2\u01bf\u01c0\13\2\2\2\u01c0\u01c1\b?\6\2\u01c1~")
        buf.write("\3\2\2\2\u01c2\u01c7\7$\2\2\u01c3\u01c6\5s:\2\u01c4\u01c6")
        buf.write("\5u;\2\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cc\t\13\2")
        buf.write("\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write("\b@\7\2\u01ce\u0080\3\2\2\2\u01cf\u01d4\7$\2\2\u01d0\u01d3")
        buf.write("\5s:\2\u01d1\u01d3\5u;\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d7\u01d8\5w<\2\u01d8\u01d9\bA\b\2\u01d9\u0082\3\2")
        buf.write("\2\2\31\2\u00b5\u00bc\u00c0\u00c4\u00c9\u00d1\u00d9\u00de")
        buf.write("\u00e3\u00e9\u00ee\u00f0\u00fc\u010a\u01ac\u01b5\u01bb")
        buf.write("\u01c5\u01c7\u01cb\u01d2\u01d4\t\3\t\2\3\n\3\3\17\4\b")
        buf.write("\2\2\3?\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    BOOLEAN = 3
    STRING = 4
    ARRAY = 5
    AUTO = 6
    VOID = 7
    INTLIT = 8
    FLOATLIT = 9
    BOOLLIT = 10
    STRLIT = 11
    BlockComment = 12
    LineComment = 13
    Function = 14
    Break = 15
    Continue = 16
    If = 17
    Else = 18
    For = 19
    While = 20
    Return = 21
    Of = 22
    Do = 23
    Out = 24
    Inherit = 25
    TRue = 26
    FAlse = 27
    LNOT = 28
    LAND = 29
    LOR = 30
    EQUAL = 31
    NEQ = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    GRE = 38
    GEQ = 39
    LES = 40
    LEQ = 41
    CONCAT = 42
    ASSIGN = 43
    LB = 44
    RB = 45
    LP = 46
    RP = 47
    LS = 48
    RS = 49
    SEMI = 50
    COLON = 51
    COMMA = 52
    DOT = 53
    ID = 54
    WS = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
            "'auto'", "'void'", "'function'", "'break'", "'continue'", "'if'", 
            "'else'", "'for'", "'while'", "'return'", "'of'", "'do'", "'out'", 
            "'inherit'", "'true'", "'false'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'>='", "'<'", 
            "'<='", "'::'", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ARRAY", "AUTO", "VOID", 
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", "BlockComment", "LineComment", 
            "Function", "Break", "Continue", "If", "Else", "For", "While", 
            "Return", "Of", "Do", "Out", "Inherit", "TRue", "FAlse", "LNOT", 
            "LAND", "LOR", "EQUAL", "NEQ", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "GRE", "GEQ", "LES", "LEQ", "CONCAT", "ASSIGN", "LB", "RB", 
            "LP", "RP", "LS", "RS", "SEMI", "COLON", "COMMA", "DOT", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ARRAY", "AUTO", 
                  "VOID", "INTLIT", "FLOATLIT", "DECPART", "EXPOPART", "DEC", 
                  "BOOLLIT", "STRLIT", "BlockComment", "LineComment", "Function", 
                  "Break", "Continue", "If", "Else", "For", "While", "Return", 
                  "Of", "Do", "Out", "Inherit", "TRue", "FAlse", "LNOT", 
                  "LAND", "LOR", "EQUAL", "NEQ", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "GRE", "GEQ", "LES", "LEQ", "CONCAT", "ASSIGN", 
                  "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", "COMMA", 
                  "DOT", "STR_CHAR", "ESCSEQ", "ESCERROR", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.INTLIT_action 
            actions[8] = self.FLOATLIT_action 
            actions[13] = self.STRLIT_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	content = str(self.text) 
            	self.text = content[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	content = str(self.text)
            	esc = '\n'
            	if content[-1] in esc:
            		raise UncloseString(content[1:-1])
            	else:
            		raise UncloseString(content[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	content = str(self.text) 
            	raise IllegalEscape(content[1:])

     


