import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_1(self):
		input = """QEQL  : float   ;   R  : auto  = - ! ! KG5_Z_MWN_      >= ! H   + n     * Z   * _    && i0yl   || JSu         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 1))

	def test_2(self):
		input = """BVoPi : function void  ( inherit out S5 : string      ) inherit c_ { }    q : function void  ( ) { F  : array [ 0 ] of integer    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 2))

	def test_3(self):
		input = """Lq : function void  ( inherit out Vve : string     , out Sp : auto    ) inherit fHZE { a4 , D , x  : float   ;  return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 3))

	def test_4(self):
		input = """W4  : array [ 24_82 , 0 ] of float    ;   yS7wbe  : array [ 0 , 1 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 4))

	def test_5(self):
		input = """Gn1 : function array [ 0 , 0 ] of string      ( ) { }    V  : auto  = false    > ! L   - Fl1B     && ! r   / o         ;   z3N , e  : float   ;   FNB , wi  : array [ 0 , 54084_1 , 0 , 0 , 6 ] of float    ;   zC : function array [ 0 ] of float      ( ) inherit Lg { D  : integer   ;  if ( t0   && _    >= Jd ( )      ) return ;     l  : auto  = q    :: - g       ;  Z , Q , St  : boolean   ;  }    Z : function float     ( out xj : integer     , out hy : auto   , inherit b : auto   , inherit out m : auto   , b : array [ 4_2346_688 ] of boolean      , inherit v2 : array [ 0 , 2 ] of integer       ) inherit bWV { while ( ! JB     :: I   - Sq    == E9   && g      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 5))

	def test_6(self):
		input = """wW , G8O , M1qh , GN1 , hP , NId , L  : array [ 5 , 0 , 0 , 0 ] of string    ;   GpK : function array [ 0 ] of integer      ( out p : auto   , out tC : boolean     , o : auto    ) inherit s { if ( ! h      ) { }     u  : array [ 29_574 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 6))

	def test_7(self):
		input = """O , h  : array [ 3_1_51_3_5918_78 ] of boolean     = ! RGf   && cUh    && s   && dq6      == ! o      , { }     != - xRB5EXQ   - Kw    && X   * JQd       :: - _ow    * qAB   % b     + ! FN ( )         ;   c_d : function void  ( inherit t : auto   , out x : auto   , w : integer     , D : auto    ) { K , td  : string    = q   || PT    >= sd   + I2iL      , LLm      ;  }    Z , Ax  : auto  = t   || gk    - ! RS     + i   - g    - ! nO      >= poZ   && Kpy    - Wk   / XeGa     || YX      , h   - ! UeUd        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 7))

	def test_8(self):
		input = """g : function void  ( ) { }    i_s : function void  ( ) { }    N , ai , W , U  : array [ 5 ] of string     = ! I   * y    % sX   && qm       :: ! Yad    >= z   * Ya    + O   * wU     || gc   || T    || Z   && R        , - oy    - ! o     - - WJFn   + R       :: ! ! Zq   - P        , ! kQ   * l     * PkQy   - _vMY    - - x      != jyPAv     , - NZ ( )     == V   || v    + - v     + { }         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 8))

	def test_9(self):
		input = """A , j  : auto  = ! p   && Kwe     - ! l   / e      > kbJy9   + tX1    || NrU    || cy      , - - Go    % nvGj   - _2      > - ! St   || g       :: DQWg   / Yc    - ! it     && - mT    - MX   / c         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 9))

	def test_10(self):
		input = """K6y : function void  ( ) inherit sz { wc  : array [ 43781 ] of integer     = gB0   && Rn     :: u5n ( )       ;  }    d4 , wl  : integer   ;   g3D  : array [ 2_0 ] of string    ;   a : function void  ( inherit out g : auto    ) inherit Z { for ( j = Mji   * P      , ""     :: - f    != lgw   || T      , J   + d     :: t   || k9    < _     ) return ;     oz , p  : auto  = s ( )    < - s      , Sg   % B    == - IZ       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 10))

	def test_11(self):
		input = """s : function void  ( ) inherit b { YQNW  : auto  = c   > ! m     :: ! ur0s    > E ( )       ;  }    kC : function void  ( inherit out jH : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 11))

	def test_12(self):
		input = """y3 : function auto   ( nX : array [ 0 ] of boolean      , inherit out aE : auto   , inherit out b : auto   , out INZV : auto    ) { AtKuA4M  : string    = ! S    <= 0     :: Xp   / wk4FBD       ;  ylP , k , r  : array [ 7 , 59 ] of string    ;  Cz , ch , tsXK , uW , h  : float    = ! dr      , C   * R71X    <= Q   || EF0loN     :: t ( )      , gB   && z    > rm   && y      , A   - jY      , - ow4qWpCl    < - t     :: l   % K       ;  }    cfWxKFZQ : function void  ( out M : auto    ) inherit HR { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 12))

	def test_13(self):
		input = """Ky  : string   ;   bz_lLU  : array [ 0 , 6 ] of string    ;   K , d , JS , VT  : array [ 63 ] of boolean     = - hmgx    || M   - U    || Ex   / H      <= - - cR    / - O       :: - W   / D    / D4   % f      >= - - eeL   - K        , ! _    + ha   + Mc     && - - z      >= ! _R ( )     && bA   - Uk    + EM   * J       :: hyHkD3 ( )    && - m     && ! Cd   || p      <= ie4PEBd     , ! v_    + PPmDYs   - M_8m     % aW   || b    * pV4   / F      <= - X    / NM   || t     + - ! MdL        , - _IP5   && Iup     * ""    % ""       :: a   - K    && - p     / o   - q0    || ph   * liWpa      <= 0    / - fzd     - ! o    + ! TW         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 13))

	def test_14(self):
		input = """RE : function void  ( inherit fN : auto    ) { d  : auto  = B   / C    >= - J     :: - X       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 14))

	def test_15(self):
		input = """E0 : function void  ( ) inherit d7Ff { for ( V = - v      , R   + Htd      , ! OW     :: Lq   * M      ) V ( )  ;     break ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 15))

	def test_16(self):
		input = """Pzdi  : auto  = (Ub :: dsl)   || - gT    || Z3   - rW       :: fqq   + o    - - D9     / - LZc ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 16))

	def test_17(self):
		input = """O  : boolean   ;   k : function boolean     ( out Br : auto   , out G : auto   , inherit p2 : auto   , J : auto   , D : float      ) { if ( ! uWb    >= TJP   && Y     :: _   && vibu0y4p      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 17))

	def test_18(self):
		input = """X  : array [ 8 , 1_866 , 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 18))

	def test_19(self):
		input = """MHxBxOnOI : function array [ 0 , 3_12_602 , 0 , 0 ] of boolean      ( Yl : auto    ) inherit c { KN  : boolean    = s   % J       ;  M  : array [ 0 , 50_95 , 0 , 80_2_42216613 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 19))

	def test_20(self):
		input = """f  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 20))

	def test_21(self):
		input = """N : function void  ( inherit out M1 : array [ 4_8 , 0 , 0 ] of string       ) inherit qG { continue ;   G , UI  : array [ 3 ] of boolean     = ""    < ""      , u   + yD    != SJ   && kH     :: v   % d    >= - dj7       ;  GxiZkyI0 , Y , VDI8  : array [ 474_93_900_5_40_338_3_04_5 , 0 , 322_5_9 , 0 ] of boolean    ;  }    ok : function void  ( out U0T_ : auto   , KA6w : integer     , out J : auto    ) { for ( f = H   + XUO    == y3Q5kZ   * W      , d   / e    >= NJX   - zb      , Z6Z   + KNj    == ! qNK     :: a   % JBa    >= eF   / H      ) continue ;     SQgr  : array [ 4 , 0 ] of float     = gs   + z    <= - fi     :: Q   % nOno    <= k ( )       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 21))

	def test_22(self):
		input = """mF : function void  ( a : boolean     , inherit out MD : auto   , inherit ZJ : auto    ) inherit lV { }    wL , a  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 22))

	def test_23(self):
		input = """YVe : function void  ( inherit S : array [ 6_531 , 8_1772226253_4 , 1562 ] of integer       ) inherit v { do { j , y  : string   ;  }  while ( yy   / s    >= U   / IAliRy      ) ;   }    PZr  : boolean   ;   I , W , Y  : auto  = ! - ! R16      <= nV     , Sr   || h    || s   && aYc     - - e   || H9       :: q7   / e    && Iauvg   / Tg     || A   % O    + ! GD        , ! - py    * l   * S       :: fY ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 23))

	def test_24(self):
		input = """Ei97 : function auto   ( inherit D : boolean     , inherit out mY : auto   , inherit out X : auto   , inherit out a : float      ) inherit a { }    c  : auto  = ! ""     / 8    / 4115      < - q    / NwIQ1m ( )     && e   + Y7dkmo2    && Wr      :: - - WS ( )      >= - G   / Jlw     && - i    - vk9   % q8         ;   M , b , Wi , S  : integer    = - WY   % v     % - UNph    / d0 ( )       :: fSfI ( )    + - efL     - Z   || o    % pq   * u      < ! - c     / ! - sS5        , ! Jc   - S     * - MT    - e     != ! pGC   / u     || K   && iOQeFmL    / Yo ( )        , - CwZ   + y     + - FOn   || I       :: - P   + p0H    - 0        , - ! ! B       :: ! e    + f   && A     && w   % FN    % A   || H         ;   T0  : float    = - I    + r   && N     % ! dD        ;   t , M , GC , vN  : array [ 13 , 971 , 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 24))

	def test_25(self):
		input = """PT  : array [ 0 ] of string    ;   MDDu  : array [ 80 , 398_2759_2_4 , 0 ] of string    ;   lv : function void  ( out PBM : auto    ) { if ( xzIi   && n0      ) continue ;   else break ;     T = - cH      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 25))

	def test_26(self):
		input = """C : function void  ( ) { for ( U = - z     :: uI   * W4    >= - O      , D07hg   != Oa   * B0      , av ( )     :: ci ( )    != k   + D      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 26))

	def test_27(self):
		input = """u : function void  ( out h : array [ 9 ] of float       ) { }    BDMt : function void  ( ) { dW  : auto  = ! CUSHj       ;  for ( yA = E   >= q   / K      , ! U     :: ld   % DV6    > J     , 0    <= k   - Bd13n     :: ! t    < sRE   || J      ) continue ;     continue ;   }    exIm : function void  ( ) { if ( - l     :: v2   + P    != ! o      ) break ;   else Alj ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 27))

	def test_28(self):
		input = """Y : function auto   ( ) inherit up { C , aI  : auto  = - ER    == s   - _jPc     :: U8B   || T    != P   - zg      , - er       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 28))

	def test_29(self):
		input = """P  : auto  = ! i    - YWK   * r     && - x   + KLyJ      >= { }      :: q7 ( )    * ST   || R4    && ! C         ;   d : function auto   ( inherit N : auto    ) { }    Q : function void  ( ) { return a     ;   A0 , x3S , EK  : array [ 0 , 0 , 0 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 29))

	def test_30(self):
		input = """mQgFP6 : function auto   ( ) { do { }  while ( - F    > fx4 ( )      ) ;   OIw  : array [ 0 , 0 , 7_3 ] of boolean    ;  break ;   }    Pt  : array [ 6_4185_32_812_296 ] of integer     = _3g ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 30))

	def test_31(self):
		input = """M , ZkR  : auto  = ! ! _     + - sXR    || ! WM      < - - b    - ! m       :: ! C   * PI    || ! AY      == ! d    + v   + V     || P      , ! ! WE     / false     >= FW   % f    - rW    || Pu4FBD   || Y    + P   + J       :: ! I   - t    + ! j4         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 31))

	def test_32(self):
		input = """Iq : function auto   ( tNHK : array [ 0 ] of string       ) { }    Nf : function auto   ( v : boolean     , inherit out K : auto   , inherit out Ae78 : string     , inherit rC : array [ 0 ] of integer       ) inherit ieVy { }    p  : float    = - vG   - Y     - H   % C    || c   && bw      < L    :: - i ( )     >= - Fw       ;   EM , pBcIeJ , Svb  : boolean    = ! ! gD    - k   * LID        , true    && - U   && p        , ! q    / - _c     - zP   - p    && Cg      :: JD   / w ( )     <= G9_uG5yd   && Kt    * ! jpzgk     * - ! t         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 32))

	def test_33(self):
		input = """v : function auto   ( ) { b  : boolean   ;  B , ZgD  : float   ;  }    R : function void  ( inherit Ye : array [ 0 ] of integer      , inherit out zL0 : auto    ) { }    W : function auto   ( inherit out boF : auto    ) { while ( koSyI   || Yt     :: - J      ) break ;     while ( - XM5     :: 0    < 0      ) TM ( )  ;     rU , a , y  : auto  = v   / FP    < aR   * zQ     :: ! x    >= Mm     , ! Q      , ! fYt    == ""       ;  break ;   t , Vr  : array [ 0 ] of string    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 33))

	def test_34(self):
		input = """w , K , K  : array [ 0 , 0 , 1_7 , 1 , 99_6 ] of string    ;   j : function void  ( ) { }    ms : function string     ( inherit a : array [ 1327 ] of float      , out i : float      ) { Cl , pc  : auto  = - jb    >= H   * p0Sq3      , s   && k    >= mm ( )       ;  return - g      ;   Z  : boolean   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 34))

	def test_35(self):
		input = """eE5eX , MID , uL , q  : boolean   ;   vN , be  : array [ 3 , 0 ] of float     = UyDM   * Q    && Klqa   - Z4     - t ( )     <= a ( )     :: ZM ( )    * - A   + H      > ! u   && F    || K   * T        , X ( )     :: ! ! W     + P   && go    - ! Ul      < ! - Xc   && d         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 35))

	def test_36(self):
		input = """Ag , f  : auto  = a    :: ! - O     - - ""      <= V6   && ""     + false       , ! M   + Ty    + ! aZ      > uS ( )     :: xkK42z   / y   || s    * ! J         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 36))

	def test_37(self):
		input = """aC : function boolean     ( ) { }    
	E  : array [ 0 ] of float     = ! - - IV       :: "\\\""    && e   && R    && NMca ( )         ;   
    FBK , X , lHgw , SE4 , x , uPz  : integer    = y    :: ! - B   % b      <= NQNz6LJB   || lEl    * c   + pLt     % ""    || w       , .9e+279      , l   || oDmLTmB    && ! v     - ""     != B   * N    || jk    && ! h   / a        , - t    && gzg   + S    - n      :: { }     < - ! ""        , Un   - zS    + ! A     || k7   && o    - t   / kU        , ! Z2 ( )     != - KaSA   - k    % - G         ;   
	g : function void  ( ) { if ( GP ( )     :: Wd   + E    != x   + d4      ) break ;   else bN ( )  ;     J  : boolean   ;  a  : auto  = Z   + sC       ;  break ;   do { break ;   }  while ( C   && A      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 37))

	def test_38(self):
		input = """q : function void  ( inherit out t : boolean     , inherit cC : array [ 5_77_1_472_3 , 9 , 0 ] of float       ) inherit z { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 38))

	def test_39(self):
		input = """N , u  : float    = - ! ! pbB        , - false        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 39))

	def test_40(self):
		input = """rKY , k  : array [ 0 ] of string     = ! ! Bp    && - spcTK      != OY7    :: ql   > - ! - n        , TrA      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 40))

	def test_41(self):
		input = """M , i , x , O  : array [ 967 , 33 ] of integer    ;   J , lA , h  : array [ 0 ] of integer    ;   f : function void  ( out G : array [ 41 , 6_8 , 0 , 0 , 0 , 0 ] of float      , Z : auto   , n : array [ 0 ] of string       ) { return ;   }    qqNC  : array [ 6 , 6 , 0 , 2_843_8 ] of boolean    ;   W  : integer    = ! 53634055_3_8     - ! jbb3d   + H_y         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 41))

	def test_42(self):
		input = """M , s  : array [ 9_79 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 42))

	def test_43(self):
		input = """TunJC , XK , u_Jwtu  : auto  = - spi   - kV     + - PMSkP   && rf      > - - l    / ! wlJ        , ! - R     + - SpT ( )       :: "\t\f"    == { }       , ! wAI3   / Xq    - wj   - tyze       :: ! ! I0    - gOjQi   || xn         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 43))

	def test_44(self):
		input = """q , S , vuC  : integer   ;   M , nKipL8  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 44))

	def test_45(self):
		input = """uWU : function void  ( inherit out e : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 45))

	def test_46(self):
		input = """mtpbOxO : function integer     ( ) { d , g  : array [ 0 , 4_4_907 , 0 , 76 , 1_7 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 46))

	def test_47(self):
		input = """Q , i  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 47))

	def test_48(self):
		input = """RzVB , b0 , I , a  : auto  = 0e-4    >= ! ! U    + - R        , ! nc ( )      :: - I ( )     - DpuB   && w    % 0        , ! ! lG   / Z      == Ui   || G    * iIckm   || nt1     - F   || q3    - - i       :: ! P ( )       , - N    || ! ZMOS     % ! ! jt      <= iFx ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 48))

	def test_49(self):
		input = """YwTO , V  : array [ 5 ] of boolean     = - Q    && xAk   * QB     % lT   || y_GQos    / - V      != c1   % CTS    || ""     || 0.e+3       , - V ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 49))

	def test_50(self):
		input = """B : function auto   ( BnT : array [ 7 , 5 , 0 ] of string       ) { }    c6 : function array [ 0 , 43_372_47156 , 26 , 0 ] of integer      ( inherit J : array [ 4_5_1 , 0 , 47_46256_918 ] of boolean      , out eIO : auto   , inherit _ : string      ) inherit zHj { A  : string   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 50))

	def test_51(self):
		input = """Zhd  : array [ 1 ] of integer     = { }      :: ! ! t    + - H      != H7   || F   * j     || ! Yo1C   % McDd         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 51))

	def test_52(self):
		input = """Y : function boolean     ( ) inherit g { do { }  while ( ! l     :: POYI   / H      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 52))

	def test_53(self):
		input = """z1f : function array [ 0 ] of float      ( inherit out d : auto    ) inherit cCVs { while ( Jp   * E    < ! E     :: - Pd    != W   / wAgS      ) { m4im , z  : string   ;  }     o  : array [ 0 , 0 ] of integer    ;  }    gDy : function array [ 247 , 4 , 0 ] of float      ( inherit out l4_pWWb : array [ 824 , 0 ] of boolean      , inherit x : array [ 0 ] of string       ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 53))

	def test_54(self):
		input = """U , zx , BaQoyIy , w , Og  : integer    = s   || H    || ! xk     * g   && IL    * ! bJ        , ! R   && X    + 0      > ! A    && REhKn3   && aE29C     && - sS   % R       :: M   > ! ! QpEs    * ""        , ! a2    && dlfe8   && Jf     % R ( )     < rrMR   && Wd ( )    && _x   || kF        , R   % a    / Hp   % SAWG3WQ5     && Ix4   && xK    || ! DO       :: - s ( )     > dj_JR   && ui6    + - VFO     && SEgZw   - t    / odi   || s        , z   + Y    - h6   - e     % _R   * _    && - c      == - l   + T     + rfX ( )        ;   as : function void  ( _Anhd : auto   , inherit V : auto   , inherit zn : auto   , inherit out H : array [ 0 ] of float      , out cIZ : string      ) inherit sxCZl { }    G , EV  : array [ 0 ] of float     = - ! XMTQ    + a   % F8      >= - ! t    - L5v0DU       , p   + r    > 0    * R   || Q     % w   || t    * e   - lyPxu       :: ! h ( )     != aO ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 54))

	def test_55(self):
		input = """i : function void  ( ) { { }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 55))

	def test_56(self):
		input = """OvX : function void  ( inherit out T : float      ) inherit h { X , DAA  : auto  = ! CT    > ! KU     :: - z    <= _k     , - h    >= g   || mP       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 56))

	def test_57(self):
		input = """iS : function float     ( ) inherit o { if ( F   - FY     :: - xF      ) continue ;     }    uR  : array [ 27 , 0 , 9 , 0 , 392 , 814 ] of float    ;   kT0NLaGwN : function void  ( inherit out H : auto   , Qn : auto   , inherit out EK : float      ) inherit f { continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 57))

	def test_58(self):
		input = """R : function auto   ( ) inherit r { }    P  : array [ 0 , 0 , 4 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 58))

	def test_59(self):
		input = """k  : array [ 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 59))

	def test_60(self):
		input = """e , cHw_  : auto  = xg   + wZ    && ! z     + iN6   + - ld      < Y   + gY6 ( )       , - l   + cv    + ! K         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 60))

	def test_61(self):
		input = """R : function void  ( ) inherit jdDU { if ( w   % E    > ! p8     :: - I      ) { }   else continue ;     }    R : function void  ( ) inherit X { }    bY  : auto  = S ( )    >= ""    || - ! I       :: ! PY    && BM   && P57SDFAlh     % - - jBBF         ;   t : function string     ( P : auto   , out A : boolean      ) { if ( E9   - CZ     :: - N    != K     ) return ;   else return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 61))

	def test_62(self):
		input = """GS : function void  ( inherit out F : auto    ) inherit FT { }    V  : string    = W ( )     :: - ! v    + N   / n      < ! ""        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 62))

	def test_63(self):
		input = """O : function auto   ( inherit out kAm : array [ 17610_5 , 0 , 64_2_9_2_3_9 ] of float       ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 63))

	def test_64(self):
		input = """f , X , nV5 , vn1A7_ , Zs  : integer    = ! Rwzf ( )     - - Ro    / Ju   && df       :: n1   * e8 ( )    + - dj        , ! ! r     + 0     <= ! .43547e6       , U   && qZTU    % fsw   / kXZ     && LTP   / ! Q      > ! lR84kkD   || m     || ""    || N60   - uec       :: false    % - X    * M   % ATow        , hpIc ( )      , ! - T_ger    && t   / g         ;   dE  : array [ 0 , 4_0_9 , 64 ] of integer     = - Hk   - pZdqbL    + y   && hLnSU         ;   YOj : function void  ( ) { T , C  : integer   ;  while ( ! r     :: - F    > ! Z      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 64))

	def test_65(self):
		input = """rIY  : integer    = - - h_2Q   + _f      <= - ! 0         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 65))

	def test_66(self):
		input = """RI  : integer   ;   vw : function void  ( out i : auto    ) inherit sKW { p  : boolean    = V   && my       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 66))

	def test_67(self):
		input = """_6  : integer    = MYd   + gh    && DEU    || n   && I    * F ( )       :: - n       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 67))

	def test_68(self):
		input = """j  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 68))

	def test_69(self):
		input = """R  : integer   ;   H : function void  ( inherit out a : auto    ) { }    y : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 69))

	def test_70(self):
		input = """H : function void  ( LT : auto   , inherit p : auto   , out Hj : auto   , out e : boolean     , n : boolean     , inherit out J : array [ 0 , 200_5412 , 73 , 8 ] of boolean       ) { e  : integer    = - z     :: L   / PRy    >= 7       ;  c , hp  : float    = ! VyW8R7    > F6lGL   - d      , vrbOF   + kt    <= ! Vm       ;  }    jSl , x  : array [ 3 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 70))

	def test_71(self):
		input = """A : function void  ( inherit out B : array [ 0 ] of boolean      , inherit out cx : auto   , t : array [ 90_06_4_520_17 , 5361_296 ] of integer      , FJ : string     , out Am : auto    ) inherit r { }    h : function array [ 5 ] of float      ( ) { }    z : function boolean     ( inherit k : auto    ) { }    j  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 71))

	def test_72(self):
		input = """EnxhmiNhKT  : float   ;   a : function void  ( inherit out eK : array [ 6 ] of float      , inherit out M : auto   , inherit I : array [ 533 , 2 , 0 , 0 , 73 ] of string       ) { { }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 72))

	def test_73(self):
		input = """P : function auto   ( Q : string     , inherit WSx : auto    ) { }    CP  : float    = { }        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 73))

	def test_74(self):
		input = """pQ , ijF , v , ebAme , o  : array [ 8_49 ] of boolean    ;   A  : auto  = CH   > Wk      ;   k , X4 , T , xR  : boolean    = mAB   >= ! ""      :: ! P   - UQi    && ! gp        , q   + s    && q   + z     * ! q    && ! XGCe      != 0    - _u   || G     * e4A   / - Ja       :: - ! Y    + ! Cd8e      < - ie   || D    + F   || O        , ! AR ( )     <= { }       , y   - H   && Hk    || C   + v       :: true    != - W    || NHqwx   / ZE    * ! x         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 74))

	def test_75(self):
		input = """C  : array [ 3_504 , 8 ] of float     = ! - EI    || ! f      == ! ! p     / ! i    || - Np       :: ! Dc   && t    / R   % fl      == - ""     && CE       ;   C : function void  ( inherit J : auto    ) { F ( )  ;   X  : array [ 821_9 ] of string    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 75))

	def test_76(self):
		input = """iB  : auto  = ! 0     >= X ( )     :: - L ( )        ;   oD : function void  ( inherit x : boolean      ) inherit w { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 76))

	def test_77(self):
		input = """y  : string    = ! F   && y     * - ! fg      != - ! UN8G     * .82E+8        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 77))

	def test_78(self):
		input = """ZvR : function void  ( W : auto    ) { d , x , EiK  : string   ;  if ( eJD   || B    > IQ   * _     :: j   * JZ    > ! DN      ) return ;   else break ;     l  : array [ 9 , 0 , 0 , 0 ] of string    ;  k , i , _Hcw , F  : auto  = OC ( )      , ""     :: n7fV ( )      , u   || S      , - u     :: ! x_a    > Ia   / _6v5       ;  x6 , W , a  : array [ 0 ] of boolean    ;  P ( )  ;   G  : auto  = Ag   / m       ;  while ( _5m5GIbx   % X    > ! Z4_K9C     :: B   / ILc      ) { bJw7z  : boolean   ;  }     do { }  while ( NhY   / c9E     :: x   && bs    >= G   / L1N5hJ      ) ;   if ( ! b     :: z   - pnC2t    > ! WotN      ) return ;     }    P : function void  ( inherit DO : array [ 2 , 0 , 0 , 169807 , 1_5 , 0 , 7_7_0_14713 , 54_5 ] of boolean       ) { }    N  : array [ 0 , 3_2403_336_22 , 4_97 , 0 ] of integer    ;   A , e  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 78))

	def test_79(self):
		input = """Z : function void  ( ) inherit O { { Wm  : array [ 26_8 , 593_5_8 , 0 , 0 ] of float    ;  break ;   }   K  : auto  = Gu   + qk       ;  qiPuMQh , dm , ug , S  : array [ 0 , 0 , 0 , 31 ] of boolean     = ! p8    < x ( )     :: X   / A      , - cd      , ! E     :: - Ag6cf    > k   * GrIHZ5      , SED   || j7r       ;  uF_deY ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 79))

	def test_80(self):
		input = """xOTp : function auto   ( ) inherit Ch { bWdVo , cAyhj  : string   ;  for ( rI_ = z   % Dq     :: ! S      , lH   % A      , ! f5B     :: y7qJ   / g      ) { }     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 80))

	def test_81(self):
		input = """UHx : function auto   ( ) { }    J : function void  ( inherit out AN : auto   , n : array [ 1 ] of string       ) inherit Y { s  : auto  = ZW   + P     :: - B       ;  while ( f   || KHd    != pXaJPF   * zQec     :: R   - h      ) v ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 81))

	def test_82(self):
		input = """c , Xf  : array [ 79463 , 0 , 5_3 , 85_821 , 79_836 ] of float     = - A    - lQ ( )     + ou   || knE3r    + sR     == v   / jt    + w   * sl     - z ( )      :: ! ! B    + fw0o   && X        , ! V ( )     <= - Z   || a     / y       ;   E5 , J , X  : array [ 3 ] of integer     = ! df   + hnS    * pK   || r        , - - Ls     - - v    / aJ   && B       :: ! I   + E     - - t0J   && dM        , - ! d    && 0         ;   h  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 82))

	def test_83(self):
		input = """K : function void  ( ) inherit Y1VF { if ( ! e    >= ! FqmL     :: K   % _    > - DTRBQvQL      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 83))

	def test_84(self):
		input = """ek7Iy : function void  ( inherit Xz1 : array [ 4 , 0 ] of float      , inherit out A4Pi : auto   , out q : array [ 5 ] of string       ) inherit i { n , iXC , cq_  : array [ 0 ] of boolean    ;  q , gk  : string    = - h    == zT   / jG     :: s   - qU    != s   % JJ      , - eNb       ;  R  : array [ 2 ] of integer    ;  do { }  while ( ! IL    >= S   * X      ) ;   uc  : auto  = R   + c    == 0     :: cYM   && U    != q3 ( )       ;  }    g , D , w , m  : array [ 0 , 0 ] of boolean    ;   Y : function auto   ( ) inherit hi { if ( Rw   / N     :: ! sv    == - f      ) { { }   }     if ( K3   && K      ) l6B5Iy ( )  ;     break ;   }    M , T , Q , nF , c  : float    = ZbW   * y    * _CA5   * d     || mDH   + n    % ""      == ! ! rSE   % R78T        , - E ( )     % ! ! R7       :: V4     , ! p   || BA    || ! X      >= d   || SX    && - p2u     && Z   / diZvt    && zAqf      :: ! - 62        , b   + pL    % d   && suRZU     + v   && i    && D     >= z ( )     :: ! ! DnR     + oCh ( )       , k ( )    && ! m    / kf_   || qj      >= mpSU   - z    - ! d     || ! h    && - J         ;   BW : function array [ 662679395972 , 22_27_3985_339808 , 616_3_52_03 ] of string      ( inherit a : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 84))

	def test_85(self):
		input = """q : function array [ 0 , 0 , 69_21 ] of float      ( inherit CD : array [ 0 ] of integer      , out lc : boolean      ) inherit G { h  : array [ 0 , 11_5_6 ] of integer    ;  w  : float    = ! M    >= 0     :: - fw       ;  }    Q58 : function integer     ( ) { cLH  : integer   ;  }    f  : array [ 0 ] of integer    ;   C  : array [ 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 85))

	def test_86(self):
		input = """Fe  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 86))

	def test_87(self):
		input = """_  : array [ 0 , 0 , 5 ] of float    ;   JYD : function void  ( ) inherit m { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 87))

	def test_88(self):
		input = """qt : function array [ 0 ] of string      ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 88))

	def test_89(self):
		input = """uO , G , w , C_ , EC_  : string   ;   V , Y , g4  : auto  = 1334_567E2    + - O   || J_        , - - l     || F   && FR    / - k      > ! ! t    && Kw   + F        , { }      :: vF ( )       ;   k76aXA  : auto  = f   * k    || S ( )     + ! - f       :: ! q   - m     + - - S      < ! ! Pn ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 89))

	def test_90(self):
		input = """T  : array [ 5_0 ] of string     = v ( )    + - J    && _d   + fN      != - _   || O     || ! _ ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 90))

	def test_91(self):
		input = """N , f  : float   ;   v , u , ngh , bMR  : array [ 0 ] of float    ;   G2 , _ynm  : array [ 689_574 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 91))

	def test_92(self):
		input = """D : function array [ 0 , 0 ] of integer      ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 92))

	def test_93(self):
		input = """ShEV8 : function void  ( out x : auto   , YD : auto   , di : float     , out CBA : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 93))

	def test_94(self):
		input = """cd , yx , g , jXLHe  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 94))

	def test_95(self):
		input = """q : function void  ( inherit out iy : auto    ) inherit qifN8 { }    Q : function array [ 0 , 9_263 , 75 , 56 , 0 , 78 ] of boolean      ( ) { E  : float   ;  v  : string    = - E2       ;  for ( D = q9tA   || f    < iq6wqc   && Np      , P   - Vr9vTb8B    != H   || G     :: I   + P6r      , - Un      ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 95))

	def test_96(self):
		input = """jR : function void  ( ) { }    wV : function array [ 0 ] of boolean      ( ) inherit J92 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 96))

	def test_97(self):
		input = """zC  : array [ 5_951 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 97))

	def test_98(self):
		input = """Kh : function auto   ( ) inherit c { ougK  : string    = U   || RQX     :: - e       ;  }    YfF : function void  ( inherit W : integer     , bQ : array [ 1762 , 0 ] of string       ) inherit EG { }    y : function array [ 0 , 0 , 7 ] of string      ( ) { j , Cx , b , w , f  : auto  = c   + E     :: N   - Hq      , 0     :: nE   || n0x      , A   - Z    < ! R      , LM   - U    == 2      , ! a0    >= Z   - A     :: a   && T    != f   % S       ;  u  : auto  = x   % IL       ;  { QA , m  : string   ;  }   q  : array [ 86_4_76_156_04_9 , 36 , 0 ] of boolean    ;  }    c : function auto   ( inherit U8U : auto    ) inherit xnb { PK , fZXhEl  : float   ;  return - B     :: Fc   / R      ;   while ( s   && y    == JG   / Q      ) R ( )  ;     }    d , j  : auto  = ! - ! u       :: Vu ( )    + E   - Q     + ! jo   + Tcn      < ! NLZ    + Yx   || XB     + qJV   * U    && UGLU   + ef        , ! ! Ol5C    || a   - g8         ;   OWj  : integer    = ! Pt ( )        ;   dO4 : function auto   ( out n : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 98))

	def test_99(self):
		input = """jZ : function auto   ( ) inherit ho { iq = jG   - E     :: ! H    == s3Mc ( )      ;   for ( AA = ! bJkg    == l   - vk      , ! x      , - AS     :: ht6pi ( )    < ! o      ) _H ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 99))

	def test_100(self):
		input = """N  : array [ 31_88 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 100))
		
	def test_501(self):
		input = """m:string = "kek"; """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 501))
