import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
	def test_401(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  R  : float   = R [ ( 0      )   + readInteger ( R    :: bar ( )      )        ]    > ( R [ ! pLrV       ]      )     , ! R [ - 201_4        ]      :: 0    != R [ R   > R     , R   == R      ]       ;
  o  : auto  ;
   ZXH7E  : array [ 0 , 980_3_6_6_8_8_95185 ] of float    = printInteger ( )    <= ZXH7E    :: ZXH7E [ 0     :: ZXH7E      ]    / ( o     )      , ZXH7E   != bar ( ( R     )     , bar ( ZXH7E     , ZXH7E [ 5E-2    >= bar ( )      , QAh6 ( )    + R       ]      )    <= ZXH7E     )      , ZXH7E   || R       ;
   """
		expect = """Type mismatch in expression: ArrayCell(R, [BinExpr(+, IntegerLit(0), FuncCall(readInteger, [BinExpr(::, Id(R), FuncCall(bar, []))]))])"""
		self.assertTrue(TestChecker.test(input, expect, 401))

	def test_402(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  S , s  : boolean   ;
  K2r , S , b , Yl  : array [ 97_8 ] of integer    ;
   Z : function string   ( ) { s , c  : string   ;
  do { }  while ( c   * Z ( K2r   - foo ( )       )       ) ;
   }    WXo , u  : string   = printString ( )     :: ( printInteger ( 9_03_044      )     :: "\\"\\f"      )     , - foo ( )        ;
   K2r : function void ( ) inherit HR { preventDefault ( ) ;
  while ( { u   - K2r [ 0    != Z ( )       ]       , K2r [ - 0.e+3        ]      }       ) if ( u    :: u   > foo ( )      ) { }       U  : auto  ;
  }    Ni : function string   ( inherit out eR : array [ 8_681080 ] of integer     , inherit R : integer     ) inherit foo { super ( { }  , 6_7_7 ) ;
  continue ;
   }    """
		expect = """Redeclared Variable: S"""
		self.assertTrue(TestChecker.test(input, expect, 402))

	def test_403(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  m , u  : string   ;
  vGUc , bar , G  : auto  ;
   """
		expect = """Invalid Variable: vGUc"""
		self.assertTrue(TestChecker.test(input, expect, 403))

	def test_404(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  w1W , GE  : array [ 0 ] of float    = foo ( )    - w1W      , 0E+0    <= 7_0_4E+87       ;
  T : function boolean   ( ) inherit foo { super ( ) ;
  }    XV , Ak3 , b , rW , W  : string   ;
   U  : auto  ;
   foo  : auto  ;
   A , f  : boolean   = ! { }        , A      ;
   M3 : function auto  ( a : auto    ) inherit foo { super ( ! GE [ ( ""     :: f   || f      )    :: ""       ]       ) ;
  }    """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 404))

	def test_405(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  M  : array [ 0 , 6 ] of float    = ! bar ( )        ;
  M  : auto  = M   == { }        ;
   """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 405))

	def test_406(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Y , Wk  : float   ;
  lF5wr : function void ( a : array [ 0 , 0 , 225_23 , 593_6 ] of boolean      ) { }    """
		expect = """No entry point"""
		self.assertTrue(TestChecker.test(input, expect, 406))

	def test_407(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  V  : float   = V [ ""     :: "\\""       ]    == readString ( { bar ( V    :: .E+3    >= foo ( )      , ""     :: ""      )    <= V [ m   - bar       ]      , V     , V   < ( V [ { V   >= true      }     && { ( foo ( )      )   > 511_80_03_4231.2E-052969      }        , "\\n\\\'"      , V   % V       ]      )     }     && { foo ( )    < V     , readFloat ( )      }        )      , .15E-1    > V     , { }     && { { true    * 4       , 11.7E-32      , V [ 0    == .E-8987      , bar ( printBoolean ( )      , V [ V    :: V     , ""     :: "\\"\\\'"       ]    > V     )    && foo ( )        ]      , ( 0.      )     }     || V      }         ;
  v : function array [ 0 ] of boolean    ( ) { _ , C  : auto  ;
  continue ;
   i  : auto  ;
  }    """
		expect = """Type mismatch in expression: ArrayCell(V, [BinExpr(::, StringLit(), StringLit(\\"))])"""
		self.assertTrue(TestChecker.test(input, expect, 407))

	def test_408(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  si  : integer   ;
  lN : function void ( inherit Lf : auto   , inherit out qln : integer     ) { }    """
		expect = """No entry point"""
		self.assertTrue(TestChecker.test(input, expect, 408))


	def test_410(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  F  : integer   = foo ( )    || 0.6        ;
  foo : function void ( ) { PtR  : array [ 0 ] of integer    = F   * printFloat ( bar ( PtR [ F   % bar ( 0      , PtR [ F   || F       ]    > PtR [ bar ( )    || bar ( ( F     )   < printBoolean ( )      , { }       )        ]      )       , "\\f"     :: bar ( ( PtR    :: bar ( )      )    :: "\\b"      , false    >= F     )      , ( F     )      ]      , PtR [ printInteger ( )    / 0e93       , - PtR      , ( F    :: ""      )   == 0       ]      )      , F   >= ( F     )     )        ;
  { { }   break ;
   }   }    """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 410))

	def test_411(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  m  : array [ 23587 , 490 ] of integer    ;
  O : function void ( ) inherit super { super ( ) ;
  m [ ( m [ m    :: m      ]      )   <= m [ O ( )    - printString ( )       , super ( ! { }        )    >= m      ]      , - m [ ( m     )   <= m [ - 0E07        ]      , 0.3e9    + m [ m   + m       ]        ]        ]   = ! m      ;
   gn  : auto  = gn    :: m [ gn   == ( 4_558_67_6359914_109_2394      )      ]       ;
  }    sZ  : auto  = { }        ;
   m : function void ( ) inherit foo { super ( ) ;
  }    """
		expect = """Type mismatch in expression: ArrayCell(m, [BinExpr(<=, ArrayCell(m, [BinExpr(::, Id(m), Id(m))]), ArrayCell(m, [BinExpr(-, FuncCall(O, []), FuncCall(printString, [])), BinExpr(>=, FuncCall(super, [UnExpr(!, ArrayLit([]))]), Id(m))])), UnExpr(-, ArrayCell(m, [BinExpr(<=, Id(m), ArrayCell(m, [UnExpr(-, FloatLit(0.0))])), BinExpr(+, FloatLit(300000000.0), ArrayCell(m, [BinExpr(+, Id(m), Id(m))]))]))])"""
		self.assertTrue(TestChecker.test(input, expect, 411))

	def test_412(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  b  : array [ 0 , 0 ] of float    = b   != ( b [ b [ b   || { }         ]       ]      )    :: b      ;
  w1G : function void ( inherit out b : array [ 70_78_7_9732_66_9_1_2432 , 0 , 0 ] of boolean      ) inherit foo { super ( { }  ) ;
  }    """
		expect = """Type mismatch in expression: BinExpr(||, Id(b), ArrayLit([]))"""
		self.assertTrue(TestChecker.test(input, expect, 412))

	def test_413(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  DVc  : array [ 7_1 , 173_173 , 0 ] of float    ;
  y  : auto  = DVc [ bar ( )    % 0e83        ]    || DVc [ y   + true       , 57_1_693.972e+058     :: ""       ]        ;
   """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 413))

	def test_414(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  T  : array [ 0 , 6624 , 0 , 4_4 ] of float    = ""     :: T [ ! bar ( printFloat ( )      , ( T     )   >= T     )        ]       ;
  R : function void ( inherit out U : boolean    , inherit out DHgp : array [ 88 ] of boolean     , inherit k6FK : integer    , Ib : auto    ) { }    """
		expect = """Type mismatch in expression: FuncCall(printFloat, [])"""
		self.assertTrue(TestChecker.test(input, expect, 414))

	def test_415(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  h  : auto  = "\\"\\r"     :: 0.    >= .E-15       ;
  ZDq  : auto  ;
   CbY  : float   ;
   """
		expect = """Type mismatch in expression: BinExpr(::, StringLit(\\"\\r), BinExpr(>=, FloatLit(0.0), FloatLit(0.0)))"""
		self.assertTrue(TestChecker.test(input, expect, 415))

	def test_416(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  t4  : auto  = t4 [ t4    :: t4      ]    - printInteger ( t4 [ t4    :: foo ( )    - t4      , bar ( )     :: ""       ]      )        ;
  J : function void ( t4 : string     ) { }    """
		expect = """Type mismatch in expression: ArrayCell(t4, [BinExpr(::, Id(t4), Id(t4))])"""
		self.assertTrue(TestChecker.test(input, expect, 416))

	def test_417(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Lql  : float   ;
  Y : function void ( ) { bar ( ( ""     :: Lql     )    :: Lql     , Lql   != { }       )  ;
   }    UW : function array [ 0 , 67_7212_51_86_17_5_10 ] of float    ( ) { q  : float   ;
  VW8R , bar , zp  : integer   = ( readBoolean ( ( 9673_1    * VW8R      )     )      )   + bar ( )       , - 0       , super ( )    <= 0       ;
  }    sl  : float   = ! UW ( 2    > .63E-7      )        ;
   """
		expect = """Type mismatch in expression: BinExpr(::, StringLit(), Id(Lql))"""
		self.assertTrue(TestChecker.test(input, expect, 417))

	def test_418(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  wG , oWC  : array [ 0 , 0 , 6_8043 ] of float    = printString ( )    > printInteger ( wG [ ( ( foo ( )      )   > oWC     )     , 0E6    < 0       ]      )      , ! d ( )       , oWC   && wG [ 0    >= wG     , wG   || oWC      , 0E+732    > ( "\\\\"      )    :: foo ( ( 3_0e346871    >= ( 648_77      )     )     , "\\\'"     :: oWC     )       ]       , "\\n\\f"     :: wG   <= 3_099e+4       ;
  Z : function array [ 0 ] of boolean    ( ) inherit foo { foo ( )  ;
  }    P : function void ( ) inherit bar { super ( ) ;
  }    wG : function auto  ( ) inherit foo { super ( ) ;
  }    """
		expect = """Type mismatch in expression: FuncCall(printString, [])"""
		self.assertTrue(TestChecker.test(input, expect, 418))

	def test_419(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  G  : float   = 0    * G       ;
  G  : integer   ;
   NqP , bar , I  : integer   ;
   o : function float   ( ) { break ;
   G  = printString ( foo ( readBoolean ( readBoolean ( foo ( )    - G      )    <= 0e681      )      , G [ NqP   % I      , NqP    :: bar     , o [ bar   >= zRJBb     , bar ( NqP     , NqP     )    - .01E-4       , 0.858    <= B      ]       ]     :: ""      )      )    + ( bar   >= 96550_22187_4_87554_141638_9670_29_50.e411      )      ;
   CR , T , NqP  : auto  ;
  XijsX , an  : float   ;
  }    """
		expect = """Redeclared Variable: G"""
		self.assertTrue(TestChecker.test(input, expect, 419))

	def test_420(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  t , D  : array [ 0 , 0 ] of boolean    = 110_8    != ( bar ( )     :: - ( ( t     )     )      )    :: bar ( D     , 0.1e+3403976    >= 1      )      , { ! t      , D   >= t     }     || ( t     )       ;
  A4 : function void ( ) inherit super { super ( ) ;
  }    """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 420))

	def test_421(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  P  : auto  ;
  P  : array [ 2_9 , 17_8_111_8_0 , 0 ] of boolean    = P   / readBoolean ( foo ( printInteger ( bar ( )      )      , foo ( 3      , - P     :: ""      )     :: ( foo ( )     :: ""      )     )    > P [ 0E+481964    < P [ ""     :: ( P    :: ""      )      ]       ]      )        ;
   """
		expect = """Invalid Variable: P"""
		self.assertTrue(TestChecker.test(input, expect, 421))

	def test_422(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  l , R  : string   ;
  Pa , j , YKn  : array [ 3_145 ] of integer    = 0.9    + YKn      , 3    <= Pa [ YKn   <= YKn     , l    :: R     , bar ( Pa     , j     )    + printInteger ( )        ]      , 0    * R       ;
   """
		expect = """Undeclared Identifier: YKn"""
		self.assertTrue(TestChecker.test(input, expect, 422))

	def test_423(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  V , c , mFl , f , eyc , UB3 , J  : string   ;
  w , GJFRj  : array [ 270 ] of boolean    = eyc    :: V     , 818    >= bar ( )     :: ( ( eyc     )     )   <= ( bar ( )     :: f     )      ;
   B : function auto  ( inherit NeQ : string     ) { s3weglxA  : array [ 738_729 , 422 , 2_6 ] of integer    = c    :: 995e-669    < s3weglxA [ ( ( ( GJFRj   != false      )     )     )   % foo ( UB3     , ! bar ( )       )        ]      , ! c      , w [ eyc   * GJFRj       ]     :: ""      , w [ c   || ( w [ - f       ]      )     :: w [ 0    != UB3      ]    >= B ( V    :: readInteger ( )    / s3weglxA      )       ]      , - 0.e+4        ;
  }    """
		expect = """Type mismatch in Variable Declaration: VarDecl(w, ArrayType([270], BooleanType), BinExpr(::, Id(eyc), Id(V)))"""
		self.assertTrue(TestChecker.test(input, expect, 423))

	def test_424(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  WoW  : auto  = foo ( )    > 0.e63       ;
  h , f , pW  : array [ 689 ] of float    ;
   ygy  : array [ 0 , 0 ] of string    ;
   """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 424))

	def test_425(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  qN , u , nc , EAIR7 , k9UDB  : auto  ;
  m : function array [ 6 , 0 , 0 , 0 , 0 ] of float    ( out y : auto   , out y : integer    , inherit x : array [ 3_02 , 0 , 0 ] of float      ) inherit bar { preventDefault ( ) ;
  H , OT , AZ , wzD  : array [ 0 , 0 ] of float    ;
  }    """
		expect = """Invalid Variable: qN"""
		self.assertTrue(TestChecker.test(input, expect, 425))

	def test_426(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  j , l , Ytkz , j  : array [ 1_53_8985_455_37 ] of float    ;
  ro : function void ( x : auto    ) inherit bar { super ( { }       ) ;
  }    b : function auto  ( inherit out u : integer     ) { }    Ytkz : function auto  ( ) inherit foo { super ( ) ;
  }    """
		expect = """Redeclared Variable: j"""
		self.assertTrue(TestChecker.test(input, expect, 426))

	def test_427(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  D7FL  : array [ 0 ] of string    = - D7FL       ;
  iE : function array [ 0 , 1 ] of integer    ( ) { }    """
		expect = """Type mismatch in expression: UnExpr(-, Id(D7FL))"""
		self.assertTrue(TestChecker.test(input, expect, 427))


	def test_429(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  zSCD , lJE , A  : auto  = ( A   != 33_1      )   / 37       , readInteger ( )     :: ( ""     :: true      )     , ! lJE       ;
  K  : auto  ;
   """
		expect = """Undeclared Identifier: A"""
		self.assertTrue(TestChecker.test(input, expect, 429))

	def test_430(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  bar , X , t , T , AtK , qefZ  : array [ 7 ] of string    ;
  H : function array [ 3_33_6_045 ] of string    ( ) inherit foo { super ( ) ;
  WSn , d  : array [ 395050 ] of string    = H ( 3    > t     )    == false     :: t     , 97    >= ( 0e-0      )      ;
  Mu , b , O , CY  : array [ 79_1_5 , 0 ] of string    ;
  }    """
		expect = """Redeclared Variable: bar"""
		self.assertTrue(TestChecker.test(input, expect, 430))

	def test_431(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  T , aLK1 , tqhs  : auto  ;
  YP : function float   ( inherit out u : auto    ) { break ;
   }    YP , aLK1  : array [ 238_68_8 ] of boolean    = bar ( )    >= aLK1 [ YP    :: YP [ "\"     :: ""      , false       ]       ]      , { tqhs   - printBoolean ( YP [ printString ( )    + aLK1      , { }     && readBoolean ( super ( )    / bar ( )       )        ]      )       , YP     , tqhs     }     <= 0     :: ! tqhs       ;
   FfHd , c  : string   = - ( 0      )      , foo ( tqhs     , YP ( T     )     :: ""      )       ;
   ji : function auto  ( inherit p : auto   , inherit out V : array [ 554_35_0_5_6 ] of string     , inherit out W : integer     ) { }    T : function boolean   ( ) { }    CxDtp  : auto  = 96    <= 0       ;
   C : function void ( ji : array [ 7_0_437_45 , 5_8 ] of string     , out z6Km : auto   , d : array [ 0 , 2_35_15_7 , 5 ] of integer      ) inherit T { }    E : function array [ 8403 , 0 , 0 ] of string    ( ) { }    """
		expect = """Invalid Variable: T"""
		self.assertTrue(TestChecker.test(input, expect, 431))

	def test_432(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  vr , F , U  : integer   = vr    :: vr     , 1_6    >= 0      , vr   / bar ( bar ( U    :: ""      , bar ( printInteger ( )      , U     )    > F [ vr   != .98e2      , - F      , ( { }       )   || vr       ]      )      , ( U [ - 0        ]    >= U     )   >= ( vr [ U    :: bar ( )      , 39299E+380    > ( U    :: 6    - ( readInteger ( )      )      )     , 0e27    < vr [ vr [ ! { }         ]     :: F     , ""     :: ""      , "\\\'"     :: ! { }        , vr    :: readInteger ( )       ]      , F   < foo ( bar ( )     :: ""      , U    :: U     )      , - foo ( )       , ( vr     )   < foo ( )       ]      )     )        ;
  U : function auto  ( ) { while ( ! { 8116.    >= vr     }        ) break ;
     _x  : boolean   ;
  break ;
   }    """
		expect = """Type mismatch in expression: BinExpr(::, Id(vr), Id(vr))"""
		self.assertTrue(TestChecker.test(input, expect, 432))

	def test_433(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  w  : auto  ;
  C9 , Fi  : array [ 264_7 , 1 , 9_044604_38523 ] of string    ;
   p9 : function string   ( ) inherit foo { super ( ) ;
  }    """
		expect = """Invalid Variable: w"""
		self.assertTrue(TestChecker.test(input, expect, 433))

	def test_434(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  k  : auto  = - 74_89_7E-9        ;
  C  : auto  ;
   """
		expect = """Invalid Variable: C"""
		self.assertTrue(TestChecker.test(input, expect, 434))

	def test_435(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  foo , u , k  : auto  ;
  bar : function void ( inherit q : string    , inherit out b : integer    , inherit out a : array [ 0 , 0 , 0 ] of integer      ) inherit foo { super ( "\\f\\b" , 0 , { }  ) ;
  }    """
		expect = """Redeclared Variable: foo"""
		self.assertTrue(TestChecker.test(input, expect, 435))

	def test_436(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  XO  : auto  ;
  C7C : function void ( fP : string     ) { do { continue ;
   }  while ( XO   && .96E+9       ) ;
   if ( ""     :: XO [ XO [ readBoolean ( ! ( { }       )      )    - XO       ]     :: C7C ( )       ]      ) { super ( )  ;
   }   else continue ;
     }    Lf , XO  : float   = XO [ foo ( bar ( )      , Lf    :: ( ""     :: bar ( )    > Lf     )     )    == ( XO     )     , Lf    :: bar ( )       ]    || { ( ( Lf     )     )   * Lf      }         ;
   """
		expect = """Invalid Variable: XO"""
		self.assertTrue(TestChecker.test(input, expect, 436))

	def test_437(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  u , readFloat  : boolean   = 0.    >= u    :: "\\r"      , u   - 6        ;
  T2G  : integer   = foo ( ""     :: "\\f"      , u    :: T2G     )       ;
   readFloat : function boolean   ( ) { U  : boolean   = T2G [ readFloat      ]     :: printBoolean ( )    <= .1E-4       ;
  }    """
		expect = """Type mismatch in expression: BinExpr(>=, FloatLit(0.0), Id(u))"""
		self.assertTrue(TestChecker.test(input, expect, 437))

	def test_438(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  _M  : array [ 0 , 4 ] of string    ;
  w : function void ( ) { for ( _M [ _M   + .E-93        ]   = printInteger ( )      , { }     - 34495_5_8_8.       , _M   / _M      ) return ( 0      )   / 627e+87       ;
     }    """
		expect = """Type mismatch in expression: BinExpr(+, Id(_M), FloatLit(0.0))"""
		self.assertTrue(TestChecker.test(input, expect, 438))

	def test_439(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  O , ot7  : auto  ;
  AeO04  : array [ 7_1573086 , 0 ] of boolean    = ot7   - ( 876_15E8      )       ;
   """
		expect = """Invalid Variable: O"""
		self.assertTrue(TestChecker.test(input, expect, 439))

	def test_440(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  KKx  : array [ 2_4_5 ] of string    ;
  heZtj : function void ( out r : auto   , out F : auto   , inherit KKx : auto   , inherit out Ca : auto    ) { break ;
   An  : boolean   ;
  }    """
		expect = """Must in loop: BreakStmt()"""
		self.assertTrue(TestChecker.test(input, expect, 440))

	def test_441(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  u  : float   = { }     && u [ .e+39       ]        ;
  u , readInteger  : auto  = { }     <= 581137_1_13.e-17      , ""     :: 0    == 6789342       ;
   Hw : function auto  ( ) inherit readFloat { super ( ) ;
  L  : string   ;
  }    B  : array [ 0 , 0 , 161_593_3_84_20651_7 , 0 , 41 ] of boolean    = ( foo ( B [ - 0        ]      , readInteger    :: Hw ( )      )      )   + u      , ! ( 0    <= printFloat ( u   < .62E-0      )      )       ;
   KC  : array [ 0 ] of boolean    ;
   j : function void ( ) inherit preventDefault { preventDefault ( ) ;
  }    ja : function void ( inherit siu : array [ 0 , 5 ] of string      ) inherit j { super ( { readInteger   + B      }  ) ;
  }    TJ : function void ( ykJ3z : auto   , out C : array [ 0 ] of string      ) { r , RXIk , B , D_IZ7  : boolean   ;
  break ;
   }    """
		expect = """Type mismatch in expression: ArrayCell(u, [FloatLit(0.0)])"""
		self.assertTrue(TestChecker.test(input, expect, 441))

	def test_442(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  M  : array [ 0 ] of integer    ;
  u : function void ( ) inherit foo { super ( ) ;
  continue ;
   }    """
		expect = """Type mismatch in expression: """
		self.assertTrue(TestChecker.test(input, expect, 442))

	def test_443(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  qq , zu , Q  : auto  = foo ( )    + foo ( )       , Q [ { }     || printInteger ( printBoolean ( zu   >= qq     )      )       , bar ( )     :: qq     , qq   % 29        ]     :: foo ( bar ( zu   == U     , printString ( )    < 0.E92      )      , Q [ ! Q      , "\\""     :: Q      ]    < ( .E9      )    :: bar ( foo ( )      , foo ( qq     , foo ( )     :: zu     )    < qq     )      )      , ! Q       ;
  HNT5 , G , C , foo  : array [ 0 , 730 ] of float    = { ( 4e13    > ( foo     )     )   - 4.08E+0       , HNT5     }     || qq      , G   < preventDefault ( )     :: HNT5     , foo [ .e50    >= HNT5 [ ""     :: ""      , 0.54    % 0       , - foo ( 2398    >= .91E-0      , C    :: qq     )       , HNT5   + foo [ 0.1    <= ( foo [ ( zu     )   >= ( readInteger ( )      )     , true    * qq      , ( - readInteger ( ""      , { }     != { }       )       )     , ( "\\\'"     :: - bar ( )       )    :: zu      ]      )      ]        ]      , - 0.1221        ]    % true       , - ( C [ - foo ( )        ]      )       ;
   """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 443))

	def test_444(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  foo  : auto  = foo    :: foo   < ( .e1      )      ;
  foo , p  : auto  ;
   j0 : function void ( ) { F6X  : string   ;
  }    QaBi : function array [ 5574 , 0 ] of boolean    ( ) { }    """
		expect = """Redeclared Variable: foo"""
		self.assertTrue(TestChecker.test(input, expect, 444))

	def test_445(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  _  : array [ 7_3_152 ] of boolean    = "\\\\"     :: { _   - foo ( )       }        ;
  _5  : auto  ;
   _  : array [ 0 ] of boolean    ;
   E : function void ( ) { }    Fp : function void ( ) inherit foo { preventDefault ( ) ;
  { zl , N  : array [ 0 , 0 , 1 , 3 ] of string    ;
  z , ps , D2XF , MwnLj8 , g , ZDek  : array [ 0 ] of integer    = Fp ( ( Fp ( D2XF   / b      )    > .E+475      )   && { }        )     :: printString ( )      , 0    > 933_15      , bar ( )    || { }       :: "\\n\\""      , ps   * b      , ! zl      , MwnLj8   || { 89    / ZDek      }         ;
  }   b  = MwnLj8   >= 9674_17_589708      ;
   }    """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 445))

	def test_446(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  G  : array [ 5_753 , 9049 ] of boolean    ;
  BN : function array [ 7 ] of float    ( out Q_LvF : auto    ) { kb , Z  : string   ;
  }    """
		expect = """No entry point"""
		self.assertTrue(TestChecker.test(input, expect, 446))

	def test_447(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Ih  : auto  = ( Ih     )   + 0        ;
  s_ : function array [ 91_6_0 ] of string    ( ) inherit foo { super ( ) ;
  }    """
		expect = """Type mismatch in expression: """
		self.assertTrue(TestChecker.test(input, expect, 447))

	def test_448(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  K , F , zE , Ua  : array [ 9_37_225_5 ] of integer    ;
  U , K  : array [ 0 ] of string    = readString ( )     :: Ua     , ! { }         ;
   s : function string   ( ) { return 1.e9    + 29_7_77_707722.13       ;
   }    """
		expect = """Type mismatch in expression: BinExpr(::, FuncCall(readString, []), Id(Ua))"""
		self.assertTrue(TestChecker.test(input, expect, 448))

	def test_449(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  r  : auto  = - ( 53_2e-94      )       ;
  bar  : auto  ;
   """
		expect = """Redeclared Variable: bar"""
		self.assertTrue(TestChecker.test(input, expect, 449))

	def test_450(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  zA , Q , g  : array [ 78724_7_3 , 0 ] of string    ;
  o , R  : integer   ;
   Jx : function void ( ) inherit printBoolean { super ( ) ;
  if ( ! { }        ) return ;
   else { }     Y  : string   = Q [ Jx ( )    % 1        ]    != R      ;
  }    """
		expect = """Type mismatch in expression: """
		self.assertTrue(TestChecker.test(input, expect, 450))

	def test_451(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Kgv_ , wf  : auto  ;
  wf  : array [ 2 ] of float    = ( foo ( )    && { Kgv_   < bar ( wf [ Kgv_   - bar ( )        ]      , wf [ Kgv_   == wf      ]     :: Kgv_   < Kgv_     )      }        )      ;
   b : function void ( ) { e , wf , n  : array [ 0 , 0 ] of boolean    ;
  p68VJ  : integer   ;
  }    """
		expect = """Invalid Variable: Kgv_"""
		self.assertTrue(TestChecker.test(input, expect, 451))

	def test_452(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Ch , R , i  : auto  = ! { }        , - Ch [ i   || Ch [ bar ( 0    > R    :: "\\r"      , R     , - 6_8.99E-76       )    / 2047       , bar ( )    + i      , foo ( )    >= R    :: ""       ]        ]       , i    :: Ch      ;
  nb : function float   ( inherit rjJAN : array [ 6_5_8693_3_9 , 9529_6129070 ] of integer     , out V : auto    ) inherit a { super ( { Ch   && i      , i    :: ( 27    >= R    :: readString ( ""     :: Ch     )      )     , Ch     }  , { 0.e-7    % Ch      , .E37      , foo ( )      }       ) ;
  qpc , bE  : auto  ;
  }    q  : array [ 3_1 , 0 , 96 , 7_36381 , 25 ] of float    = ! { Ch   % .2616e+0192       , q     , ( .E+7425      )     , ( ( bar ( i    :: foo ( ( j [ Zy   && q       ]     :: ""      )     , q   <= readFloat ( )      )      , foo ( )    < bar ( Ch     , foo ( )      )      )     :: ( Ch     )     )     )     }        , 0.45E970    < R      ;
   """
		expect = """Type mismatch in expression: UnExpr(!, ArrayLit([]))"""
		self.assertTrue(TestChecker.test(input, expect, 452))


	def test_454(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  p , BZ  : string   = p [ ! foo ( )       , ! p       ]    % foo ( )       , BZ      ;
  Ze  : auto  ;
   B8 : function void ( inherit out a : array [ 6_2037_28_0 ] of integer     , inherit out b : array [ 0 ] of boolean     , inherit b : boolean     ) inherit foo { super ( { }  , { }  , false ) ;
  }    """
		expect = """Type mismatch in expression: ArrayCell(p, [UnExpr(!, FuncCall(foo, [])), UnExpr(!, Id(p))])"""
		self.assertTrue(TestChecker.test(input, expect, 454))

	def test_455(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  io , B  : array [ 735 ] of float    = io    :: io     , B [ ( V   > io     )     , ! printBoolean ( io    :: B     )        ]       ;
  eid : function array [ 0 , 0 ] of boolean    ( ) inherit foo { super ( ) ;
  }    """
		expect = """Type mismatch in expression: BinExpr(::, Id(io), Id(io))"""
		self.assertTrue(TestChecker.test(input, expect, 455))

	def test_456(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  q  : array [ 0 , 0 ] of string    = 61    >= ( 0      )      ;
  Ug  : array [ 0 , 0 , 5 , 8176_791_8640 , 813810_93 ] of integer    = .E9    - q       ;
   """
		expect = """Type mismatch in Variable Declaration: VarDecl(q, ArrayType([0, 0], StringType), BinExpr(>=, IntegerLit(61), IntegerLit(0)))"""
		self.assertTrue(TestChecker.test(input, expect, 456))

	def test_457(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  SV  : array [ 0 , 0 , 0 , 0 , 0 , 6_613539 , 0 ] of integer    = ! foo ( bar ( )      , SV [ ! ""        ]     :: SV [ - ( bar ( )      )       ]      )       , 4231_771_4_8    % 0        ;
  I : function void ( ) { return SV   % upO ( )       ;
   v  : float   = 91_7e-8    < v      ;
  gk  : array [ 0 ] of integer    ;
  for ( gk  = SV [ bar ( )       ]    / 0.       , SV [ { 0    / I ( )       , v     }     || { I ( )     :: gk     , v    :: ( I ( )     :: gk [ v   <= v      ]      )     }        , ""     :: { SV [ gk    :: SV      ]    - SV      , SV     , SV [ printInteger ( gk     )    % 0       , v   || { }         ]      }     || { }         ]      , foo ( I ( )      , SV [ - ieAdVbA      , ( printFloat ( ( 239e-4      )     , v   <= v     )      )   > 6_0_9E6      , gk   + v       ]     :: ""      )    == ( SV [ "\\t\\r\\r"     :: gk [ 836_869      , readInteger ( false    * 0       )    >= .E6       ]      , printString ( bar ( foo ( gk     , ! v     :: foo ( )    != { }       )      , printInteger ( 71_4_74_7      )    > ( 0E+8      )     )     :: v     )    && { ( 83E+62964      )   % v      , foo ( )      , v     }        , gk   * 0        ]      )     ) SV  = - printString ( )       ;
     t  : array [ 5_29925 ] of string    ;
  }    Fx , ZYpX , T  : array [ 99_86004 ] of boolean    = bar ( )      , 0    != T [ foo ( )    * 2_25       , ! { }        , Fx   != printString ( )       ]      , T   > 4_8       ;
   c  : auto  = printBoolean ( )     :: ""       ;
   T : function array [ 0 ] of string    ( ) inherit I { super ( ) ;
  SV  = Fx   > ( printString ( )      )     ;
   }    """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 457))

	def test_458(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  r , ow2 , printFloat  : auto  ;
  foo , x4  : array [ 0 ] of string    ;
   """
		expect = """Invalid Variable: r"""
		self.assertTrue(TestChecker.test(input, expect, 458))

	def test_459(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  V , nVr0bN  : auto  ;
  nVr0bN : function auto  ( ) inherit bar { super ( ) ;
  }    """
		expect = """Invalid Variable: V"""
		self.assertTrue(TestChecker.test(input, expect, 459))

	def test_460(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  E  : float   ;
  i , Q , A , b  : auto  = E ( )    > E     , ( b    :: ( false    <= 5_2301e013     :: A     )     )    :: E     , A   - E      , E   && printFloat ( 9_37832_99104_62_9      )        ;
   """
		expect = """Type mismatch in expression: FuncCall(E, [])"""
		self.assertTrue(TestChecker.test(input, expect, 460))

	def test_461(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  e  : auto  ;
  aT : function void ( ) inherit foo { super ( ) ;
  }    x  : auto  ;
   """
		expect = """Invalid Variable: e"""
		self.assertTrue(TestChecker.test(input, expect, 461))

	def test_462(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Imq , Q , E  : boolean   ;
  T  : auto  ;
   """
		expect = """Invalid Variable: T"""
		self.assertTrue(TestChecker.test(input, expect, 462))

	def test_463(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  S  : array [ 3 ] of integer    ;
  e5  : boolean   = printString ( bar ( e5     , e5     )     :: S [ ! e5       ]      )    > S [ ! e5      , 6020    < e5     , ! { }        , S   != S [ 0    + S       ]      , e5   - readBoolean ( )        ]       ;
   """
		expect = """Type mismatch in expression: FuncCall(bar, [Id(e5), Id(e5)])"""
		self.assertTrue(TestChecker.test(input, expect, 463))

	def test_464(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  z , tJ  : auto  ;
  Jd5S : function void ( ) { }    Ep_ : function array [ 0 , 586_2720_0858144_8 , 0 , 59_6_73 , 0 ] of float    ( out j : auto    ) { }    s : function auto  ( out vWLLj : array [ 0 , 0 , 0 ] of float      ) inherit Jd5S { preventDefault ( ) ;
  }    """
		expect = """Invalid Variable: z"""
		self.assertTrue(TestChecker.test(input, expect, 464))

	def test_465(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  I  : array [ 7_25 ] of string    = - foo ( ( I   == I     )     , printInteger ( 13_1      )    <= I [ I    :: bar ( )       ]     :: "\\t"      )        ;
  e , tU , foo  : float   = foo     , bar ( 0      , { }       )    + e      , 3_8    > foo      ;
   preventDefault : function array [ 0 ] of float    ( ) { }    """
		expect = """Type mismatch in expression: BinExpr(==, Id(I), Id(I))"""
		self.assertTrue(TestChecker.test(input, expect, 465))

	def test_466(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  Ur , dUNI3 , WN , P38R  : auto  ;
  Wl  : array [ 8_9_1049 , 0 , 0 , 286 , 20 , 83_3_2_13040_5_959678441 , 3 , 80_4 ] of string    = Wl   <= dUNI3      ;
   """
		expect = """Invalid Variable: Ur"""
		self.assertTrue(TestChecker.test(input, expect, 466))

	def test_467(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  VT  : integer   = ( preventDefault ( )      )   <= preventDefault ( )       ;
  f2 : function void ( ) inherit foo { preventDefault ( ) ;
  }    """
		expect = """Type mismatch in expression: FuncCall(preventDefault, [])"""
		self.assertTrue(TestChecker.test(input, expect, 467))

	def test_468(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  R6  : auto  ;
  U : function void ( inherit out a : auto    ) inherit foo { super ( R6     ) ;
  }    """
		expect = """Invalid Variable: R6"""
		self.assertTrue(TestChecker.test(input, expect, 468))

	def test_469(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  h , P6 , HmA , E  : array [ 0 , 0 ] of float    ;
  _fm0Tl : function void ( LxM : float     ) { }    A_j , _fm0Tl , K  : array [ 4_084_8_87 ] of string    = ! _fm0Tl      , E [ ! E [ 7_94    < ( ( 9_7_1_27_68_25072E-754091      )     )     , printBoolean ( { ! _fm0Tl      , { }       }       )    - .e7       , 0       ]       , h   == 6       ]    < 0      , foo ( 0      , h     )    < 930     :: HmA      ;
   """
		expect = """Type mismatch in expression: UnExpr(!, Id(_fm0Tl))"""
		self.assertTrue(TestChecker.test(input, expect, 469))

	def test_470(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  i , fi , b  : array [ 0 , 4 ] of float    ;
  OFMv : function integer   ( ) inherit bar { super ( ) ;
  _ , Z  : auto  = super ( )    - 279_8_412_925196       , readString ( ""     :: 4120_89_4_2_2_2_6_85    > foo ( 90      , ""     :: ! fi      )      )    * x       ;
  Z , bm , S , A , kVVSM , S  : auto  ;
  }    """
		expect = """Type mismatch in expression: """
		self.assertTrue(TestChecker.test(input, expect, 470))

	def test_471(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  NN , IYkD , UJ , y_g , Ye8 , ws , s , oxH , U , B , bar , _  : string   ;
  R : function string   ( ) { }    N : function array [ 902 ] of integer    ( inherit out Ciipt : float    , h : array [ 0 ] of string      ) inherit R { super ( 0E90 , { 32E60    - bar ( bar ( bar     , { }       )      , R ( )      )       , true    != { }       }  ) ;
  }    z : function void ( inherit W : array [ 140_51 , 0 , 5 , 9_37_11_6367 , 0 ] of float     , inherit a : auto    ) inherit foo { preventDefault ( ) ;
  }    """
		expect = """Redeclared Variable: bar"""
		self.assertTrue(TestChecker.test(input, expect, 471))

	def test_472(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  g  : auto  ;
  qKj  : array [ 0 ] of float    ;
   """
		expect = """Invalid Variable: g"""
		self.assertTrue(TestChecker.test(input, expect, 472))

	def test_473(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  i , Z  : auto  ;
  M : function void ( inherit out y : float     ) inherit bar { preventDefault ( ) ;
  { Zyal  : array [ 5_9 ] of integer    ;
  }   for ( Zyal [ 2E+7       ]   = y    :: "\\t"      , ( readFloat ( )      )    :: ( "\\b"     :: Zyal [ Z   <= Zyal [ Zyal [ foo ( Zyal     , 0    < readFloat ( - Z      )     :: Zyal   > 0      )    > Z     , ( Z    :: ""      )    :: ( readInteger ( y   && 0.9e1       )     :: foo ( )      )     , Zyal [ i   % y       ]    >= Z      ]     :: "\\""      , y   == vul ( )       ]       ]    - bar ( 0      , i     )       )     , M ( )    == 5_014      ) return y   + 0       ;
     }    """
		expect = """Invalid Variable: i"""
		self.assertTrue(TestChecker.test(input, expect, 473))

	def test_474(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  q , a  : integer   ;
  bar , a  : float   ;
   printString , aay_ , q  : string   = a [ foo ( a   % printString [ aay_ [ ( { }       )   || aay_      , q   != printBoolean ( )      , 0    * 0        ]     :: ( printString [ ( a   >= ( 3_3      )     )   != { }        ]     :: ""      )      ]      :: q     , printString     )     :: bar ( )    * a      , a   <= ( 0      )      ]    * 0        ;
   n2awp  : array [ 0 ] of string    = ! foo ( 0      , foo ( )     :: printString ( )      )        ;
   ji5 , J  : array [ 0 ] of boolean    = .19E+5    > bar     , - bar       ;
   """
		expect = """Redeclared Variable: bar"""
		self.assertTrue(TestChecker.test(input, expect, 474))

	def test_475(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  u  : array [ 0 , 0 ] of integer    = - u       ;
  vf  : array [ 0 ] of boolean    ;
   """
		expect = """Type mismatch in expression: UnExpr(-, Id(u))"""
		self.assertTrue(TestChecker.test(input, expect, 475))

	def test_476(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  a  : auto  = a    :: a      ;
  w3 : function auto  ( F : auto    ) { }    jS : function float   ( ) inherit readFloat { preventDefault ( ) ;
  }    """
		expect = """No entry point"""
		self.assertTrue(TestChecker.test(input, expect, 476))

	def test_477(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  IA , i  : string   ;
  j : function void ( ) { j ( ( IA     )   > i     )  ;
   C , Y  : array [ 3_9053 , 0 ] of string    = bar ( )     :: foo ( j ( C [ ( 0    > 5_9910_0467      )   && ( C     )      , 0e+21    - ( i     )       ]    == preventDefault ( true      , ""     :: IA     )      )    <= Y     , ! { 0.e3    >= .9e+16      , foo ( foo ( )    == IA     )    >= Y     }       :: ""      )      , i   || printFloat ( printInteger ( Y [ ( ""     :: j ( - IA      )    || j ( )       )    :: i     , { }     && { }         ]     :: .E7      )      )        ;
  }    w88bls , rbHpK  : array [ 0 , 1_5951 , 0 , 4 , 0 , 24_23_39669_85 , 4143 ] of string    ;
   """
		expect = """Type mismatch in statement: CallStmt(j, BinExpr(>, Id(IA), Id(i)))"""
		self.assertTrue(TestChecker.test(input, expect, 477))

	def test_478(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  y , _J  : float   ;
  x  : auto  = bar ( 0      , 0.85    <= foo ( )      )    || _J       ;
   """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 478))

	def test_479(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  vMN , wX , I , N5D  : array [ 0 ] of float    = bar ( )    / 0       , bar ( bar ( vMN     , vMN [ N5D   >= N5D     , bar ( )      , ! N5D      , .037e-8    % N5D       ]      )     :: bar ( )      , bar ( )    <= N5D     )    || foo ( foo ( )      , bar ( )     :: ( I    :: ""      )     )      :: N5D     , ( 64.9e145      )   < ( 0.2      )    :: I     , ! I     :: 0E+1    < bar ( )       ;
  Zco : function auto  ( ) { O , fM  : array [ 5479873 , 769 , 0 ] of boolean    = ! I [ printInteger ( true      )     :: .E-44    >= 0      , ( I     )   - readBoolean ( )        ]       , { ""     :: vMN     , ""     :: ""      }     || I      , - printString ( )        ;
  }    """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 479))

	def test_480(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  y  : array [ 0 ] of float    = 6_57    % y       ;
  readString : function auto  ( inherit l : boolean    , inherit out b : array [ 67_3 ] of float      ) inherit foo { super ( false , { y [ ! printInteger ( y     )        ]      , a    :: foo ( )    != a     , ""     :: "\\b"      }  ) ;
  { li  : float   = li   - 4_50_74.6        ;
  }   X , li , Si , eC , C , b , li  : boolean   ;
  break ;
   }    """
		expect = """Type mismatch in expression: BinExpr(%, IntegerLit(657), Id(y))"""
		self.assertTrue(TestChecker.test(input, expect, 480))

	def test_481(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  N , zuE , f  : auto  = N [ foo ( ( f     )     , bar ( )     :: "\\\\\\\'"      )    <= ( 0E9      )     , ( 9    > 0e8      )   == bar ( ( 4_5_919      )     , zuE    :: f     )      , printString ( foo ( foo ( )      , N    :: zuE [ 3266    / bar ( )       , N   > f     , ! f       ]      )     :: "\\b\\r"      )     :: zuE      ]     :: "\\r"      , bar ( )    <= foo ( ""     :: .1E-59    < bar ( ( ( f     )     )     , { zuE   / 0       , ( 0      )     , foo ( )      }       )      )       ;
  KW : function auto  ( out a : integer     ) inherit foo { super ( 881_9_853 ) ;
  }    ykC  : array [ 1 ] of boolean    ;
   """
		expect = """Type mismatch in expression: ArrayCell(N, [BinExpr(<=, FuncCall(foo, [Id(f), BinExpr(::, FuncCall(bar, []), StringLit(\\\\\\'))]), FloatLit(0.0)), BinExpr(==, BinExpr(>, IntegerLit(9), FloatLit(0.0)), FuncCall(bar, [IntegerLit(45919), BinExpr(::, Id(zuE), Id(f))])), BinExpr(::, FuncCall(printString, [BinExpr(::, FuncCall(foo, [FuncCall(foo, []), BinExpr(::, Id(N), ArrayCell(zuE, [BinExpr(/, IntegerLit(3266), FuncCall(bar, [])), BinExpr(>, Id(N), Id(f)), UnExpr(!, Id(f))]))]), StringLit(\\b\\r))]), Id(zuE))])"""
		self.assertTrue(TestChecker.test(input, expect, 481))

	def test_482(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  wKt  : array [ 0 , 0 , 48_8102 ] of string    ;
  a : function void ( inherit s : auto    ) inherit bar { super ( x    :: ( bar ( )     :: ""      )     ) ;
  t  : float   = t   > wKt [ ( { x   == x     , t   <= 25_20      , wKt   == wKt     , 0    < wKt [ x   > x      ]      }       )   || { }         ]      , 0    <= super ( )       ;
  }    q  : auto  ;
   T : function integer   ( out Q : auto   , a : array [ 7_9_8 ] of boolean     , out P : auto   , a : auto    ) inherit foo { }    """
		expect = """Type mismatch in expression: """
		self.assertTrue(TestChecker.test(input, expect, 482))

	def test_483(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  printInteger , o , u , XfpJ , ul , h , X  : array [ 5 ] of string    ;
  N  : array [ 1 , 0 , 85_7_78484 ] of string    ;
   f : function auto  ( out n8 : array [ 1_90_68 , 705_66 ] of string     , b : array [ 0 ] of string      ) { k , Z  : integer   = XfpJ    :: ""      , .0870E+77    - u       ;
  }    """
		expect = """Redeclared Variable: printInteger"""
		self.assertTrue(TestChecker.test(input, expect, 483))

	def test_484(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  yUl , a3  : string   ;
  r , FE  : array [ 10 , 0 , 0 ] of float    = - foo ( bar ( )      , ""     :: foo ( yUl    :: ""      , 0E8     :: bar ( )      )      )       , ( FE     )   > yUl      ;
   Q , sq  : array [ 2 ] of integer    ;
   t  : array [ 0 , 4 ] of boolean    = foo ( )    < 0       ;
   Q  : boolean   ;
   """
		expect = """Type mismatch in expression: FuncCall(bar, [])"""
		self.assertTrue(TestChecker.test(input, expect, 484))

	def test_485(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  rr , qAZ , qyh , GnB  : auto  ;
  u , X  : auto  = u   == qyh     , qAZ    :: GnB      ;
   zIS : function void ( inherit GnB : integer     ) { }    """
		expect = """Invalid Variable: rr"""
		self.assertTrue(TestChecker.test(input, expect, 485))

	def test_486(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  foo  : integer   ;
  v  : auto  ;
   """
		expect = """Redeclared Variable: foo"""
		self.assertTrue(TestChecker.test(input, expect, 486))


	def test_488(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  jd  : array [ 1 ] of integer    ;
  foo , CcHX3  : auto  = foo   <= ( .E1      )     , { jd     }     && CcHX3       ;
   h : function integer   ( R : boolean    , out h : string     ) { }    B : function void ( ) inherit foo { preventDefault ( )  ;
  }    r : function void ( out X : array [ 0 ] of integer      ) { }    L , bar  : auto  ;
   """
		expect = """Redeclared Variable: foo"""
		self.assertTrue(TestChecker.test(input, expect, 488))

	def test_489(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  printString  : auto  = - printString [ printString   >= readInteger ( )       ]       , ""     :: printString      ;
  printString , U , PzBemOo  : array [ 7_0 , 0 , 5 ] of integer    = ! { }        , printInteger ( )    - PzBemOo      , PzBemOo    :: ( printString   <= 86      )   != readInteger ( )       ;
   a : function auto  ( ) inherit bar { super ( ) ;
  }    """
		expect = """Redeclared Variable: printString"""
		self.assertTrue(TestChecker.test(input, expect, 489))

	def test_490(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  VT  : auto  ;
  preventDefault : function void ( out vI : integer    , inherit out ev : string     ) { }    D , J , Zfy , Ab , N9 , eeT  : auto  ;
   """
		expect = """Invalid Variable: VT"""
		self.assertTrue(TestChecker.test(input, expect, 490))

	def test_491(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  C , s897K , P  : auto  = ""     :: s897K [ s897K   && C      , s897K   || P [ P [ foo ( )      , P   - ( ( P     )     )      , .9089e04    <= P [ s897K   && ( C     )      , "\\n"     :: ""      , readInteger ( )     :: ""       ]       ]    < C [ 0.286e9    > foo ( foo ( s897K     , s897K    :: bar ( bar ( )      , C     )      )      , readFloat ( .924e737      )     :: 0    < C     )       ]       ]       , ( ( ""     :: C     )     )   % foo ( 16      , bar ( )    >= To [ 0.45281e54    >= C    :: s897K     , C   == s897K      ]     :: ""      )        ]      , false    / s897K      , 0    > 0e3      , s897K [ - 0       , - 25_1.e2       , s897K [ readInteger ( { }     || { }        )    * ( printInteger ( )      )       ]      , - 0e6       , ( 5805    > foo ( )      )      ]    / 2        ;
  Y : function auto  ( out a : boolean     ) inherit foo { preventDefault ( ) ;
  }    """
		expect = """Undeclared Identifier: s897K"""
		self.assertTrue(TestChecker.test(input, expect, 491))

	def test_492(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  s  : auto  ;
  T : function void ( out Y : integer    , out C : array [ 0 , 0 ] of string      ) { }    """
		expect = """Invalid Variable: s"""
		self.assertTrue(TestChecker.test(input, expect, 492))

	def test_493(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  _eP5h6EHFU , Lnx  : boolean   ;
  F : function void ( inherit w : float    , out foo : auto    ) { }    w  : array [ 0 ] of string    = printInteger ( )     :: "\\t"       ;
   """
		expect = """Type mismatch in expression: FuncCall(printInteger, [])"""
		self.assertTrue(TestChecker.test(input, expect, 493))

	def test_494(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  p  : auto  = ! { ! { p    :: p [ { }     != p      ]      , p    :: readInteger ( bar ( )    <= p     )    >= "\\r"      , printInteger ( )     :: p [ foo ( p [ p   && foo ( )       , ( foo ( )      )      ]      , p [ readBoolean ( )    % p       ]    && { 6_0_80417_3_95_8    < p     , p     , { }       }       :: 5_6.      )     :: ( p [ p   >= 8_2825_86_7_6_1_46       ]    <= p    :: p     )     , p [ ! p [ p   >= p    :: p      ]        ]    || bar ( 288_3_234      , bar ( )      )        ]      }        , 5    == p     }        , ! { }         ;
  e  : array [ 0 ] of string    = e   <= p      ;
   """
		expect = """Type mismatch in expression: ArrayCell(p, [BinExpr(!=, ArrayLit([]), Id(p))])"""
		self.assertTrue(TestChecker.test(input, expect, 494))

	def test_495(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  _zWl , z  : auto  = foo ( )    || ( z     )      , printInteger ( )    % z [ z   * super ( )       , ( readInteger ( )      )   - 4_9_4_6E+1        ]        ;
  _zWl , mDZY , I  : float   ;
   im , A291p9  : array [ 0 ] of boolean    = im [ - mDZY      , bar ( 0      , foo ( )    >= preventDefault ( - A291p9      )      )       ]    / ( _zWl     )     :: im     , A291p9   && A291p9       ;
   """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 495))

	def test_496(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  eURCrt  : auto  ;
  m  : array [ 0 ] of string    ;
   """
		expect = """Invalid Variable: eURCrt"""
		self.assertTrue(TestChecker.test(input, expect, 496))

	def test_497(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  printString , sJ , R  : integer   ;
  Z : function auto  ( inherit out C : auto    ) { }    nW : function boolean   ( C : auto    ) inherit Z { super ( readBoolean ( )      ) ;
  break ;
   }    """
		expect = """Redeclared Variable: printString"""
		self.assertTrue(TestChecker.test(input, expect, 497))

	def test_498(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  N  : float   = N      ;
  J  : integer   = foo ( )    * bar ( )        ;
   """
		expect = """Type mismatch in expression: FuncCall(foo, [])"""
		self.assertTrue(TestChecker.test(input, expect, 498))

	def test_499(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  PiG  : string   ;
  ev2k  : auto  ;
   pMaL : function auto  ( foo : string    , inherit out L : string    , zT : integer     ) inherit preventDefault { super ( "\\\\\\f\\"\\n\\\'" , "" , 0 ) ;
  }    d : function array [ 0 ] of string    ( ) inherit readString { super ( ) ;
  }    wESl , y , r , W , l  : integer   = ! { - 9_335_36_0.       }        , PiG    :: foo ( )      , PiG    :: PiG     , 31_911e4    / foo ( wESl     , ""     :: bar ( ( 389_2_884E-3      )     , y   < 5_1690_0_7295_7319_9      )      )       , 0.e8    / ev2k       ;
   """
		expect = """Invalid Variable: ev2k"""
		self.assertTrue(TestChecker.test(input, expect, 499))

	def test_500(self):
		input = """foo : function void ( inherit out a : integer , inherit out b : string ) { }  bar : function integer ( inherit out x : integer , inherit out y : boolean ) { }  r , foo , nF , J  : array [ 5_9 , 9 ] of float    ;
  N : function void ( inherit foo : auto   , inherit a : array [ 13_4_7_0_4 , 9 ] of boolean     , inherit out Ldg8 : auto   , inherit out m : array [ 0 ] of boolean      ) inherit foo { y , Z  : integer   ;
  }    R  : integer   ;
   """
		expect = """Redeclared Variable: foo"""
		self.assertTrue(TestChecker.test(input, expect, 500))

