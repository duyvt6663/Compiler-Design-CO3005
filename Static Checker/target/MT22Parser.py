# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u0149\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4W\n\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5_\n\5\f\5\16\5b\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6j\n\6\3\6\3\6\3\6\5\6o\n")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\7\7v\n\7\f\7\16\7y\13\7\3\b\5\b")
        buf.write("|\n\b\3\b\5\b\177\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008f\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009d\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\5\r\u00ad\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\5\22\u00c5\n\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\7\24\u00cf\n\24\f\24\16\24\u00d2")
        buf.write("\13\24\3\24\3\24\3\25\3\25\3\25\5\25\u00d9\n\25\3\26\3")
        buf.write("\26\5\26\u00dd\n\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u00e6\n\30\f\30\16\30\u00e9\13\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u00f4\n\31\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u00fa\n\32\f\32\16\32\u00fd\13\32\5")
        buf.write("\32\u00ff\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u010b\n\33\3\34\3\34\3\34\5\34\u0110\n")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u011e\n\36\f\36\16\36\u0121\13\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0128\n\37\3 \3 \3 \3 \3 \5")
        buf.write(" \u012f\n \3!\3!\3!\3!\3!\3!\5!\u0137\n!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\7!\u0142\n!\f!\16!\u0145\13!\3\"\3\"\3\"")
        buf.write("\2\3@#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@B\2\b\3\2\3\6\4\2!\"(+\3\2%\'\3\2#$")
        buf.write("\3\2\37 \5\2\3\4\6\t\20\35\2\u0155\2E\3\2\2\2\4M\3\2\2")
        buf.write("\2\6O\3\2\2\2\bZ\3\2\2\2\nc\3\2\2\2\fr\3\2\2\2\16{\3\2")
        buf.write("\2\2\20\u008e\3\2\2\2\22\u0090\3\2\2\2\24\u0095\3\2\2")
        buf.write("\2\26\u009e\3\2\2\2\30\u00ac\3\2\2\2\32\u00ae\3\2\2\2")
        buf.write("\34\u00b4\3\2\2\2\36\u00bc\3\2\2\2 \u00bf\3\2\2\2\"\u00c2")
        buf.write("\3\2\2\2$\u00c8\3\2\2\2&\u00cb\3\2\2\2(\u00d8\3\2\2\2")
        buf.write("*\u00dc\3\2\2\2,\u00de\3\2\2\2.\u00e0\3\2\2\2\60\u00f3")
        buf.write("\3\2\2\2\62\u00f5\3\2\2\2\64\u010a\3\2\2\2\66\u010c\3")
        buf.write("\2\2\28\u0113\3\2\2\2:\u0118\3\2\2\2<\u0127\3\2\2\2>\u012e")
        buf.write("\3\2\2\2@\u0136\3\2\2\2B\u0146\3\2\2\2DF\5\4\3\2ED\3\2")
        buf.write("\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\2\2\3")
        buf.write("J\3\3\2\2\2KN\5\6\4\2LN\5\n\6\2MK\3\2\2\2ML\3\2\2\2N\5")
        buf.write("\3\2\2\2OP\5\b\5\2PQ\7\65\2\2QV\5(\25\2RS\7-\2\2ST\5:")
        buf.write("\36\2TU\b\4\1\2UW\3\2\2\2VR\3\2\2\2VW\3\2\2\2WX\3\2\2")
        buf.write("\2XY\7\64\2\2Y\7\3\2\2\2Z`\78\2\2[\\\7\66\2\2\\]\78\2")
        buf.write("\2]_\b\5\1\2^[\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a")
        buf.write("\t\3\2\2\2b`\3\2\2\2cd\78\2\2de\7\65\2\2ef\7\20\2\2fg")
        buf.write("\5*\26\2gi\7.\2\2hj\5\f\7\2ih\3\2\2\2ij\3\2\2\2jk\3\2")
        buf.write("\2\2kn\7/\2\2lm\7\33\2\2mo\78\2\2nl\3\2\2\2no\3\2\2\2")
        buf.write("op\3\2\2\2pq\5&\24\2q\13\3\2\2\2rw\5\16\b\2st\7\66\2\2")
        buf.write("tv\5\16\b\2us\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\r")
        buf.write("\3\2\2\2yw\3\2\2\2z|\7\33\2\2{z\3\2\2\2{|\3\2\2\2|~\3")
        buf.write("\2\2\2}\177\7\32\2\2~}\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\78\2\2\u0081\u0082\7\65\2\2\u0082")
        buf.write("\u0083\5(\25\2\u0083\17\3\2\2\2\u0084\u008f\5\22\n\2\u0085")
        buf.write("\u008f\5\24\13\2\u0086\u008f\5\26\f\2\u0087\u008f\5\32")
        buf.write("\16\2\u0088\u008f\5\34\17\2\u0089\u008f\5\36\20\2\u008a")
        buf.write("\u008f\5 \21\2\u008b\u008f\5\"\22\2\u008c\u008f\5$\23")
        buf.write("\2\u008d\u008f\5&\24\2\u008e\u0084\3\2\2\2\u008e\u0085")
        buf.write("\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u0087\3\2\2\2\u008e")
        buf.write("\u0088\3\2\2\2\u008e\u0089\3\2\2\2\u008e\u008a\3\2\2\2")
        buf.write("\u008e\u008b\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3")
        buf.write("\2\2\2\u008f\21\3\2\2\2\u0090\u0091\5\30\r\2\u0091\u0092")
        buf.write("\7-\2\2\u0092\u0093\5<\37\2\u0093\u0094\7\64\2\2\u0094")
        buf.write("\23\3\2\2\2\u0095\u0096\7\23\2\2\u0096\u0097\7.\2\2\u0097")
        buf.write("\u0098\5<\37\2\u0098\u0099\7/\2\2\u0099\u009c\5\20\t\2")
        buf.write("\u009a\u009b\7\24\2\2\u009b\u009d\5\20\t\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\25\3\2\2\2\u009e\u009f")
        buf.write("\7\25\2\2\u009f\u00a0\7.\2\2\u00a0\u00a1\5\30\r\2\u00a1")
        buf.write("\u00a2\7-\2\2\u00a2\u00a3\5<\37\2\u00a3\u00a4\7\66\2\2")
        buf.write("\u00a4\u00a5\5<\37\2\u00a5\u00a6\7\66\2\2\u00a6\u00a7")
        buf.write("\5<\37\2\u00a7\u00a8\7/\2\2\u00a8\u00a9\5\20\t\2\u00a9")
        buf.write("\27\3\2\2\2\u00aa\u00ad\58\35\2\u00ab\u00ad\78\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\31\3\2\2\2\u00ae")
        buf.write("\u00af\7\26\2\2\u00af\u00b0\7.\2\2\u00b0\u00b1\5<\37\2")
        buf.write("\u00b1\u00b2\7/\2\2\u00b2\u00b3\5\20\t\2\u00b3\33\3\2")
        buf.write("\2\2\u00b4\u00b5\7\31\2\2\u00b5\u00b6\5&\24\2\u00b6\u00b7")
        buf.write("\7\26\2\2\u00b7\u00b8\7.\2\2\u00b8\u00b9\5<\37\2\u00b9")
        buf.write("\u00ba\7/\2\2\u00ba\u00bb\7\64\2\2\u00bb\35\3\2\2\2\u00bc")
        buf.write("\u00bd\7\21\2\2\u00bd\u00be\7\64\2\2\u00be\37\3\2\2\2")
        buf.write("\u00bf\u00c0\7\22\2\2\u00c0\u00c1\7\64\2\2\u00c1!\3\2")
        buf.write("\2\2\u00c2\u00c4\7\27\2\2\u00c3\u00c5\5<\37\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\7\64\2\2\u00c7#\3\2\2\2\u00c8\u00c9\5\66\34\2\u00c9")
        buf.write("\u00ca\7\64\2\2\u00ca%\3\2\2\2\u00cb\u00d0\7\60\2\2\u00cc")
        buf.write("\u00cf\5\20\t\2\u00cd\u00cf\5\6\4\2\u00ce\u00cc\3\2\2")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d3\u00d4\7\61\2\2\u00d4\'\3\2\2\2\u00d5")
        buf.write("\u00d9\5,\27\2\u00d6\u00d9\5.\30\2\u00d7\u00d9\7\b\2\2")
        buf.write("\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9)\3\2\2\2\u00da\u00dd\5(\25\2\u00db\u00dd")
        buf.write("\7\t\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("+\3\2\2\2\u00de\u00df\t\2\2\2\u00df-\3\2\2\2\u00e0\u00e1")
        buf.write("\7\7\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e7\7\n\2\2\u00e3")
        buf.write("\u00e4\7\66\2\2\u00e4\u00e6\7\n\2\2\u00e5\u00e3\3\2\2")
        buf.write("\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00eb\7\63\2\2\u00eb\u00ec\7\30\2\2\u00ec\u00ed\5,\27")
        buf.write("\2\u00ed/\3\2\2\2\u00ee\u00f4\7\n\2\2\u00ef\u00f4\7\13")
        buf.write("\2\2\u00f0\u00f4\7\f\2\2\u00f1\u00f4\7\r\2\2\u00f2\u00f4")
        buf.write("\5\62\32\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f3")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2")
        buf.write("\u00f4\61\3\2\2\2\u00f5\u00fe\7\60\2\2\u00f6\u00fb\5<")
        buf.write("\37\2\u00f7\u00f8\7\66\2\2\u00f8\u00fa\5<\37\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fe\u00f6\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u0101\7\61\2\2\u0101\63\3\2\2\2\u0102\u010b")
        buf.write("\5\60\31\2\u0103\u010b\58\35\2\u0104\u010b\78\2\2\u0105")
        buf.write("\u010b\5\66\34\2\u0106\u0107\7.\2\2\u0107\u0108\5<\37")
        buf.write("\2\u0108\u0109\7/\2\2\u0109\u010b\3\2\2\2\u010a\u0102")
        buf.write("\3\2\2\2\u010a\u0103\3\2\2\2\u010a\u0104\3\2\2\2\u010a")
        buf.write("\u0105\3\2\2\2\u010a\u0106\3\2\2\2\u010b\65\3\2\2\2\u010c")
        buf.write("\u010d\78\2\2\u010d\u010f\7.\2\2\u010e\u0110\5:\36\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7/\2\2\u0112\67\3\2\2\2\u0113\u0114\78\2")
        buf.write("\2\u0114\u0115\7\62\2\2\u0115\u0116\5:\36\2\u0116\u0117")
        buf.write("\7\63\2\2\u01179\3\2\2\2\u0118\u011f\5<\37\2\u0119\u011a")
        buf.write("\7\66\2\2\u011a\u011b\5<\37\2\u011b\u011c\b\36\1\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u0119\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120;\3\2\2")
        buf.write("\2\u0121\u011f\3\2\2\2\u0122\u0128\5> \2\u0123\u0124\5")
        buf.write("> \2\u0124\u0125\7,\2\2\u0125\u0126\5> \2\u0126\u0128")
        buf.write("\3\2\2\2\u0127\u0122\3\2\2\2\u0127\u0123\3\2\2\2\u0128")
        buf.write("=\3\2\2\2\u0129\u012f\5@!\2\u012a\u012b\5@!\2\u012b\u012c")
        buf.write("\t\3\2\2\u012c\u012d\5@!\2\u012d\u012f\3\2\2\2\u012e\u0129")
        buf.write("\3\2\2\2\u012e\u012a\3\2\2\2\u012f?\3\2\2\2\u0130\u0131")
        buf.write("\b!\1\2\u0131\u0132\7$\2\2\u0132\u0137\5@!\b\u0133\u0134")
        buf.write("\7\36\2\2\u0134\u0137\5@!\7\u0135\u0137\5\64\33\2\u0136")
        buf.write("\u0130\3\2\2\2\u0136\u0133\3\2\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0137\u0143\3\2\2\2\u0138\u0139\f\6\2\2\u0139\u013a\t")
        buf.write("\4\2\2\u013a\u0142\5@!\7\u013b\u013c\f\5\2\2\u013c\u013d")
        buf.write("\t\5\2\2\u013d\u0142\5@!\6\u013e\u013f\f\4\2\2\u013f\u0140")
        buf.write("\t\6\2\2\u0140\u0142\5@!\5\u0141\u0138\3\2\2\2\u0141\u013b")
        buf.write("\3\2\2\2\u0141\u013e\3\2\2\2\u0142\u0145\3\2\2\2\u0143")
        buf.write("\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144A\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0146\u0147\t\7\2\2\u0147C\3\2\2\2\37G")
        buf.write("MV`inw{~\u008e\u009c\u00ac\u00c4\u00ce\u00d0\u00d8\u00dc")
        buf.write("\u00e7\u00f3\u00fb\u00fe\u010a\u010f\u011f\u0127\u012e")
        buf.write("\u0136\u0141\u0143")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'integer'", "'float'", "'boolean'", "'string'", 
                     "'array'", "'auto'", "'void'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'function'", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'while'", "'return'", "'of'", "'do'", "'out'", 
                     "'inherit'", "'true'", "'false'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'>'", "'>='", "'<'", "'<='", "'::'", "'='", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "FLOAT", "BOOLEAN", "STRING", 
                      "ARRAY", "AUTO", "VOID", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "STRLIT", "BlockComment", "LineComment", "Function", 
                      "Break", "Continue", "If", "Else", "For", "While", 
                      "Return", "Of", "Do", "Out", "Inherit", "TRue", "FAlse", 
                      "LNOT", "LAND", "LOR", "EQUAL", "NEQ", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "GRE", "GEQ", "LES", "LEQ", "CONCAT", 
                      "ASSIGN", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                      "COLON", "COMMA", "DOT", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_idlist = 3
    RULE_funcdecl = 4
    RULE_paramlist = 5
    RULE_paramdecl = 6
    RULE_stmt = 7
    RULE_assignstmt = 8
    RULE_ifstmt = 9
    RULE_forstmt = 10
    RULE_scalarVar = 11
    RULE_whilestmt = 12
    RULE_dowhilestmt = 13
    RULE_breakstmt = 14
    RULE_continuestmt = 15
    RULE_returnstmt = 16
    RULE_callstmt = 17
    RULE_blockstmt = 18
    RULE_vartype = 19
    RULE_functype = 20
    RULE_atomic = 21
    RULE_arrtype = 22
    RULE_literal = 23
    RULE_index_arrlit = 24
    RULE_operands = 25
    RULE_funcall = 26
    RULE_index_expr = 27
    RULE_param = 28
    RULE_expr = 29
    RULE_string_expr = 30
    RULE_num_expr = 31
    RULE_keyword = 32

    ruleNames =  [ "program", "decl", "vardecl", "idlist", "funcdecl", "paramlist", 
                   "paramdecl", "stmt", "assignstmt", "ifstmt", "forstmt", 
                   "scalarVar", "whilestmt", "dowhilestmt", "breakstmt", 
                   "continuestmt", "returnstmt", "callstmt", "blockstmt", 
                   "vartype", "functype", "atomic", "arrtype", "literal", 
                   "index_arrlit", "operands", "funcall", "index_expr", 
                   "param", "expr", "string_expr", "num_expr", "keyword" ]

    EOF = Token.EOF
    INTEGER=1
    FLOAT=2
    BOOLEAN=3
    STRING=4
    ARRAY=5
    AUTO=6
    VOID=7
    INTLIT=8
    FLOATLIT=9
    BOOLLIT=10
    STRLIT=11
    BlockComment=12
    LineComment=13
    Function=14
    Break=15
    Continue=16
    If=17
    Else=18
    For=19
    While=20
    Return=21
    Of=22
    Do=23
    Out=24
    Inherit=25
    TRue=26
    FAlse=27
    LNOT=28
    LAND=29
    LOR=30
    EQUAL=31
    NEQ=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    GRE=38
    GEQ=39
    LES=40
    LEQ=41
    CONCAT=42
    ASSIGN=43
    LB=44
    RB=45
    LP=46
    RP=47
    LS=48
    RS=49
    SEMI=50
    COLON=51
    COMMA=52
    DOT=53
    ID=54
    WS=55
    ERROR_CHAR=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.decl()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.ID):
                    break

            self.state = 71
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._idlist = None # IdlistContext
            self._param = None # ParamContext

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            localctx._idlist = self.idlist()
            self.state = 78
            self.match(MT22Parser.COLON)
            self.state = 79
            self.vartype()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ASSIGN:
                self.state = 80
                self.match(MT22Parser.ASSIGN)
                self.state = 81
                localctx._param = self.param()
                if localctx._idlist.iSize != localctx._param.pSize: 
                            raise NoViableAltException(self)


            self.state = 86
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.iSize = 1

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MT22Parser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 89
                self.match(MT22Parser.COMMA)
                self.state = 90
                self.match(MT22Parser.ID)
                localctx.iSize += 1
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def Function(self):
            return self.getToken(MT22Parser.Function, 0)

        def functype(self):
            return self.getTypedRuleContext(MT22Parser.FunctypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistContext,0)


        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MT22Parser.ID)
            self.state = 98
            self.match(MT22Parser.COLON)
            self.state = 99
            self.match(MT22Parser.Function)
            self.state = 100
            self.functype()
            self.state = 101
            self.match(MT22Parser.LB)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Out) | (1 << MT22Parser.Inherit) | (1 << MT22Parser.ID))) != 0):
                self.state = 102
                self.paramlist()


            self.state = 105
            self.match(MT22Parser.RB)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Inherit:
                self.state = 106
                self.match(MT22Parser.Inherit)
                self.state = 107
                self.match(MT22Parser.ID)


            self.state = 110
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ParamdeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ParamdeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.paramdecl()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 113
                self.match(MT22Parser.COMMA)
                self.state = 114
                self.paramdecl()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def Out(self):
            return self.getToken(MT22Parser.Out, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = MT22Parser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Inherit:
                self.state = 120
                self.match(MT22Parser.Inherit)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.Out:
                self.state = 123
                self.match(MT22Parser.Out)


            self.state = 126
            self.match(MT22Parser.ID)
            self.state = 127
            self.match(MT22Parser.COLON)
            self.state = 128
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.dowhilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 136
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.returnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 138
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 139
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarVar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarVarContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.scalarVar()
            self.state = 143
            self.match(MT22Parser.ASSIGN)
            self.state = 144
            self.expr()
            self.state = 145
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(MT22Parser.If, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def Else(self):
            return self.getToken(MT22Parser.Else, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MT22Parser.If)
            self.state = 148
            self.match(MT22Parser.LB)
            self.state = 149
            self.expr()
            self.state = 150
            self.match(MT22Parser.RB)
            self.state = 151
            self.stmt()
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 152
                self.match(MT22Parser.Else)
                self.state = 153
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(MT22Parser.For, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def scalarVar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarVarContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MT22Parser.For)
            self.state = 157
            self.match(MT22Parser.LB)
            self.state = 158
            self.scalarVar()
            self.state = 159
            self.match(MT22Parser.ASSIGN)
            self.state = 160
            self.expr()
            self.state = 161
            self.match(MT22Parser.COMMA)
            self.state = 162
            self.expr()
            self.state = 163
            self.match(MT22Parser.COMMA)
            self.state = 164
            self.expr()
            self.state = 165
            self.match(MT22Parser.RB)
            self.state = 166
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(MT22Parser.Index_exprContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalarVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarVar" ):
                return visitor.visitScalarVar(self)
            else:
                return visitor.visitChildren(self)




    def scalarVar(self):

        localctx = MT22Parser.ScalarVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scalarVar)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MT22Parser.While)
            self.state = 173
            self.match(MT22Parser.LB)
            self.state = 174
            self.expr()
            self.state = 175
            self.match(MT22Parser.RB)
            self.state = 176
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(MT22Parser.Do, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MT22Parser.Do)
            self.state = 179
            self.blockstmt()
            self.state = 180
            self.match(MT22Parser.While)
            self.state = 181
            self.match(MT22Parser.LB)
            self.state = 182
            self.expr()
            self.state = 183
            self.match(MT22Parser.RB)
            self.state = 184
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(MT22Parser.Break, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MT22Parser.Break)
            self.state = 187
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(MT22Parser.Continue, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MT22Parser.Continue)
            self.state = 190
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(MT22Parser.Return, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MT22Parser.Return)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRLIT) | (1 << MT22Parser.LNOT) | (1 << MT22Parser.SUB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LP) | (1 << MT22Parser.ID))) != 0):
                self.state = 193
                self.expr()


            self.state = 196
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.funcall()
            self.state = 199
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VardeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VardeclContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MT22Parser.LP)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Break) | (1 << MT22Parser.Continue) | (1 << MT22Parser.If) | (1 << MT22Parser.For) | (1 << MT22Parser.While) | (1 << MT22Parser.Return) | (1 << MT22Parser.Do) | (1 << MT22Parser.LP) | (1 << MT22Parser.ID))) != 0):
                self.state = 204
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 202
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 203
                    self.vardecl()
                    pass


                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic(self):
            return self.getTypedRuleContext(MT22Parser.AtomicContext,0)


        def arrtype(self):
            return self.getTypedRuleContext(MT22Parser.ArrtypeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_vartype)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.atomic()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.arrtype()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(MT22Parser.AUTO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctype" ):
                return visitor.visitFunctype(self)
            else:
                return visitor.visitChildren(self)




    def functype(self):

        localctx = MT22Parser.FunctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functype)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING, MT22Parser.ARRAY, MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.vartype()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)




    def atomic(self):

        localctx = MT22Parser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atomic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(MT22Parser.LS, 0)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INTLIT)
            else:
                return self.getToken(MT22Parser.INTLIT, i)

        def RS(self):
            return self.getToken(MT22Parser.RS, 0)

        def Of(self):
            return self.getToken(MT22Parser.Of, 0)

        def atomic(self):
            return self.getTypedRuleContext(MT22Parser.AtomicContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrtype" ):
                return visitor.visitArrtype(self)
            else:
                return visitor.visitChildren(self)




    def arrtype(self):

        localctx = MT22Parser.ArrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arrtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MT22Parser.ARRAY)
            self.state = 223
            self.match(MT22Parser.LS)
            self.state = 224
            self.match(MT22Parser.INTLIT)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 225
                self.match(MT22Parser.COMMA)
                self.state = 226
                self.match(MT22Parser.INTLIT)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(MT22Parser.RS)
            self.state = 233
            self.match(MT22Parser.Of)
            self.state = 234
            self.atomic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(MT22Parser.STRLIT, 0)

        def index_arrlit(self):
            return self.getTypedRuleContext(MT22Parser.Index_arrlitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(MT22Parser.INTLIT)
                pass
            elif token in [MT22Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(MT22Parser.FLOATLIT)
                pass
            elif token in [MT22Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.match(MT22Parser.BOOLLIT)
                pass
            elif token in [MT22Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.match(MT22Parser.STRLIT)
                pass
            elif token in [MT22Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.index_arrlit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_arrlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_index_arrlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arrlit" ):
                return visitor.visitIndex_arrlit(self)
            else:
                return visitor.visitChildren(self)




    def index_arrlit(self):

        localctx = MT22Parser.Index_arrlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_index_arrlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MT22Parser.LP)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRLIT) | (1 << MT22Parser.LNOT) | (1 << MT22Parser.SUB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LP) | (1 << MT22Parser.ID))) != 0):
                self.state = 244
                self.expr()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MT22Parser.COMMA:
                    self.state = 245
                    self.match(MT22Parser.COMMA)
                    self.state = 246
                    self.expr()
                    self.state = 251
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 254
            self.match(MT22Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(MT22Parser.Index_exprContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MT22Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operands)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.index_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.funcall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.match(MT22Parser.LB)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(MT22Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MT22Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MT22Parser.ID)
            self.state = 267
            self.match(MT22Parser.LB)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.STRLIT) | (1 << MT22Parser.LNOT) | (1 << MT22Parser.SUB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LP) | (1 << MT22Parser.ID))) != 0):
                self.state = 268
                self.param()


            self.state = 271
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LS(self):
            return self.getToken(MT22Parser.LS, 0)

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def RS(self):
            return self.getToken(MT22Parser.RS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = MT22Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.ID)
            self.state = 274
            self.match(MT22Parser.LS)
            self.state = 275
            self.param()
            self.state = 276
            self.match(MT22Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pSize = 1

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.expr()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 279
                self.match(MT22Parser.COMMA)
                self.state = 280
                self.expr()
                localctx.pSize += 1
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.String_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.String_exprContext,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.string_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.string_expr()
                self.state = 290
                self.match(MT22Parser.CONCAT)
                self.state = 291
                self.string_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Num_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Num_exprContext,i)


        def NEQ(self):
            return self.getToken(MT22Parser.NEQ, 0)

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def GRE(self):
            return self.getToken(MT22Parser.GRE, 0)

        def GEQ(self):
            return self.getToken(MT22Parser.GEQ, 0)

        def LES(self):
            return self.getToken(MT22Parser.LES, 0)

        def LEQ(self):
            return self.getToken(MT22Parser.LEQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = MT22Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_string_expr)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.num_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.num_expr(0)
                self.state = 297
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.GRE) | (1 << MT22Parser.GEQ) | (1 << MT22Parser.LES) | (1 << MT22Parser.LEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.num_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def num_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Num_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Num_exprContext,i)


        def LNOT(self):
            return self.getToken(MT22Parser.LNOT, 0)

        def operands(self):
            return self.getTypedRuleContext(MT22Parser.OperandsContext,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def LAND(self):
            return self.getToken(MT22Parser.LAND, 0)

        def LOR(self):
            return self.getToken(MT22Parser.LOR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_num_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_expr" ):
                return visitor.visitNum_expr(self)
            else:
                return visitor.visitChildren(self)



    def num_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Num_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_num_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.state = 303
                self.match(MT22Parser.SUB)
                self.state = 304
                self.num_expr(6)
                pass
            elif token in [MT22Parser.LNOT]:
                self.state = 305
                self.match(MT22Parser.LNOT)
                self.state = 306
                self.num_expr(5)
                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRLIT, MT22Parser.LB, MT22Parser.LP, MT22Parser.ID]:
                self.state = 307
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 319
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MT22Parser.Num_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num_expr)
                        self.state = 310
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 311
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 312
                        self.num_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = MT22Parser.Num_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num_expr)
                        self.state = 313
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 314
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 315
                        self.num_expr(4)
                        pass

                    elif la_ == 3:
                        localctx = MT22Parser.Num_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num_expr)
                        self.state = 316
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 317
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.LAND or _la==MT22Parser.LOR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 318
                        self.num_expr(3)
                        pass

             
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class KeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def Function(self):
            return self.getToken(MT22Parser.Function, 0)

        def Break(self):
            return self.getToken(MT22Parser.Break, 0)

        def Continue(self):
            return self.getToken(MT22Parser.Continue, 0)

        def If(self):
            return self.getToken(MT22Parser.If, 0)

        def Else(self):
            return self.getToken(MT22Parser.Else, 0)

        def For(self):
            return self.getToken(MT22Parser.For, 0)

        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def Return(self):
            return self.getToken(MT22Parser.Return, 0)

        def Of(self):
            return self.getToken(MT22Parser.Of, 0)

        def Do(self):
            return self.getToken(MT22Parser.Do, 0)

        def Out(self):
            return self.getToken(MT22Parser.Out, 0)

        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def TRue(self):
            return self.getToken(MT22Parser.TRue, 0)

        def FAlse(self):
            return self.getToken(MT22Parser.FAlse, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_keyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = MT22Parser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.STRING) | (1 << MT22Parser.ARRAY) | (1 << MT22Parser.AUTO) | (1 << MT22Parser.VOID) | (1 << MT22Parser.Function) | (1 << MT22Parser.Break) | (1 << MT22Parser.Continue) | (1 << MT22Parser.If) | (1 << MT22Parser.Else) | (1 << MT22Parser.For) | (1 << MT22Parser.While) | (1 << MT22Parser.Return) | (1 << MT22Parser.Of) | (1 << MT22Parser.Do) | (1 << MT22Parser.Out) | (1 << MT22Parser.Inherit) | (1 << MT22Parser.TRue) | (1 << MT22Parser.FAlse))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.num_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def num_expr_sempred(self, localctx:Num_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




