import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = """s : function auto  ( ) inherit _n { }    X , dy  : void  = R7V   && gJ    % T   - D1b     && ! U    * ! e       :: - SYW9RQ    * Z   / qW     || - ""      == fL2 ( )    + Y   / LV    || V   - s        , ! D    && - nI4     * T   / - KX      == 754636     :: ! - AC    / ""         ;   NG : function array [ 5_107278_55 , 301658_20_6_74_676 ] of integer    ( ) inherit LBBa { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = """B , KsMJ , JL  : array [ 6 ] of boolean    = - s   && WozO    && wHj   || Zs       :: ! GA   && aIW     && - DP   && yl      >= - A   || e     / ! ! Tg        , yO   == - yz ( )       , - Y   % D     % rz   || k    % Nh7   - v      >= ! Z    || ! nB     - ""    % Bt   / djT       :: ! ! ! Zt         ;   h , O , Si  : void  = - D ( )     < P1 ( )      , p   - M   && Dzh    && M   % df       :: v   + _FE    + y   % V3     && 64       , ! ! p5   % OA      != ! false        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = """g : function auto  ( inherit Ddv : auto    ) inherit I { }    Y  : array [ 71 , 0 ] of float    = - wWV   - k   && R         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = """fQ : function void  ( inherit out y_eUwJ : void    ) { }    S1  : array [ 0 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = """O  : array [ 0 , 0 ] of float    = - - eh    + LY   * C       :: ! FVI       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = """f : function auto  ( inherit o : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = """C : function void  ( ) inherit o { { s , r , r , U , c , wg  : boolean   ;  }   k  : boolean   ;  }    _e : function void  ( out wpG : void    ) inherit Xn1 { j  : string   ;  vX , ig , DC , QN , O  : void  = - T    == Np7yx    :: ! Fph7    > qD   - dm      , - H    < Z   || im      , YxCi   && fI     :: ! R4      , Mb   / Rw    <= - z     :: tPk   * T    > - T6N      , uWs2C   && Q     :: - z       ;  if ( t   || H      ) return ;     b , I  : float   = ! k0      , ! p       ;  break ;   if ( ytLJuv   && o     :: t   && j      ) return ;     return ;   return ;   { }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = """B : function void  ( out JW4 : void   , inherit out Q76 : void    ) inherit k { return Xu   && CA     :: AY   < Fr   || yn7x      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = """J6j , U  : integer   ;   a : function auto  ( ) inherit A { q  = l   + w7A     :: ! h2DYI    != 1      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = """dmEvUc , V , XI  : void  ;   l : function auto  ( ) inherit o { l  = s   - th     :: t   * ln      ;   }    Ei , wx  : auto  ;   xR , zG , rg , G , yN  : auto  ;   T , EUc2 , a  : float   ;   lCZEr , j  : integer   ;   t , L , ml , z , l  : string   ;   nWQoI  : float   = ! Mk   - U     * WU   && L    - ! F      < true    || - ! z       :: 0    - ! KTPAZ     * - ! yPx      == S      ;   y : function auto  ( ) { }    wNB : function void  ( inherit out G : string    , inherit out hO : void    ) inherit Zlq { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = """APTV , N1  : integer   = - S   || ysnBg    && - oY      > "🪐\\"𑝀࿎ⴧ𝔕"      , B   / p    || ""     && - dF    % ! sl      > ! bHY   && QJnX60K    % ! P         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = """b : function void  ( inherit zbD : void   , inherit out VyL : integer    , inherit out A : void   , out oD : void   , out n : void   , inherit TSxi : array [ 0 ] of boolean     , out W : void    ) inherit A { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = """gSj  : array [ 63_6 , 0 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = """qZ : function void  ( ) { }    bE : function auto  ( ) inherit ed { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = """x  : void  = k   && HYie    - H   * TRHP     && xt   / BNk    / r   && W      <= ! - tkg ( )         ;   xM : function auto  ( a8Q : float     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = """K , hlJ  : string   = B ( )    < ! - ! l3i        , ! ! ! zJ      <= MKj9   - u    / ""     % - f    && ! r       :: - - - tLI      == ! ! ml    || b   || ak         ;   Io : function string   ( ) { }    ZRa , e  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = """T1G : function string   ( inherit Cgh : auto   , out sv : void    ) { p4 , NwB , kMm , Hp  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = """P : function array [ 5_432_6 ] of string    ( out P : float    , out bbMs : array [ 0 ] of integer      ) { }    m : function void  ( ) inherit n { }    T : function void  ( inherit _ : integer    , inherit iv : void    ) { M5e  : void  ;  gP4 , ek , g , DPgKL5  : void  = nD6   * l      , X    :: Iq   && Y      , - hJk      , _Z   * b    > H   && RCQd     :: u   - rG    < - A       ;  }    Ht : function void  ( inherit out Per : array [ 0 ] of string     , T : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = """B : function void  ( ) inherit HM3 { do { XP9_D ( )  ;   OO ( )  ;   }  while ( 0     :: r   % f      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = """Uei : function void  ( inherit n8 : array [ 4 , 0 ] of string      ) { for ( Bu  = p   % H_     :: y   * La      , ! Z      , W   - b     :: - b    != s     ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = """pn : function float   ( inherit T : void    ) inherit Ga { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = """C : function float   ( ) { }    F  : void  = s   || FA    - z   + p     - n ( )     < G   + - z1    + i   - O       :: true    && dcT   && LG    / IqE3   - R         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = """g , pqw  : integer   = - - gw   * enXgb      == ! mJt   || w8x3     + - m ( )       :: R31iGlEyh ( )    || dg   + By     || hv ( )       , - Ib   && kl    + TPH   - LSK      <= - ! r    + z   - yKCQ         ;   g : function float   ( out C : auto    ) inherit rWBP { }    q : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = """DJ  : float   = j ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = """KPv : function void  ( RM : array [ 0 ] of boolean     , C : auto    ) inherit A { }    yL  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = """J : function array [ 0 , 0 ] of string    ( l : float    , inherit toR : array [ 4_195 ] of boolean     , out oz : string     ) { Q , JlFN , T , i , DdUD , Ok0p  : float   = ! Ez      , y    :: Y   * eEi      , - _    != ! t     :: l   - C      , jEK   && uJ2mX      , a   && W     :: a   && NCmt    != k   * t5      , k   && iK       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = """Z_d , L  : array [ 0 , 0 , 0 , 90 , 24_3_51 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = """mD , Rbx  : array [ 0 ] of float    = ! Z   * I    && K2   - F        , mH1GC   && T    || Pt   * N     + - - k3         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = """d : function array [ 0 ] of string    ( inherit nFE : auto    ) inherit NH { break ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = """mc  : array [ 4 , 0 , 64 ] of string    ;   RP  : array [ 1 , 0 , 93_4_8 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = """B8 : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = """u , V , c5clvp  : array [ 0 , 2 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = """yjci : function void  ( inherit out f : void   , MC : void    ) inherit DX { }    C , T3Oq  : array [ 817_32_8 , 9_5_8 ] of string    = jfH   / g    - s2   || EHa     - h   || G    / f   - g        , j   || Z    / k ( )     - - - QVM      <= y   + S    % Y   / u     + { }         ;   _ : function auto  ( inherit out Nu : array [ 0 , 204 , 3_4 , 59 , 0 ] of float     , inherit out xB : auto    ) inherit V { }    n : function void  ( ) { }    eP : function array [ 28_3_90 , 0 ] of boolean    ( ) inherit Z { LyJ  : void  = M   || Gw     :: A   < R   + e7       ;  V  : array [ 0 ] of boolean    ;  }    y : function array [ 4209_3_85 , 9 ] of integer    ( inherit out t : float    , inherit U : void    ) inherit J { }    Y : function boolean   ( inherit u : void    ) inherit y { }    a  : void  = ! - hF5    && B   + a      < - Z ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = """GzH  : integer   = - o   && F     - - H ( )      != - S ( )     && - _Cw   && DDYmoP       :: - - I3RQ    / ! v         ;   X : function boolean   ( ) { xNsLxr , j  : integer   = D   % F      , - EO    >= mZ ( )     :: ""       ;  b , pTM , Pu , D  : void  ;  }    G , Q  : array [ 0 , 0 , 0 ] of boolean    = UKS   + P    + ""     / b   + ATm    % - Nu      <= - ! g   || Ra        , CF   + Fq    - PIe ( )     && ! j   - d      > false     :: 1    - La   + c6z    / D   || fZ         ;   GMrm5 , Oq6  : float   = ! - _ ( )       :: c   + Tv    || ! F     || - AGOW5    / ! rhUm        , y   % C7b    + ! DK     || qFSw7S ( )     >= ! y   + T    * B   && vR         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = """z , oUSY , j  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = """W : function void  ( ) inherit W { YUT , GR , E  : auto  ;  for ( v4rxA  = n   / W     :: K   / Dr      , d ( )      , wU   + d    >= - xK      ) { }     return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = """utoC : function array [ 0 ] of integer    ( u : array [ 0 ] of float     , inherit u : array [ 1 ] of string      ) inherit JP { SM25  : void  = ! xo7       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = """R : function array [ 29_067_2_532603_40 ] of float    ( ) inherit G { o  : float   ;  Y  = rQb   || v      ;   }    IK : function void  ( inherit out F : void    ) inherit Z2 { }    VOG : function auto  ( ) inherit kHI { sH57E  : auto  = s ( )       ;  break ;   do { Lp ( )  ;   }  while ( y5vv   * P    <= g   / OmVnkK      ) ;   while ( - T     :: PNm   && d_j    == ! S      ) continue ;     }    ISy  : void  = ! ilE7R   + m     / - Mp    - ! h      <= tJw   || d    / - W     - t ( )    % - zzN         ;   k , K , FOt , c  : void  = r   % GtxLArXV    * uS   % R     && ! DB    && I   || gw       :: - jS ( )     == ! I   || a     % ""    - uX   || bu        , - ! dSI    || Zk   / Rd       :: ! ! - u      > - - Mr     - SuD3i   + f    - u   + y        , ! E   + C    - aS   + m       :: - JEX   % _     * r   % Ziw    || ! yMT      >= u1   || z   || sa     % R   / M    && rX   && O        , - - Fd     + ""     >= Z   - ! w    * ! Ye       :: - Ff   - tXLc2c     && - O   && Pv         ;   I : function string   ( inherit C : auto   , inherit out e : void   , out ble : integer    , inherit s : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = """N : function void  ( ) inherit gBNfdA7 { d  : boolean   ;  return f17   - O      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = """g : function void  ( inherit U : string     ) { while ( ""     :: Hy   - y      ) break ;     bJz  : void  = i2   - ErG       ;  kJ , b  : array [ 0 ] of float    = e   * qQ     :: u   * hKR    <= 5      , ! x6       ;  z  : void  ;  do { }  while ( t   > l   / V     :: te   || r      ) ;   O  : void  = J    :: ! k    == L      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = """z , Y , k , voLB , Tw , N0 , T , X70 , RK , C , Rjk , F7tuv1  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = """eokJALJ : function array [ 7 ] of float    ( m : array [ 0 , 0 , 0 , 66 ] of integer     , inherit e8XtK : auto    ) { p  : array [ 0 , 0 ] of boolean    = ""    > - P       ;  }    E1 : function float   ( ) inherit fXj { }    h : function auto  ( ) { g , wV  : array [ 0 ] of integer    = DfX6A   || W     :: Fp   / p    >= y2WPHq   % o0      , Z   - q2     :: A   * u3CAN    <= n   - LuQ8M       ;  wG9  : auto  = zFCl   / l7     :: F   - u    != qgspf0      ;  }    N_ : function auto  ( inherit out w : array [ 6 ] of boolean      ) { GQ4lY , Z2 , _ , W  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = """M : function void  ( out B : float     ) inherit ktwrB { }    U  : auto  ;   T , l , A , x , i , Dfal , S , Br30g  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = """Ktw  : auto  = ! _    || ! A     + - C   - Y      == ! K ( )      :: ! - C   + p      <= hC   + q    + ! _D     * ! ! ifHu         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = """jy76 , y , g , Y  : array [ 0 ] of integer    ;   XgvL : function array [ 9_3_3_4 ] of integer    ( ) inherit o { H5 , P  : auto  ;  Z , q81F , B , X6 , b , e0Z_Vs , Q , J , mpBq  : boolean   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = """nRaI : function float   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = """x , Kw , _YcQq , m , HZgR , Os , Uj  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = """G : function string   ( ) { TGYlQ0u  : array [ 0 , 9_343_9_3 ] of integer    ;  while ( ! s    <= UU_Q   + C6      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = """u  : string   = O ( )    + - Exnt   && dj         ;   K : function auto  ( ) inherit hApOB { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = """gz  : auto  = D   / HP7    - wQGI   + l     || V    < wsY   - Q8    && p   / NX     - ! R    % p   * uU         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = """y  : integer   = ! K   / y     && - Yp   && prNQ8y       :: q   || v    / y    % 0     < ! C   % AJFgh    || lpzj   || V         ;   P  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = """Ev : function auto  ( ) { Am  : array [ 0 ] of integer    ;  v  : void  = ! e    < ! UL       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = """o : function void  ( out N : array [ 0 , 0 ] of boolean      ) inherit l { for ( R  = TU2C   / h     :: ""    > K   || kK      , c   - Q    == - V      , a   || _N    < h   * a     :: r   || Vb      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = """Jd  : void  ;   g : function auto  ( out r : auto   , out GVA : array [ 2357 , 3849 ] of integer      ) { if ( g   + ZC    > O   / B      ) { }     do { return ;   }  while ( U   - Bm      ) ;   for ( ii  = Y ( )    <= Au     , kFUIX   % v3I     :: ""    <= ""      , hw ( )    == KT    :: - V      ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = """tlf : function array [ 2 , 0 ] of integer    ( out cE : array [ 6 , 8 ] of integer     , JKi : void   , inherit H7KOaH : array [ 0 ] of boolean      ) inherit Tdwt { break ;   }    E : function array [ 15 ] of boolean    ( ) inherit xi { }    Maf : function array [ 0 , 9_4_85 ] of integer    ( ) { }    c , gqO , AV  : auto  = ! "\\t𞺊"     != P    :: - ! MQz    + ""      != - ! I   / H        , - uaIG   * o    || Ca   - kop       :: - g    >= ! f ( )       , ! U   % u     && - ! xvsf      == SESg   && qE    - w   + B     * C     :: _   && X    * - CB7     + 5_9_7_22        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = """j , G5C , B , Yh0 , V  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = """lENIS2 , z  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = """S : function auto  ( inherit a7 : string    , inherit out H : auto   , inherit BT : string     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = """Rw  : void  = ! AG   && Ew    || _Ip      :: 0       ;   y : function auto  ( inherit out Xf : boolean     ) inherit p { return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = """GA_ : function auto  ( ) { break ;   }    nJD : function array [ 0 , 35_535 , 0 ] of float    ( ) inherit Ij { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = """CF : function auto  ( ) { do { }  while ( - XkD    <= yLi   * l      ) ;   }    uR : function array [ 8_85_4_58_95495156 ] of float    ( ) inherit uM { O ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = """i  : array [ 0 ] of float    = - d   && SyQ    || czD     != ! ! u    % - Y         ;   e  : void  = Zz ( )    - ! ! K      != - E     :: ""    - - x     * h   - L    + - fM         ;   r , r , BV , o , fD , p  : auto  = ! tDUd    || _3Ox   && R     || ! x    || o   / I       :: - - D    / ""      < ! j   * nani    * I   + r        , - KoH ( )     + 0    - ""      == ! m   / KcBMHY     % - - RT0pV       :: - Z   - Y    % O   * f      != - j   || z     && - cCMe    % Wd       , "\\\\"    < ! ! f    || - W        , ! q    || bEPs    % - m    - 4      != ! zHu   || nb     && ! d7D   % RM        , ! JlV    / YEp   / MECB6J     && - V   || E        , - Z   - eF6wzL     / "\\\\"        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = """af , U  : integer   = ! lXmRA ( )     / We ( )      :: I9_6   - JgEc    - mZ   % GmW     * h   + mp    && vvTf6 ( )        , sBOa ( )     :: p   / cExCNZ    || - QytgtT     - false        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = """L : function integer   ( ) inherit S { Dqn  : array [ 58_0 , 0 , 6 ] of integer    ;  }    x  : array [ 4 ] of string    = ! H    || kM   * bK     * ! ""         ;   D , ke  : auto  = 0    / J   % S     * ! S    * pOm   && t      == ! ""      :: ! pM    && x    / ! T_    - cfA   % zhr      < ! - ! fT        , ! CT   && - TH       :: ""       ;   gbKE : function array [ 0 , 9 ] of boolean    ( inherit out r : string     ) inherit v { }    Pc , tb , _ , uy  : void  = ! ""     || V_Ne   - z    / - Zs      < z    :: ! v   * i     && e ( )     < r7 ( )      , 5E9    >= k ( )    * M9Fjf   - E    || e   % BZu       :: { }       , ! e   - J     || RY   + Z    || - rY        , { }     != I   || iL    + E    + - m   * B       :: false    + JFHRo       ;   _h : function auto  ( ) inherit d { nH4 , CZ8 , pIqV , H  : array [ 36_9 , 0 ] of integer    = Pvv ( )    >= - V      , - E    <= U   && h      , - J    <= Wh1   % qzZ08      , A   / GuFq    > ! khN       ;  }    _rQ4a : function auto  ( inherit out ID : void   , KB : auto    ) inherit L { qqd6  : void  ;  }    VQ  : array [ 0 ] of integer    = b   || x   * j     + m ( )     != - p   / G     && S   && G    / LC   / P         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = """t  : array [ 72_652_9_196 ] of integer    = DPs4TXpM   - FEq    || f   || HNBNB     + ! i   - D       :: 8_9.5e+6    < Z   || i   || Fu    || XeB   * t         ;   uk , jwT1 , P  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = """E : function array [ 7 , 0 , 830549_65_664 , 0 , 7 , 9774_6 , 28141_7279 ] of string    ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = """o : function auto  ( ) inherit qTD { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = """HvW : function auto  ( w : boolean    , out A : void   , Rz : array [ 0 ] of integer     , M : void    ) { cY  = ! j    != ! n     :: VMmU   && t      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = """F : function float   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = """l , c , zZ0 , q  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = """lq : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = """p : function auto  ( ) inherit SZ { for ( O  = hQ   + AZEy    == WM   && mH     :: F ( )      , - R1    >= v   || Z      , H   - B    <= - Y     :: ""      ) continue ;     continue ;   K  : string   = J   + g1    >= O ( )     :: Q   + Tw       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = """GW  : string   = e2   / ! p     / yd   / BSTkhz    + ! W       :: ! ! L     || e   || v    / x ( )         ;   N8Ee  : integer   = ZtwU ( )       ;   C : function void  ( ) inherit H { return ;   }    O , V  : boolean   = - - b     - i   % - ID      != ! true       , ! EsTb0    && uF   + f    * l   / r      == Fk   + N    - - m     * wW   + I    * ! q5         ;   f : function array [ 0 , 660_59 ] of boolean    ( inherit out rojFxrl : void   , c : string     ) inherit NYCs { }    u : function void  ( out rFCkmI : void   , f : array [ 0 , 5_4 , 2_29 ] of string      ) { return _u ( )     :: m   < rAi   && m      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = """k : function auto  ( m8sm : auto    ) inherit iObq { n , e  : string   = E   + j    >= HDN    :: n   * p    == pFEB     , n   % LHMV       ;  Yww ( )  ;   do { }  while ( BB   - uX3    >= k   / Y     :: UA   * ql    > I   - EL9      ) ;   t5  : float   ;  b  : void  ;  Tw  = sF   / TfG7      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = """C7 : function void  ( ) inherit s9U4 { continue ;   }    Z : function array [ 58_7 ] of string    ( ) { { }   }    nVDC2 : function string   ( inherit I : auto    ) inherit e6 { Ta  : void  = ! X    > I ( )       ;  }    wxz  : array [ 25 , 7_3_31_6_4_5 , 0 ] of string    ;   YYR , v29 , OlVo8t , V  : auto  ;   G , i  : array [ 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = """ru  : void  ;   Rn  : void  = X ( )     :: ! rzj   + g     % ! - Y      != ! w   || XC     % M   / v    / bVaC ( )         ;   g : function auto  ( cJ_fP : auto   , inherit out n2j : array [ 27_900_44_4219_1_62_14_1_8_38_9 ] of float      ) { break ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = """VYM : function void  ( ) { for ( p  = ! A     :: u   || O    <= - n      , I   % F7PfXDG     :: X   + D      , - RQw     :: 5    != US   - IAtFSo      ) break ;     }    NZ , yn , n , Mb  : void  = - B     :: dlAE     , - L   - Ku    % - f      > true     :: ! - Y   && mAX2        , y   - l    + ! x     || ! ! N      < s     , - ! H4s6K     % - - d      <= ""       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = """L : function array [ 6769_9_014 , 0 ] of boolean    ( out xJw : void   , inherit J : auto   , inherit out Y : array [ 0 , 71 , 0 , 0 , 0 , 0 , 42 ] of string      ) inherit S { { }   }    S , r , Z , Nr  : string   ;   N  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = """VBgHQ  : auto  = - - ec     - P   % lh    || U   / A      != - K1    - m   * gXE6w     / hR ( )      :: GS   > ! H4 ( )    || ! Mm         ;   d  : auto  = ! ohUghK   || D3     - skU_h ( )      :: - - M   - b      != ! u   || SS    - - u8         ;   N : function auto  ( ) inherit K { do { }  while ( - D      ) ;   w12U  : auto  ;  }    dR : function void  ( out Wb : boolean     ) { }    b  : array [ 5_6_82_12_838_747 , 56_8 ] of string    ;   H : function integer   ( ) inherit m { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = """I : function integer   ( out Tw : array [ 0 , 0 , 0 , 0 ] of integer     , inherit wszT : auto   , inherit out XxB : float    , inherit C : array [ 0 , 9434 ] of string     , out E : void    ) inherit A5Oz { u , s , j , E  : auto  ;  x3k , n , H , w , B , z  : auto  = ! YxwqZN    <= Q   + kP      , M   || B    > X   + M      , - mw    < d7   % bymr      , ! jaaX     :: ! j04AiF      , - u    >= d   / g      , O   / R1    != qA   / eW     :: N   - x    != zhwCc   - B       ;  continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = """A , lZf  : auto  = ! - z    - ""       :: ! ! ! s      > R3_a   % ew    + tW   / bm3     || HTx   % Nay8    || n   % f        , ! p ( )     == - ! 0         ;   S  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = """H , B  : boolean   = r   % fu_b    * ""     && ! OQ    + ! xE      > tIm   * dJ    / RA   || G     % U ( )    / - H       :: ! xS    && z    - ! - Q      >= ho ( )    || - - R        , ! ! XX    % O   && f      <= - - Z     + SO3q8 ( )        ;   UD : function auto  ( inherit Hs : array [ 6_15 , 0 ] of float      ) inherit l { }    y  : auto  = ! ! s    && 0      <= - W   - pd   || ZZm       :: - ! S   / J0         ;   c : function void  ( ) inherit D { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = """YWF : function void  ( ) inherit u { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = """y  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = """W6vWo , BL , F  : auto  ;   k , I  : auto  = C   <= L4Uj   + RgP    - z    * ! Ar   - vVePnY        , ! { }       :: Awc   || - o    || ! SAm      == - faTEl    - Y   - n     || { }         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = """X : function auto  ( ) inherit Lq { OLVf , B  : void  ;  }    Y0 : function auto  ( _M : void   , Y : void    ) inherit g { }    NQz : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = """Uy : function integer   ( inherit B : auto   , inherit out d : void    ) { }    R  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = """Ko , Z  : array [ 132_4 ] of float    = false    && ! I    % ! k        , 0    && ! lJ    % N6At ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = """S , vb , N , Nw  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = """O  : array [ 0 , 2 ] of boolean    ;   FpZ  : float   = - - fod     * _   && tno    && - a      < ! Ne   && o     || ! Pxg    % M   + L         ;   b , Rsk , _7  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = """A  : array [ 198_461 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = """uF : function array [ 0 , 64 , 0 ] of integer    ( ) { }    R : function void  ( inherit mdW : integer    , z : auto    ) { }    Cx  : array [ 0 , 15_5 , 48_2 , 0 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = """g  : integer   ;   k  : array [ 0 ] of float    ;   jrf  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = """P6 : function array [ 30 , 3_7_530_4 ] of boolean    ( out Cp : auto    ) inherit w { for ( p  = ! a    == ! S      , - J    > EW   - J      , Df   && z      ) JA ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = """cS  : array [ 0 ] of string    = rca   + Si    || uPB   && VzG     + T   || bnsB    + W   / Vkbj         ;   F : function integer   ( ) inherit P { J3LmD , lG  : boolean   ;  v , zVm  : auto  = ! h    >= u   - kfdn      , AQ   % _Rm       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = """S  : auto  ;   u : function array [ 3_5_0 ] of float    ( inherit out N : void    ) inherit vDfS { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = """r , E  : string   = ! v    / f   || n     && D   - _    && ! yr        , - l    || - B     + 0    - - Uy      >= bh   / K    / gOV    * Nkd       ;   gbyenu , NTw , M  : string   = ! l ( )    - 3        , ! ! N   && AC        , - ! o     && n ( )    % ! hsqhr       :: ! b    * ! w8k     && { }         ;   E4  : array [ 0 ] of boolean    ;   m , aKIb , M , YL , _  : float   = - ! 0      < ! - ! zO       :: ! kETM3   + _     / u6Y   - fg    - T   && vcn      >= _     , V ( )    || ! ep   + Pr        , { }     + ! As   / d      > E   || S    * yebV   - fb     + - AB       , ! ! Lg     / hTZ   - ZUBr    && - e        , - dUA   * oQJ    || - xHqX         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = """M : function integer   ( inherit out F : void   , inherit Op87Cc : void   , inherit Y : array [ 0 ] of boolean      ) { E  = DYWl_   % NW0J1Za     :: yv   / ej      ;   t , v  : float   = - X    > p   / jq     :: U   - nI    == ! k      , - k     :: P   / e    != vc   - J       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = """qY6dgBl : function void  ( inherit out p : boolean    , out rUNr : void   , inherit w : array [ 0 ] of integer     , out _buRE : boolean    , inherit gM : auto    ) { U , n  : void  = Lb   && a      , ! k    == - p     :: q   || g       ;  o , I8 , XrCa , S  : void  = ""    <= GQ   - Uaoqj14E     :: - XmK    != x2OVs ( )      , _   * B     :: K   || P      , d0   || G    > O   % KHs     :: k   * d      , ! h       ;  }    Fa : function void  ( ) { }    w5  : array [ 0 , 9 ] of string    ;   ov , C  : auto  = - N   * F7     && AV4   % _sM    - ""      > - R     :: ! JP   - Sa    - ! g9      > - - o    % H   + L        , 0e3    < S   + H    - - Wz     - 0    || A   % Y       :: ! YV   % SKFj    + PT   || edqEM         ;   A7Uv  : auto  = ! w   && h   % f      <= RS ( )    - - Oc    || ! b       :: ! RS   - pUz     && - Oq    * - f         ;   Q  : void  = ! - 7      != ! ! rq    / qodM   * gq       :: q   != ! I   - p93wJNbRMerv     && X   % fG    || hF   - qV         ;   Ub  : array [ 0 ] of integer    = ! ! L    + i   % pv      == ! d2   - L    - ! g         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = """SRUp : function boolean   ( ) { m  : array [ 0 ] of string    ;  }    mL  : boolean   = ! SLy ( )     < ""    - I   % b     / - K   + O8         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 300))

	def test_301(self):
		input = """FKx : function float   ( W : float     ) inherit H { ZOrBtNFc  : string   = Q   - aJ     :: yT2   || C    > ! O       ;  break ;   if ( ""    <= - zj      ) continue ;   else continue ;     E , Rgu4  : void  = Nm   || J8ObtWN    != - v0      , ! E    < icHP   + LXN7Eq       ;  }    B , Q  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 301))

	def test_302(self):
		input = """a3 , ZA  : float   = ! - - TC       :: 0    / h   - vL0i     - ! Y   || K      >= p     , - ! - uXI         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 302))

	def test_303(self):
		input = """B : function void  ( inherit x : boolean    , out J : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 303))

	def test_304(self):
		input = """g : function array [ 19438_72_54 , 0 ] of boolean    ( inherit P : void   , kN : float     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 304))

	def test_305(self):
		input = """iZ  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 305))

	def test_306(self):
		input = """Q8 : function auto  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 306))

	def test_307(self):
		input = """W , M  : void  = - Sw7    + Y    + v   + J    && ! PO      != - - N_e    - ""        , "\\t"    + Efl_a   - r    / - Gq         ;   fb1VD  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 307))

	def test_308(self):
		input = """k  : void  ;   V , l  : auto  = eZ3m ( )     :: - S   - ws7HS58     / ! b    * h ( )      <= gC   + - Q    % T ( )        , dI ( )    + N   - JS    && z   / Jkz       :: ! _n   || a    - ! c         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 308))

	def test_309(self):
		input = """Wf : function array [ 0 , 0 ] of boolean    ( ) inherit x { bES , Q  : auto  = AS   || Y    <= Eh   + N      , v1mt   * k       ;  }    C5 , TR , fK , Rz , P  : void  ;   wx  : array [ 7417 , 0 , 0 , 8 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 309))

	def test_310(self):
		input = """X , Oh38  : integer   = iP ( )    && ! b     % ! ! N      < w   - "\\f"      :: - B   - i     && xf   && L    && n   && zM        , ! cZs    + gAnqy76_ ( )     + ! k   || Y      <= true    % - k   + y       :: o8rM      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 310))

	def test_311(self):
		input = """x : function boolean   ( inherit out z3 : void   , inherit out dB : auto   , inherit out i : array [ 0 , 0 , 5 , 0 , 34_78_1_20_094400 , 0 ] of float     , Y : array [ 0 ] of string      ) { }    b : function void  ( ) { { x , YrPu , GA0H  : string   ;  O  : integer   ;  }   }    GJF  : array [ 65606 , 8_8_0_92_8029 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 311))

	def test_312(self):
		input = """k4f : function array [ 6 ] of integer    ( inherit out wdCxn : auto   , out e8 : void   , inherit C : auto   , out u : auto    ) { return d   + n     :: f   + maKO    >= AGoAc   && a      ;   continue ;   break ;   t2F , q3XKn  : array [ 0 ] of boolean    = DWB   - zUFX    == v4RR   || lGNsk     :: AzlI   % BiZP      , hM    :: lx   && z    >= - nhE       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 312))

	def test_313(self):
		input = """kO , hP  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 313))

	def test_314(self):
		input = """TOCuD , BLb , _4 , s , C_ZBr , M  : void  = - ! Tk   || WvV       :: ! - Le     || ! JhZFy   % gOPvQ      == - - i     && - U    - I   + lH        , ! _   % EG     * ! x    - P   || o      <= "\\f"    - - ! MTSZ        , Zj   + r    || Z    + Su   - O    % N   * iLx       :: ! 0     - ! k   || Y        , ! ! td   + q        , s    :: t   + o    * ! my     - - B     != ! E    + ! - g        , p   / - dLa   / F         ;   j , Y , sy , sKR  : string   ;   LW : function float   ( K : array [ 0 ] of boolean     , inherit o : auto    ) inherit i { Q  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 314))

	def test_315(self):
		input = """e : function auto  ( ) inherit n { }    _  : array [ 1_956 ] of integer    ;   D : function array [ 0 ] of boolean    ( f8u : void   , out VgI : auto    ) { }    YY : function array [ 99551610 , 32_1 ] of string    ( out L : array [ 0 , 9_4_1_87_90 ] of string      ) inherit tO { }    Oc  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 315))

	def test_316(self):
		input = """L , b  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 316))

	def test_317(self):
		input = """di2t , o  : void  = y ( )    + e6G    > { }       , ! H    * s_K4   + V     - A   % uce    / a   + giH      < - d   / yZ    && rY   - D       :: ! - ! g_F         ;   a5Y  : auto  = - - M   + I      > - e ( )        ;   iTVX , M  : void  ;   FJN  : void  = - D   || y    % Y   * C       :: A7C   && wk   && d     * - Fqk   + iP         ;   Y : function array [ 0 , 744020_08_85 ] of float    ( out a : auto   , I : array [ 0 , 0 , 0 ] of float     , out q : auto   , tJ3 : auto   , inherit out B9I : array [ 1_5290449242_5 ] of boolean      ) inherit s { { }   q , iOGz , y  : boolean   = S   - Ty    == 0     :: lwzwV2   || a      , h   / e      , ! p9       ;  }    M : function void  ( ) inherit L { }    GD : function array [ 0 , 5_65 , 1_9 ] of integer    ( ) { }    q , Z  : auto  = - gwXlt    || c   && F     - ! GE   || g      < V ( )    - PRZ   || b    - ! xL        , - Y   && Fj    || - m      > e ( )    % tD   || WqJnm     && ! NOA0    || ""       :: - wTBNUOQ   || _     / - ! Vfv      == - Y    * - Y     + - As    * Na   || ZW5         ;   P : function boolean   ( ) inherit D { continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 317))

	def test_318(self):
		input = """e , I , dh  : string   ;   lEbs , Y , c , r7 , EJD  : void  = I   && XUj    + Ip8Y   && YL     % Z   + FZT    || y   - a       :: - ! il   || nU      > false      , Z ( )     :: - - G    && YdK   || xX        , MLBg   >= ! ! A    && BRMDC ( )        , - ce    && N   % UQ     && - Z   || yz9      > a   || Pf    || - W     - YVp   - j    / 0        , ! - ! T      >= 0.       ;   A  : integer   = d    :: - - f9jrP     % { }      < ! PE    * - M     / ! K    + hHu   && _D         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 318))

	def test_319(self):
		input = """NH8 : function integer   ( AAAPX6 : array [ 223 ] of string      ) { }    BBZ : function float   ( ) { }    R : function auto  ( SuTf : auto    ) { i , JPO , A , RF , i , sF , owmXlY , vc  : void  ;  for ( kc  = - y    >= n7   || SA      , - Tk     :: - X3    <= _a   % Kdv      , k5   + pQo6l    <= - Uvur     :: 0    < kz   + F      ) break ;     }    f  : array [ 0 ] of boolean    = - p   % a    && - x      >= - ! ! U       :: J ( )    > k   / M    && RUr   % b     && ! eM    + - i         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 319))

	def test_320(self):
		input = """qP : function void  ( ) inherit s { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 320))

	def test_321(self):
		input = """p45Q  : auto  = d   % R    - - G     && ! - lvbf       :: mlL ( )    >= f   && Q    || BdB   + E     % ! OVMXJ   && xr         ;   UD  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 321))

	def test_322(self):
		input = """Mk , i  : auto  = y   == ! - B     || zzw ( )      :: ! S   / q     % hnt   - w8yu    / - M      == ""    && YxP   + BnS     % - yga   % sKi        , ""     :: ! A   % Q    + - KT7         ;   sL : function auto  ( ) inherit U { }    bpd1cL : function auto  ( ) { Y  : integer   ;  }    YH  : auto  = 8_64    > ! q   && hMmPsV    + Fe   || sR         ;   D  : integer   ;   ZLeuT , jj , q , R , uuN , Y8 , DfyU , UyRX , Ska , P1 , gr  : float   = z ( )    || OJGTgLWFZ2   - Q    % T   || j      < - EW ( )    % j6       , ! D   - c     + ! P   + Xuc5       :: t   || k   + T    - ""        , ! - x    && - a      != ! yESjT   || Y    * B   && D4Nl        , ! ! ! Y      > ! N   + BYxnbX    - ! sO        , { }       , ! - B     - uT   - R   / zyvUt      <= .7e3      , - - - H        , - - o   || oef      == - ! P   + uN9        , "𑙭"    - hh   && nM    - e   - c        , ! n   % A    - fzI   && ya      > ! mp    && C     :: - U   || zbsN    + KS   - NOM        , U   && C    % ! fT     - V   || x    || my   / V      >= HP2    :: - - aM     || AVGL ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 322))

	def test_323(self):
		input = """c3y : function auto  ( zo : string     ) { J  : float   ;  continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 323))

	def test_324(self):
		input = """IYK : function array [ 0 ] of string    ( inherit M : auto    ) inherit ZrEs2G { }    O  : array [ 7 , 82_9_49_5_9 ] of float    = - v ( )    * - g      <= PW    :: Tv5z   || GT    - ""     || - tD    || E   && I      == - - S        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 324))

	def test_325(self):
		input = """z : function array [ 9_79112975722_8 ] of integer    ( ) inherit X { }    W : function boolean   ( inherit a : array [ 0 , 48 ] of boolean     , inherit V : auto    ) { break ;   while ( D   - N0    <= ! M     :: ! O97IZEcx      ) f9S ( )  ;     Ufbb  : void  ;  }    r  : float   = - ! ! Ri         ;   T , W2xV  : auto  ;   J , Jg  : string   = ""      , ! IAi   || - xek      != ! _3    / t   + A     + 9    - q        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 325))

	def test_326(self):
		input = """qb  : float   = vz   || V    || - X     && R    == ! QmP0f   * vH5db    - R3      :: ! ! ! lG      > O ( )       ;   a  : void  = - ! K ( )       :: - - r   - sUCS      == ! gX   && nJihQ    + - EF         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 326))

	def test_327(self):
		input = """M  : float   = 0    && vDdk ( )    % - D      != ! ! b     - - Nfi ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 327))

	def test_328(self):
		input = """BM : function auto  ( inherit out s : boolean     ) inherit bX { }    GF : function integer   ( inherit out Z : array [ 0 , 6_59 , 8_1 ] of boolean      ) { u , D  : array [ 5 ] of string    ;  { }   a  : void  = ifC   && SCDpix       ;  { }   continue ;   break ;   eKYqV , Vb  : array [ 2_4 , 4_6 ] of string    ;  continue ;   }    V : function integer   ( inherit out ACHSU : boolean    , inherit c : void   , inherit bd : array [ 0 ] of string     , w : auto    ) inherit _PotJfcXU_ { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 328))

	def test_329(self):
		input = """C5x : function auto  ( inherit XM : void   , out G : void    ) { FsG  : void  ;  }    W  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 329))

	def test_330(self):
		input = """ur : function float   ( ) inherit rG5 { return - o     :: 0      ;   }    Iw : function void  ( inherit S : auto    ) inherit n { pBe  : integer   ;  H6E  : array [ 0 ] of integer    = myTrWb   / _       ;  break ;   }    N , kHk  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 330))

	def test_331(self):
		input = """p : function integer   ( ) { }    TB : function string   ( KL : void   , out M : array [ 0 ] of integer      ) { }    H : function boolean   ( ) { }    T : function integer   ( ) { }    b : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 331))

	def test_332(self):
		input = """z3 , k , a  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 332))

	def test_333(self):
		input = """pY : function void  ( ) inherit Dwxo { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 333))

	def test_334(self):
		input = """oV5X : function array [ 0 ] of boolean    ( inherit M : array [ 81 , 0 , 0 , 30_03_533462_1 , 0 , 0 ] of boolean     , inherit Ke : array [ 2 , 8 ] of string     , out G : integer    , Rer : auto   , inherit out gL : void   , inherit out LQ1 : string     ) inherit dA { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 334))

	def test_335(self):
		input = """I : function string   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 335))

	def test_336(self):
		input = """ik : function void  ( out Vy : float     ) { while ( f   / E    <= l   / L     :: h   && a    == R   + Qpw      ) { i  : void  ;  q ( )  ;   V  : auto  ;  }     LgVm  : boolean   = BV   % zoCoROr    < Az0y   || UaU     :: - Csju    >= ! _       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 336))

	def test_337(self):
		input = """t : function integer   ( ) { while ( - Ck      ) { C  : auto  ;  }     }    Ok , XE , qSZ  : array [ 1 ] of boolean    = - - ! S       :: f     , ! ! 6      >= E ( )     :: oZ   < ! z4   % k7N    / sZ   + mUaJ1db0        , - Z   + ZF    || P   - t3A       :: ""       ;   t , yI , A , LRADaA7  : void  ;   Y : function array [ 985_99492 ] of boolean    ( ) inherit e { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 337))

	def test_338(self):
		input = """R : function void  ( ) inherit M7oq { }    q5 , n , LuDq  : array [ 0 , 8_41_1_0869 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 338))

	def test_339(self):
		input = """z , Jh  : auto  = - 8_0_7     == - L    - - z     - h   - - pi       :: true      , H   + RP    - - Nq_R     - 8    && ! X      < - s    && _    / false      :: - _dk   || a1    && m     > ! l   / Kl_Dz        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 339))

	def test_340(self):
		input = """b : function void  ( inherit vT : integer    , inherit i : array [ 0 , 0 , 0 ] of string     , inherit out h : auto   , out Lm0 : auto   , C : array [ 7026 ] of boolean     , out T : array [ 0 , 0 , 6 ] of integer      ) inherit f { }    GO8 : function auto  ( ) inherit N { q  : integer   ;  dy0N9  : array [ 3_85 , 0 , 79 ] of boolean    ;  p  = A   == f   - jXJ     :: ""    < k   - D      ;   }    C0  : array [ 2_64_2_50_1 , 1 , 75 ] of boolean    ;   h : function integer   ( ) inherit B { m , k  : auto  = B   && ZUug0_t     :: j   / KoUk3      , ""     :: v   && AATKJ       ;  }    eDbg : function array [ 60 , 0 ] of boolean    ( ) { dbN , g , JW , W  : auto  = - r      , Zf ( )      , W   % EF    != Cy   || ur     :: XYG   / k      , Una   * q     :: ET   * H3    < N   - s7xzF       ;  }    Od , i  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 340))

	def test_341(self):
		input = """P , SW  : array [ 0 ] of float    = Px   % V   - z    / ! mWO      == ! N      , - mh   - n5    || u   && UUq         ;   w , R8K  : integer   ;   j : function auto  ( inherit out O : auto    ) inherit x { H  : boolean   ;  do { }  while ( cJ   % _df      ) ;   }    s  : auto  = ! HA ( )     + 0      :: ! Vgg ( )        ;   lXl , gqy  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 341))

	def test_342(self):
		input = """odMHP : function void  ( ) { }    wq , P  : array [ 9 ] of float    ;   jk2 : function integer   ( ) inherit _A { }    g  : array [ 0 ] of boolean    = - TSAS   || Wv     % cD ( )      :: I ( )    > q7 ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 342))

	def test_343(self):
		input = """hN  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 343))

	def test_344(self):
		input = """Kj : function auto  ( ) inherit w { }    h  : array [ 0 , 0 ] of boolean    ;   ji  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 344))

	def test_345(self):
		input = """Y , vY , SD , qyBAv , G1vqSGS , ig , oe , jMF , Q , K , yp  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 345))

	def test_346(self):
		input = """t  : auto  = - zQ   && ff    + ! N       :: - - ! B         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 346))

	def test_347(self):
		input = """mS : function auto  ( inherit P0v : auto   , Q : integer    , out v : void   , inherit V : array [ 9_7_63439_66_3 , 0 , 0 , 32 ] of string      ) inherit CZP { y1I , v , G  : array [ 0 , 0 , 9 , 0 , 0 ] of string    = - k      , R   && L    != - d      , f   % dg       ;  if ( NfF   % C     :: uIdH   / J3    != MZ   + t      ) P ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 347))

	def test_348(self):
		input = """R : function void  ( ) inherit vT5q { E  = _p   % pY      ;   for ( Hl  = T   || GF      , x   + V    > - B      , kC   - _q     :: P_b   * f1      ) continue ;     }    i6 : function void  ( x : array [ 5_3349 ] of float     , out a : auto    ) inherit ac { q ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 348))

	def test_349(self):
		input = """Ta4 : function array [ 17_9_921 , 420 ] of string    ( Q : void    ) inherit RdDg { }    U6Z  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 349))

	def test_350(self):
		input = """K  : void  = - Gt    || - QOe2     || ! m    / ! G      <= - ! ""       :: - Nc    + - r_Y2     && R ( )     > ! Qh ( )        ;   Gjv2 , T7 , qdl , G0Q  : void  = ! E_   + ""      > v ( )     :: D ( )    / ! l   || P9      == u ( )      , ""    > SuO   % vmS    - ! alD     - - V    || L   && X        , - L ( )    + z   - m9K        , ! LBb   * o     && N   % _    && - a5         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 350))

	def test_351(self):
		input = """V  : integer   = - ! W    * - L       :: 82813       ;   vN : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 351))

	def test_352(self):
		input = """Eq  : float   = cS ( )    < - - My0   || R       :: BkKZ9p ( )    != - ! Lc     * ! g   + T         ;   F : function void  ( inherit out E : auto    ) { c ( )  ;   do { }  while ( ! FE    > 0     :: ""    != wB   && V      ) ;   N , spJ , co37 , g5kq  : array [ 87_5 ] of string    = fC   * l    != 0     :: tO77RLU   && oM      , YW   - K    < v   && bE_     :: Xe   && m    != S ( )      , t   % XPN      , - iv    >= ! b       ;  An1 , yz , H  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 352))

	def test_353(self):
		input = """uiGe  : integer   = - D    + - Bkz     && ! ! X      != ! p9o   + w     / ! 0         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 353))

	def test_354(self):
		input = """ggY0 : function boolean   ( inherit out jD : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 354))

	def test_355(self):
		input = """W , M  : array [ 9_66 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 355))

	def test_356(self):
		input = """sv : function boolean   ( inherit U : void    ) { }    XR  : float   = - Y ( )     <= { }        ;   y , yR , aWpSR1Eyhb , m  : auto  = W9H   + J    + LcpQ ( )     && ! PI ( )      > - ! _    && t   || wk        , m ( )    < K ( )    || _   && C     + - LY   && HD       :: X   * XT    + iJKAxrlaA   && V     + A    == - ZMi   % WBI     - U ( )       , - ! r4E     % y ( )    * DYX   - M      > i   - mP    || y    || ! U    % ! A        , ! i    / - _zW    || bbM   || v         ;   yTIucKT : function auto  ( inherit out k : auto   , inherit out n : auto   , s : auto    ) inherit hnbN { b  : array [ 81_8 ] of boolean    ;  }    g : function string   ( out S : float     ) inherit MOgbG { TTzAh  = - C      ;   fno ( )  ;   continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 356))

	def test_357(self):
		input = """D_k : function array [ 0 ] of string    ( out y : void   , out l : boolean    , inherit out l : array [ 0 ] of string     , out T : void    ) { }    I  : auto  = - LN    && - w     * ! qXg    + I   + Ci      > - MR   && hf     + ! wh   && y         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 357))

	def test_358(self):
		input = """e : function void  ( X : array [ 6_408_9 , 47 ] of integer      ) inherit RLr { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 358))

	def test_359(self):
		input = """dZ : function float   ( OQ : auto   , out k : auto   , inherit x : array [ 0 ] of boolean      ) inherit E { }    xA83t  : auto  ;   UACs5gmCUA , kX  : void  ;   Xwb_koNu : function array [ 0 , 0 ] of boolean    ( out o : boolean     ) { do { MBVK ( )  ;   JjC  : auto  ;  poc ( )  ;   return ;   x  : void  ;  break ;   ZQF , smY  : void  ;  }  while ( J    :: - S      ) ;   Y , Y , I5 , S , n  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 359))

	def test_360(self):
		input = """J  : array [ 230 , 0 , 0 , 327_04_7 , 6_0_7 ] of integer    = ! lWv    || yd   + A5iU     + ! L   / rk5W       :: ! vQN    || ""     || - FR9CzX   + Q      < - ! aL1   - _         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 360))

	def test_361(self):
		input = """Xcl : function array [ 76574_5 , 5 , 0 , 0 , 0 ] of string    ( inherit X : auto    ) { }    NBJt : function integer   ( ) inherit L { }    E : function void  ( ) { DxO  : array [ 0 ] of float    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 361))

	def test_362(self):
		input = """X : function boolean   ( ) { P  : integer   = ! y8S_b     :: - pSCM0w74       ;  do { }  while ( - hN    >= - v     :: rTb   >= Y   + E      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 362))

	def test_363(self):
		input = """c : function void  ( inherit ZP : auto   , m : auto   , inherit out t : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 363))

	def test_364(self):
		input = """J : function array [ 0 ] of integer    ( inherit out K : boolean     ) inherit S { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 364))

	def test_365(self):
		input = """lI : function array [ 34 ] of string    ( inherit FTD : integer     ) { SMv , w  : auto  = - A    != g   + B      , q ( )    >= - nB       ;  }    g : function array [ 0 ] of integer    ( ) inherit DRB { }    gsk  : integer   = - n    % - c     + - Dm   % A      == ! WuAjFhR   * F     - - - KVh_N         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 365))

	def test_366(self):
		input = """Ywe : function string   ( ) inherit tQ { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 366))

	def test_367(self):
		input = """C : function float   ( inherit out dm : void   , Gx : string    , inherit ztAU : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 367))

	def test_368(self):
		input = """U : function array [ 3 ] of boolean    ( ) { qB  : void  ;  }    p02  : float   = 0     :: o ( )    % - YF    + j   || Ml      <= - ! p ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 368))

	def test_369(self):
		input = """Ah , d  : array [ 0 , 0 ] of float    = ""    || - kfnT    || yL       , - - k     / ! g ( )      >= k   * Ff    % ""     % - - JeSL         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 369))

	def test_370(self):
		input = """GW : function integer   ( ) { MG , cWaD , N , Qp  : string   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 370))

	def test_371(self):
		input = """BE  : array [ 73_0_19_581_20_6_6_4 , 1_363 , 25_0637581_1_31_833 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 371))

	def test_372(self):
		input = """S : function auto  ( out A : auto   , inherit out zY : auto    ) { Nx , lF_ , jR6 , W9db  : float   = F6G   / Co    >= Ly   % krL      , pP   + T      , dRLEAWi   && kRMm    <= xE   * hrJ      , PpD   % t     :: Z      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 372))

	def test_373(self):
		input = """c : function void  ( ) { }    T1 : function void  ( ) inherit xSq { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 373))

	def test_374(self):
		input = """G  : boolean   = UH   % N    || ! SW     / ! bUBA    - - oZPFL      < - - yP    && - bc       :: ! _    / N   / M     - false        ;   YX  : boolean   = I   && uK    + H6   / D     + ! - as      > ! vf    - - H     * tK3BT   + b    / J8a        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 374))

	def test_375(self):
		input = """gb , E  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 375))

	def test_376(self):
		input = """F : function array [ 0 , 84 ] of string    ( ) { G  : integer   ;  }    fU  : auto  = - A   * v    && nU7YIVhccc   + TC         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 376))

	def test_377(self):
		input = """g , w  : auto  ;   GX3 , bQ  : array [ 0 ] of float    ;   O0 , jkH9  : void  = dNnJ4 ( )     :: - FbXMk   + H    * a   - lKqc        , d ( )    <= uQ ( )    || ! JN   - eB1rk3       :: ! ! LZ   % Fs      <= - g ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 377))

	def test_378(self):
		input = """V  : array [ 348_53_497742 ] of string    = zw   / vyqO    * J   + Xd     - K5   || Z    * IT   / J       :: - y   + m     - 0    && G   * y         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 378))

	def test_379(self):
		input = """z : function auto  ( ) inherit op { }    K  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 379))

	def test_380(self):
		input = """lOj : function void  ( u : integer     ) inherit Zh { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 380))

	def test_381(self):
		input = """u : function void  ( P : array [ 88 , 9 , 0 ] of float     , inherit W1E : boolean     ) { }    xYX : function void  ( ) inherit jY { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 381))

	def test_382(self):
		input = """C : function auto  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 382))

	def test_383(self):
		input = """lOy  : float   = ! ! MuqU   / Ac8      >= - TV   % d     || - R    - w3Hz4y   / k       :: ! ! z    + - N78      >= - oK       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 383))

	def test_384(self):
		input = """m , eZZ , AV5D0  : void  = ! ub   * gP     || l      , w ( )      , - P ( )    / rIP5   + E      > S1   - ! Z    + O4rj   && H       :: e   % O    / LpH   + r     && - - M      == ! E3S   + A     * ! u    % - kp6         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 384))

	def test_385(self):
		input = """UNd : function auto  ( inherit C : void   , inherit jsV : float    , k : auto    ) inherit b { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 385))

	def test_386(self):
		input = """mt  : boolean   = true       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 386))

	def test_387(self):
		input = """Nqk , Hzp , JdB , TuLn , Gg , j , Sp  : array [ 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 387))

	def test_388(self):
		input = """i4 , E , ve  : float   = ! - ! o      < - w   * W     || c0   / ! IGv        , _     , ""    % P4   * Ep     / uo   || KK2    || B   - _Vl      > AW   + U    && P   && vpE     || R   || N    && L ( )       :: A   <= - KwP   / PQ     || ""    + j   && t         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 388))

	def test_389(self):
		input = """I1pp  : auto  ;   Z , ko  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 389))

	def test_390(self):
		input = """b , UUp , Q , d_u , Rc , f  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 390))

	def test_391(self):
		input = """Kw , RgS  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 391))

	def test_392(self):
		input = """K1ul : function void  ( inherit out P : integer    , out Y : void   , AyUI1 : boolean     ) inherit Nb { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 392))

	def test_393(self):
		input = """D , LF  : auto  ;   b_N : function float   ( ) inherit E { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 393))

	def test_394(self):
		input = """q : function void  ( ) inherit D { }    N : function void  ( O69 : array [ 759_200_3_9 , 0 ] of string     , b : auto   , inherit c : auto   , u : array [ 4 , 2_6728 ] of string     , inherit out y : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 394))

	def test_395(self):
		input = """fHf , P  : array [ 1272 ] of string    = FrD     , vc   || - Q ( )       :: b   || lE    % H   || fkb     - x ( )    / ""      != - ! ! H         ;   oh : function void  ( ) { }    aK  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 395))

	def test_396(self):
		input = """d  : integer   = G1   % j    + IXM   % eqdfM     && - Z9SvZ   - Q3eU3xed       :: ! - or   - OOz         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 396))

	def test_397(self):
		input = """U  : auto  ;   MeIm : function array [ 18_013_48_718_50 ] of integer    ( ) inherit YsdDQd2 { }    Qo  : array [ 8 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 397))

	def test_398(self):
		input = """Cp , P , o  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 398))

	def test_399(self):
		input = """gipG_l  : void  = L4   || CN    || c   || s     + ! m   + O      <= true    + 0        ;   q : function boolean   ( out pZzkL : array [ 0 ] of string      ) { }    i : function string   ( ) inherit SBe { Nuj , Qw  : void  = ""    == Ur   && I     :: ds   + FqDpcmT    <= f5Ubs   && r      , kj   + O    != - M       ;  q , A , s , Z , e , a , x , R , J , Qvhd  : auto  = t1   - k    != My     , N   / xMo     :: V_u1   || H      , aZA ( )      , ! uF8     :: ""      , ""      , d   || OvoR    == - g8UaC      , t   && d     :: x   - nWB    == qP2   / WX      , E   - _     :: S     , QYHJW   / d8     :: t   + SL    != ! _d6      , C ( )       ;  }    Zm : function array [ 8_35_00_5_0 ] of string    ( inherit eH7 : void   , Cd : auto    ) inherit fD { }    k  : array [ 65_798 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 399))

	def test_400(self):
		input = """xnS , obV  : void  = lSH ( )      , - ! Sl    || ""       :: H   % wL    % d    * ! W   || M      >= - W   % wdz     || - b   % h         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 400))

	def test_401(self):
		input = """z  : integer   = ! ! d    + TG8   * E8      != - "\\\\\\r"        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 401))

	def test_402(self):
		input = """YUM : function void  ( W : array [ 4 ] of integer      ) { Fq , T , n , o , ONM , c , q  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 402))

	def test_403(self):
		input = """JV , D6J  : array [ 56_3719 ] of integer    = ha   + H   + xO     / NUH   + P   % e      > false     :: R_76m   || { }        , ! 8    / s   + IaMq      == - xKo7w    || ! M   || Z0       :: l ( )       ;   Ca2  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 403))

	def test_404(self):
		input = """e : function float   ( inherit out Y : auto   , inherit out G : void    ) { for ( D  = v   || x     :: G   || s      , ! y     :: - O8N    >= t   - y      , - L5Jf39    > woWh   - GXZL      ) M ( )  ;     Jv , U  : float   = ! MJHyfg9    == Ur   + Z     :: wvKM   + f8o    > h   % R      , - oE     :: l   || p0T       ;  }    Lu  : string   ;   P , Wt  : string   ;   HuBw5nJ5n : function void  ( ) { AIQ  : array [ 0 , 96_9 ] of integer    ;  for ( qSX  = jpNsJPFX   || f     :: o   != m     , - X    == fBT   * F      , ! h     :: d   || g4      ) return ;     Kx6 ( )  ;   xY , V9S , S  : auto  = ""    != qMlDVD4   && H      , zei   - E    == 0      , r   && EU     :: k ( )       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 404))

	def test_405(self):
		input = """z  : array [ 0 ] of boolean    = - ! N      :: ! - aA    * ! hFe         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 405))

	def test_406(self):
		input = """Ar : function array [ 0 , 0 , 8_548 ] of string    ( ) inherit n { }    C3SLT : function integer   ( inherit out Now : float     ) { do { return ;   c7x , OK , IvL , X  : float   ;  return ;   }  while ( Ml   * K1    >= - eR     :: ! qD      ) ;   { }   if ( - El      ) continue ;   else { }     }    i  : void  = zX   + j1D9    / zQ   + c     - ! XjDh    - ! g         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 406))

	def test_407(self):
		input = """G : function void  ( out UO : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 407))

	def test_408(self):
		input = """r : function string   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 408))

	def test_409(self):
		input = """WB  : void  = ! v     :: ny      ;   p  : float   = J5 ( )    >= k   - p    || ur   / qt     || ! B    % B   % aRw         ;   o  : void  = ""    >= - ! G    % Rss7   - kR       :: - - ALnM3     * M   / o    || O   || y         ;   CpD : function void  ( ) { }    Y5kG2 : function void  ( ) { t , V  : string   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 409))

	def test_410(self):
		input = """_ME , l9tC  : array [ 91 ] of float    = - h   - FI    / ! T        , U   % SNG    * GL ( )     - - - xKqdTn       :: - Dxkjb    && C2   - w     - ! e    + NtVC   / F         ;   g  : void  ;   D  : boolean   = ! pyl   + P6     - i   % el    || - aVN      != { }        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 410))

	def test_411(self):
		input = """G , U  : array [ 0 ] of integer    = - ! z_Fc    + tt   * K        , - - e7L    || tr   % V         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 411))

	def test_412(self):
		input = """RTTr , hC  : auto  ;   X : function boolean   ( ) inherit C { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 412))

	def test_413(self):
		input = """d : function void  ( ) { }    n , Zg , GnY , n  : array [ 0 , 2_46_1_70686_8 ] of float    = 7.E5     :: - T   + Q   / L      < NM   || tnd   || Y    - C   % Uo        , - _   * nVn    || d ( )      >= Cw ( )     :: ! QE   * d     - H      , ! mev    || N   - poi     - U   && D    || ! op      < - ! ! C        , - j   && uM    && HcB   && he         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 413))

	def test_414(self):
		input = """x : function void  ( ) inherit U { _  : void  = ! u    >= jm   * R       ;  s24  : auto  = ""       ;  break ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 414))

	def test_415(self):
		input = """n  : auto  ;   PKd , kBvG , z , im  : float   = - ZfN   - UiD    && ah   && k      < ! uj   % GX_     - ! KZ   + CT        , C   + J    && - n     || - Bfh    / ! Z       :: ku3   + i_c    && ! jOvfKlH7     && - O ( )      <= Lt   / ae    - y   * j     || - ! c        , ! - B   - eJ        , l2   + - MD     / L   && oB    + s0l   - zzn       :: KJq3   + d   * n     % - x    + Y   || JR      == { }     || VA   % F    || CJG        ;   n , rR , a , J  : void  = ! myjC    && n   / w    % - d8        , - 0      :: ! ! - u      != "\\f𫜵"      , - D   % P    && ! jat       :: ! - K    * o2       , ! k    + ! z     || xgT ( )     > - BmaU08a    && L    || ! EVF8p        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 415))

	def test_416(self):
		input = """Iy , Z  : auto  ;   B , v , uGHESQ  : auto  = ""    <= - ""    && X   / lE       :: v ( )    == - ""    + r       , - n    / ! Zne     || F   && K    + A6   / S3tmaJQ      == - loPm   / J    + - gs       :: s   - pM    * - z     + q   / zy    && A     >= ! - a     + ! Oo    / ae   + S        , A ( )     :: - bqUt ( )    - - hfv      <= - - hj    + ! tB4         ;   yS : function void  ( rjU : void   , out P : void   , inherit BigOO : void   , inherit out tY : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 416))

	def test_417(self):
		input = """gnF : function string   ( ) { O , a , E1 , r , LIT3  : void  ;  }    EuoCZp : function integer   ( ) inherit b { }    Jhp8 : function void  ( z : boolean     ) inherit Q { do { }  while ( sG   && G     :: - H      ) ;   }    PjbQ : function auto  ( ) { h  : auto  = - B0    <= RM7cC   || eXW     :: - uPv6       ;  Fy ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 417))

	def test_418(self):
		input = """CCioF4  : array [ 54_0_3_14_28_89 , 8_4 ] of string    = j   % eKy    && AZO5   && K     % - V    / v   && G         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 418))

	def test_419(self):
		input = """Ul : function string   ( K : void   , out rmO : array [ 425_7_2 ] of boolean      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 419))

	def test_420(self):
		input = """geO  : string   ;   u7  : array [ 0 , 0 ] of boolean    = ! true        ;   Z4 , B , J2  : auto  = ""    && dW0   / KQ8v     + ! HZi   / P       :: ! kFg    - 1     - Jg   * Na    - E   % z      < - - T     || ! eN9    + - X        , IAiP   / - ib    / TqO   || Q        , - - _9   % o       :: - B ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 420))

	def test_421(self):
		input = """T : function float   ( inherit uW : integer     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 421))

	def test_422(self):
		input = """_e , Y8  : integer   = ! KqZh0   && Eu    || 0        , "\\"𞀇𞺊\\n"       ;   b  : array [ 0 ] of boolean    ;   Cf , f , TmVb  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 422))

	def test_423(self):
		input = """N , N , Et  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 423))

	def test_424(self):
		input = """rVyh : function auto  ( ) inherit N { do { }  while ( ! m     :: ""    < f   - Q      ) ;   for ( J  = ! m     :: fqp4   / F    <= ""      , B   + PS      , ! DQlJq    == Es   || Yb6      ) return ;     if ( BiMJ   + O      ) A ( )  ;     F , Ea , cE  : void  ;  dP4 , v  : void  ;  }    n  : integer   = - - x6s    * i   * p      != - h   + I    - ! Q         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 424))

	def test_425(self):
		input = """a3 , Vn  : auto  = - G2 ( )     || p   / z   - MX87m       :: r ( )    != - - Z   % I        , - - ! D       :: - vQl   * q    - k   && z      < - - ym   - LmE         ;   nV , M , q3 , DQm , aa , n , zc  : void  = ! P   * V     || ! Iv   || d      <= I_M ( )    || ! oUCv     - ! 0        , - - H   % R      > ! - i       , ! E    < E     , - ! r   + y       :: ! - Gy   || l8        , 0E20    == ! ! D     - ! ""       :: fy   + q    % ! u     + j3 ( )     <= ooYq ( )      , ! - i61     - yx   || yWbib    || CS9SJ   + t0      <= - ! DG    || - C       :: - P    + ! L     || ! vO0    || S   / G7H_        , - ! Sv     || - I     < - Qx   + x     + ""    / ! qify         ;   u  : float   = - N89F    + - V     % Z   + j    + ! S       :: - T    + ztM   - eB     || ! ""         ;   U : function void  ( inherit out jcP : void    ) inherit j { t , fG , o  : string   ;  }    udmU : function void  ( inherit j : array [ 6 ] of boolean     , X : string    , inherit out N3 : void   , m : array [ 0 ] of integer     , out i6K : array [ 61 , 0 , 18 , 0 ] of boolean     , inherit Lpn : auto   , out pbfk : void    ) inherit D5 { nahn  : integer   ;  do { }  while ( e   % apw     :: DA   && f    == d   + PgW      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 425))

	def test_426(self):
		input = """g , c  : auto  = oz   + im    / r7BTi   - Yp     - W    >= By    :: ! ! Yvu     >= - kL      , n ( )    >= ! - E      :: Kxh   % ! ! yzbm         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 426))

	def test_427(self):
		input = """T  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 427))

	def test_428(self):
		input = """ye : function array [ 0 ] of float    ( T : array [ 5_6 ] of integer     , inherit kR : boolean    , cG : boolean    , inherit out z : auto    ) inherit Ar { d3 , E , T  : integer   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 428))

	def test_429(self):
		input = """l  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 429))

	def test_430(self):
		input = """q , AP , J1Un , a  : void  = I   / z   - Qf    && ""        , - uT   * ZNBB_    / ! yZ       :: - y   || Z     - - - gG      == ! ! D   && D        , - M    * YN   * aj     * ! T1    || - Z      >= ! L   || vRK     - L   - TA0N9L    || rOrF ( )       :: h ( )    + 0     % ! ! F        , P   + f    + ! v22B     * pFT       ;   X_d : function array [ 3 ] of float    ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 430))

	def test_431(self):
		input = """Ft : function auto  ( ) inherit lI { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 431))

	def test_432(self):
		input = """X , e  : array [ 91 , 89_81 ] of integer    = - ! z    || - BePro        , b   && d    || W   * Ntr     || ! rTU   * yJ      < 0.34     :: - - W     || - y   + a      > ! ! ! U         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 432))

	def test_433(self):
		input = """Dz : function array [ 8 ] of string    ( ) inherit o0 { T , PW6 , m  : auto  ;  break ;   }    m , gp9 , W  : array [ 3 , 0 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 433))

	def test_434(self):
		input = """j : function string   ( ) inherit J88e { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 434))

	def test_435(self):
		input = """V : function array [ 0 ] of float    ( ) { }    B9utZyS4KfK : function void  ( inherit out U : integer    , inherit out N : auto    ) inherit O { }    VEfZ  : array [ 861 ] of string    ;   M , wQ , Ev , HUZp  : auto  ;   ZE , Z2WshKgL , l  : array [ 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 435))

	def test_436(self):
		input = """EX  : auto  = .78E+297    <= - uqnH    * F ( )        ;   n , s , lKT  : void  = j   / G    || dLB   && un     - 3    * Qt   / g9p      != c   - P2    - ""     || - E6   + f       :: - - OC   && u        , - - v     * - Ti   % zn      >= v   + J    * u6   && vd     + { }        , hMW      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 436))

	def test_437(self):
		input = """b : function string   ( inherit out Bjs : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 437))

	def test_438(self):
		input = """h : function array [ 1 ] of integer    ( ) { break ;   K , q  : array [ 0 ] of integer    ;  if ( e   || a      ) break ;   else { }     E , Uat  : auto  ;  gJ2t , Ur , eH  : auto  = xIi   * h0Q4      , ! HY    == ab   * B      , - Ax8    > ! W     :: X   && SW    != - O3       ;  pB , QY  : boolean   ;  }    w  : void  ;   VCR : function void  ( out h : void    ) inherit O { cP4Ceo , PS  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 438))

	def test_439(self):
		input = """gW : function array [ 0 , 68_2_71_8 ] of string    ( I : array [ 8_366 , 0 , 75_383 , 0 , 1 ] of float      ) inherit XIiC { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 439))

	def test_440(self):
		input = """k  : string   = - ! - B       :: - ! V    && Y   + b         ;   l  : array [ 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 440))

	def test_441(self):
		input = """A , Mp  : string   ;   x  : array [ 0 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 441))

	def test_442(self):
		input = """C : function void  ( inherit Fvig : void   , QM : auto    ) inherit Z { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 442))

	def test_443(self):
		input = """Zw : function void  ( inherit out sJQ0 : auto    ) inherit v { _ , q  : integer   ;  To , InH  : void  = f   - yV    >= i   - t      , mM   - GZ     :: JX      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 443))

	def test_444(self):
		input = """b  : void  ;   U  : void  ;   Bp , o , Cv  : void  ;   y : function string   ( ) inherit fc7 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 444))

	def test_445(self):
		input = """xxfJfF : function array [ 0 , 0 ] of string    ( ) { Vp , r  : boolean   ;  k ( )  ;   l0  : array [ 28 ] of float    = d   * w       ;  AY  : integer   ;  q , j04G  : auto  ;  for ( FfSg  = n   + l     :: 3    <= ! X      , GwtKM ( )    <= - YI     :: s6p   + lR68    == Z   && sK      , - e    < ! kWD     :: u   * eXe      ) continue ;     }    n3  : void  = - - n     * ""    % ! pB         ;   z  : array [ 1338997_49590 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 445))

	def test_446(self):
		input = """u , i  : void  ;   d , Z  : array [ 7 , 0 , 65_160 , 0 , 9_7 , 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 446))

	def test_447(self):
		input = """J  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 447))

	def test_448(self):
		input = """ew  : array [ 221188_27211 ] of string    = T   != ! yh   * xn     + Y4   + w    / r   * u       :: - YZ    || - opH   - T         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 448))

	def test_449(self):
		input = """I , S  : float   ;   Si3i : function array [ 4 , 0 ] of integer    ( out p2 : array [ 0 , 6_36 ] of integer      ) inherit z { }    Q_ : function auto  ( ) { qK  = hY   / E    >= hf   || b     :: x   / rtR      ;   O7 ( )  ;   for ( X04  = SfL   && V    <= ! sJ     :: PG   * r    > oB   && S      , ! ex    < j    :: lVQFwso ( )    != JiiAj   / hvcqnxaF      , ""     :: o   * _    != jif   + x      ) E ( )  ;     xO , pts  : array [ 3 , 473 ] of float    = wW   + Br    > UT   % r     :: h   / Y    != z     , Z   && Y2D    > - X8Ydw     :: B   % WXMb9    >= - O       ;  break ;   W  : integer   = ! Li     :: - w0    < X   - dLB6       ;  JPkEAZ , R  : string   = - Z     :: rZ   * U    < YP   + y      , En   * Xw       ;  g  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 449))

	def test_450(self):
		input = """fUw , rE , l  : string   = Q ( )    + - h5y0   * _B        , c1   <= - i   + KB     / false       , ! - OPP     || j   % o    && u   / DKAf5F      < - - DQ   || _       :: ! - PON   % iXPl      < - - W   || S8f         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 450))

	def test_451(self):
		input = """rY_ : function integer   ( G : auto   , out at : array [ 0 , 7548_088_289 , 887551 , 82 ] of integer      ) inherit xQ { eA ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 451))

	def test_452(self):
		input = """Q , oN  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 452))

	def test_453(self):
		input = """s8 : function void  ( inherit V : array [ 0 , 0 ] of integer     , E : boolean     ) inherit vP { c_ , UM  : array [ 6 ] of boolean    = ! g      , ! JN    <= BQ   * bK     :: t   - _f    > V      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 453))

	def test_454(self):
		input = """UEb : function boolean   ( ) inherit t { do { }  while ( - h    < 3     :: R   % E8    != hDK   + vq      ) ;   r3v , f , I , WQRO , W5MWU , o , WT  : void  ;  MH  : void  = qxx    :: QVf   / I       ;  }    f : function float   ( inherit out U : array [ 0 , 6 ] of string      ) inherit VS3 { }    B : function boolean   ( inherit j : void    ) { wM ( )  ;   return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 454))

	def test_455(self):
		input = """GX4 , Cb4R  : string   = ! ! E    - ! w4SV        , - I   + xb     / J ( )     >= - - n   || XyIAC         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 455))

	def test_456(self):
		input = """s : function array [ 0 ] of float    ( ) inherit b { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 456))

	def test_457(self):
		input = """b  : array [ 0 , 5 , 69_27_6 , 0 ] of boolean    = - g       ;   tG , H , m  : integer   = ! Oe   || y39RgEgw5     || p   / Ihq    || sD   && i      == ""     :: v5   % Bv    + j7 ( )     + - 0      < ! 0    + b   + O        , Vj   - pE6BA    + U   || E     - ! - Gc      <= - ! ! rsd        , - J    - yO    * gUac   / F7z    + ! H9l      == ! Yw1    - ""     % Oo   / bY    - ! _4       :: h   + _    + ! id     - ! D    + - PbqU         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 457))

	def test_458(self):
		input = """o , qJD , ZI  : boolean   ;   _  : array [ 7_24 , 0 , 7 , 86_98_60_1 , 4 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 458))

	def test_459(self):
		input = """Q , dx , U , em , O  : integer   = p2   <= zJ9     , PN   / U    * 0     + ! ! fP       :: A4 ( )    > { }     || y   - yIsfaC    + oqJ_DB   - h        , - J    || R   * v     / ! Cg0    || ! om        , x   || Pz    - A   || cx     * ! UX ( )       :: 0      , ! nqIfre    || - nfh     && { }         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 459))

	def test_460(self):
		input = """ERX : function auto  ( ) inherit G { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 460))

	def test_461(self):
		input = """eZ : function string   ( inherit S : integer     ) inherit YZ { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 461))

	def test_462(self):
		input = """A : function array [ 0 ] of string    ( ) { D , X  : auto  = zP   + i     :: sfvB   && Y4    == K   + SL5Rve      , D ( )    != ns   - W     :: ! kd33a       ;  U  : auto  = - p       ;  }    S : function auto  ( xKU : integer    , inherit out x7Q : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 462))

	def test_463(self):
		input = """Dj , L , E  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 463))

	def test_464(self):
		input = """q9 : function auto  ( rB : void   , inherit out e : array [ 2_9_608_4_1 , 0 ] of integer      ) inherit u { }    v : function void  ( out fGiLVc : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 464))

	def test_465(self):
		input = """j : function boolean   ( inherit out k2Qx : array [ 267_6_2 , 1_277 ] of float     , H6 : array [ 48 , 2 , 0 , 59 , 4_5 ] of float     , inherit out E : auto    ) { break ;   mF , W , y  : string   ;  gX  = cW   || M     :: ! M    > ""      ;   Ek  = - r    <= R   || w     :: ! i    <= - qR      ;   d  : array [ 80620_3 ] of boolean    = - F       ;  YoJ , zllmwoA  : void  = Y   - o     :: P   || oRc    >= ! h      , 2     :: ! ODlz    == - ZB7zlV       ;  Z , SU  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 465))

	def test_466(self):
		input = """U : function void  ( cY : auto   , inherit out k : string    , out V : void   , inherit out wn : void   , out XMJ : void   , inherit out O6 : array [ 4_65 , 0 , 44_31 , 0 ] of boolean      ) inherit eA { X , kq5Gc4  : integer   = - T8    <= ""     :: mI ( )      , - x    > Rvdmo   && I     :: ! Q_       ;  Ha , w  : auto  ;  Pa , N  : auto  = a   / dY     :: V   * W      , ""    >= w   + ZV     :: A32XKM   % _CW       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 466))

	def test_467(self):
		input = """Ro : function float   ( inherit wD : boolean    , out r : string    , r : auto    ) inherit dHUcH9 { A , Ast  : void  = r   && Ey    == 7     :: fm   - b    < lP   && H      , 0     :: YsXaXV   / fb    > ! iI       ;  }    f : function void  ( ) inherit Stxo9X { }    A_ : function void  ( O : array [ 0 ] of string      ) { S  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 467))

	def test_468(self):
		input = """G : function array [ 0 ] of integer    ( ) inherit v0h { }    ne : function auto  ( ) inherit M { return ;   break ;   iP  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 468))

	def test_469(self):
		input = """_M4  : string   = - ! o   && S      > - cW   && bgq   - o       :: ! ME   + x    * ! yIX         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 469))

	def test_470(self):
		input = """cB  : auto  ;   i : function float   ( ) inherit C { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 470))

	def test_471(self):
		input = """Bjk2 : function array [ 8_6 ] of float    ( jYw : void   , out c7 : auto   , inherit O : integer     ) { if ( 9    > v1   + jq      ) continue ;   else { continue ;   }     if ( ViwEakJ   - E    <= ""      ) { iW  : void  ;  }     break ;   F , u , b , Cy , Xq , YO4 , N20 , Q  : boolean   = u   - _     :: - P    < AizIoQOKh8z   && PE      , 5    == S7   && b     :: ! jb    < P   % lF      , ! g    >= k     , ! JX     :: ! C0A      , Tf   && gI    > H   % O      , ! F    <= T   || ji      , M   && HXn9JTT     :: - i      , l   - z     :: ! dD       ;  v  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 471))

	def test_472(self):
		input = """GF : function void  ( ) { y  : auto  = G   + l       ;  }    W , Y  : void  = z   || H    % l   / Kkohg     % s ( )     <= - Z    && - A   - e       :: ! R    || bR   || r    * ! L      > - - Lf     || kW   / N    * N   % w9        , d ( )    > ! ! c    % - M         ;   lj : function string   ( ) { }    h : function void  ( ) inherit z { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 472))

	def test_473(self):
		input = """N : function array [ 0 ] of boolean    ( ) inherit Q_r { Z , No , pPR  : auto  = - F     :: i   && e      , Hu   - sI6K      , w   / Q2       ;  if ( o    :: i   || ac      ) continue ;   else { }     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 473))

	def test_474(self):
		input = """B , m , k  : void  = ! ! S   || vVA        , ! ""     || ! zv    || ! R        , mQLEHs   && e    && T   / Px     || S   && _qq    || m   - oe      <= - - ! hF       :: O ( )    * PSIwj   + U     % ! psEO    / W   - E      < Bk8   * bW    && ! Y     && Mdci   && d    + eMmT ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 474))

	def test_475(self):
		input = """yx  : auto  = - i   - Z     && SJwz       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 475))

	def test_476(self):
		input = """mbJEo : function void  ( inherit jq : float     ) { O7 ( )  ;   for ( Jg  = e   - T    >= ! C      , RcAvv   || K    <= 6      , k   && E    != j   - j      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 476))

	def test_477(self):
		input = """t  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 477))

	def test_478(self):
		input = """H , WWV  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 478))

	def test_479(self):
		input = """Z , sxek , DZD8 , w , i , JgF  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 479))

	def test_480(self):
		input = """N2 : function string   ( ) inherit s { return i   - Q     :: ! NE      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 480))

	def test_481(self):
		input = """g , BU  : void  ;   S : function array [ 0 ] of integer    ( out L : auto    ) inherit bc { for ( T  = ! hap      , C   && w    < NG   + nT6lrmZCuI      , E   % H    == - X     :: XU6   - dU      ) S ( )  ;     if ( Qx ( )     :: Mzx   - sT      ) { S  : void  ;  { }   yK , E  : void  ;  }   else iQW1 ( )  ;     Y  : void  = ! PI42    < mT   / RR       ;  }    S , lG  : void  ;   m , GE , Ibwxi8 , V  : float   = n   / - b ( )      > 2_559e9      , qG ( )    || ! ""       :: - ! Hsb   - M        , - Vc    / ! J     - Rc   - DGP    - n   / i        , st   + l ( )     >= H4Z ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 481))

	def test_482(self):
		input = """iX4  : array [ 0 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 482))

	def test_483(self):
		input = """N  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 483))

	def test_484(self):
		input = """xp_  : string   = ""    == - ! gC7   + pI         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 484))

	def test_485(self):
		input = """tI , NH  : auto  ;   X3 , YlAN , w  : auto  = - FxZ ( )       , pyI   - Z    % kL   || x     || X1   - f    || X ( )        , - ! ss    || ! jfPj      < - w   && d     || ! ! eoH         ;   f , iV  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 485))

	def test_486(self):
		input = """X  : auto  ;   H , Pxa_K8 , WCa , WL , f  : void  = orX    :: ! P2Gc0EfWTK    || - Oep     % - Y    || - Un8gAF      < ! V   * N    / jc   || yO        , ! - v   / A2       :: ! c   && Q5D     * ! X   && D        , ! - - z      > ""    / S   - Hc     + - K ( )        , - - Gh    - ! qVZ      >= - b    % Hz   || J     && - r    + - RooKn        , JR3VU ( )    % E   + L     / - G    || c   * vm      > Z      ;   eK : function float   ( inherit out m : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 486))

	def test_487(self):
		input = """Xo , V  : array [ 9_2_0_1 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 487))

	def test_488(self):
		input = """j : function void  ( inherit out f : auto   , d_6 : string     ) inherit C { }    f4  : void  ;   Q  : void  = - Y   && AoEg_     - ! Q    && Py8   + a       :: ! - - vd3J         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 488))

	def test_489(self):
		input = """jH : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 489))

	def test_490(self):
		input = """rFnu , v , M , A  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 490))

	def test_491(self):
		input = """xVrr : function array [ 96 ] of string    ( ) { y  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 491))

	def test_492(self):
		input = """L  : array [ 0 , 0 ] of float    ;   f : function integer   ( inherit out S : integer    , out hS8m3M : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 492))

	def test_493(self):
		input = """F : function void  ( ) { X  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 493))

	def test_494(self):
		input = """kBB : function void  ( ) { }    G : function auto  ( R : void    ) inherit dm8 { do { r  : boolean   ;  }  while ( - Gd     :: 2    > m   * Q      ) ;   }    pzC , p , u  : void  ;   F0I : function array [ 2659 ] of string    ( inherit JXG : integer    , out zo : auto    ) inherit E8 { }    B  : auto  = d   && a    % A   / txD     / ! Cm    / 0      != ! - ik   || V         ;   Q , bS , iz , p  : void  = l   + ! T5   || y      >= - d ( )       , - "\\b"       , m ( )    + - x   - b        , B   && uBE    * bQof   || xB     * ! - C      <= ! - ""       :: - AFFPy5    * RY   - b     * w6   || d    || ! Is      > 88       ;   LK , h7 , Vj6 , z  : auto  = ! ! ! y       :: ""    || n   + E     / - g   / UFvhO      < - - e    && - S        , e     , ! - A   - tZFg        , ! - L   * K_      > kw41 ( )    + B   % p    || - dj       :: { }     == - es   && W     - ! R   - M         ;   ciZx  : boolean   ;   _  : array [ 4 ] of float    = - x   && PSj    / J ( )       :: b ( )    && ""    && I   - e         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 494))

	def test_495(self):
		input = """EEP : function integer   ( out Wh : integer    , inherit out Bn : void   , inherit D : array [ 3 , 0 , 9_3_44 , 0 , 0 ] of boolean      ) inherit n { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 495))

	def test_496(self):
		input = """W : function boolean   ( inherit out k : auto    ) { }    AZ : function integer   ( ) { kau  : array [ 0 , 7_7578 ] of integer    = 0    <= g8    :: Pw1JP   - aiG       ;  _  : void  = - N    != V3m   && HD     :: i   / ye    <= ! g       ;  return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 496))

	def test_497(self):
		input = """v : function auto  ( y : array [ 0 ] of string     , out Lz : integer    , inherit _1K : void    ) { y4  : auto  ;  }    U  : array [ 0 ] of string    = ! - mn     < ! ! j     + ""    % - Bq         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 497))

	def test_498(self):
		input = """k  : auto  ;   O : function boolean   ( inherit d : float    , inherit LO : array [ 0 ] of float     , out U : auto   , inherit out L : integer    , iB : array [ 12_0_5 ] of string     , inherit out v : void   , P : array [ 25_5_9928_7 , 0 , 1 ] of float      ) { }    aRYner : function array [ 0 , 0 ] of string    ( inherit j3S : string    , Fgy : auto   , e : array [ 67 ] of integer      ) inherit N { }    w1QEt : function array [ 0 ] of string    ( G : array [ 794 ] of integer      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 498))

	def test_499(self):
		input = """T9K5  : array [ 0 , 0 , 4 , 6 ] of boolean    = - uY   - P     + o   % RS    * ! w      == .6497E3     :: C   + FizW    - ! F     / E   && Hm    * - L         ;   bL_bi7  : array [ 0 , 8 , 714037 ] of float    = L   <= - ! JG    && EiG   && Qxd         ;   B2 : function void  ( ) inherit Cd { GYyP7  : array [ 3 ] of string    = 0    != SwTxGM   * pBX       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 499))

	def test_500(self):
		input = """YJKg : function void  ( inherit r : void   , inherit u : array [ 0 , 0 ] of float     , out c : void   , inherit out V : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 500))

	def test_501(self):
		input = """FEw , pH  : void  ;   d  : array [ 433_64_77_70 ] of float    = ! x   || EAyUoFQ     / ! k    / - hFx       :: ! ! Gy    && - k7      != - - ! A3         ;   Iv4 , q  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 501))

	def test_502(self):
		input = """xw4E : function auto  ( ) { }    B6S : function array [ 6952_9_94_9_93246 , 956 , 0 ] of integer    ( ) inherit dNOE { f  : integer   ;  WE , Zb  : void  = - BV    <= h   + EB      , O   && n2    > lP   && ha     :: ! BDO       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 502))

	def test_503(self):
		input = """V : function float   ( ) inherit Tlu { S  = ! U9     :: ! f5T      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 503))

	def test_504(self):
		input = """_tM : function void  ( inherit JU : auto    ) inherit Ps { T ( )  ;   }    R8 : function void  ( ) { }    l  : array [ 775 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 504))

	def test_505(self):
		input = """gD , C , X , FC_3 , f  : string   = ! ! v     * M   - _    % ! C       :: ! BzF2   || Kh5lC   + Wa8        , ! ! A     % - h   - d1SsZ        , Y   / k    && - DK4     - ! - B        , - iFtX   % G   * bghM      != - ! XB    && GE   * bo       :: - DQ   / ln     + ! G1   && g        , - "ࢠ"     > dkc1K   - MshHD    * - F     && UiA   - EPv    * K ( )         ;   JJVU0Tfm  : array [ 0 ] of boolean    = ! ! zK1c    - ! v      < - - N    + ! zX         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 505))

	def test_506(self):
		input = """VhEvt  : string   = iyL   - - N     + - A   || Kd3      <= ! V   + Z     % - J    && vH   % W7       :: nlf   + j3    + _   * tNtahf     * ! w   || yqx         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 506))

	def test_507(self):
		input = """eBj , Ev , U , L3  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 507))

	def test_508(self):
		input = """qP : function void  ( A : array [ 6 ] of float     , out d : string    , inherit Un : float    , C : array [ 0 ] of string     , inherit out r : void   , VUg : integer    , inherit out g : auto   , inherit Y : array [ 0 , 7_615_3_01 , 0 , 0 , 0 , 7 , 70_6 , 0 ] of integer      ) inherit ap { }    j0grIRcTfb : function array [ 0 ] of string    ( ) inherit x { }    B : function integer   ( ) inherit R { for ( D  = - G    >= ! u0E     :: v   == y     , s   - p     :: - C7    <= fg   - i      , ! tf    == E    :: b ( )    == u   * sp      ) { break ;   }     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 508))

	def test_509(self):
		input = """D , hU , apXi , g , vS  : string   = - rg    && Qw   - o     * - IS   + cshE      <= ! - Z2l    - 1       :: R4Op   * Px    || V   || hym     && vPLV      , ! ! j     - j   || e3u    / OH719     == - - b     % l   || Z    && h   && QdXqI3UUnFGHPiU        , e ( )     :: - H   / z     + n ( )       , - - d    && p   % P1        , - a ( )    && V   && v      != - ! O     && - ! g8YR       :: ! wP   || c     || vx   || a    || ""      != ""       ;   XJE : function array [ 0 ] of float    ( rW : auto    ) { B  : void  = fbhx0l   && Cu    != qa   * T     :: ! zc       ;  tYi  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 509))

	def test_510(self):
		input = """Fg , M , Zq , pE6  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 510))

	def test_511(self):
		input = """UG : function auto  ( C : array [ 0 ] of float     , AaEf : auto    ) { K , rOEM , VP , C , C , K , U  : string   ;  v , DD , q  : integer   = ! F     :: - q      , t   != - p     :: C3   + N    == Sszv     , D   || S    <= vkl   * w       ;  }    T : function void  ( c0 : array [ 0 , 0 , 0 ] of boolean      ) inherit dAZ2 { }    k : function boolean   ( ) inherit W { KNd_dU ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 511))

	def test_512(self):
		input = """aDb , SoN  : array [ 0 ] of integer    ;   C : function auto  ( jxX3 : void   , G : void   , J8 : array [ 98397_73_4_98 ] of float      ) inherit k { w  : array [ 10_4_93_7 , 35_3988 ] of float    = - U    < q   + j7       ;  pjQS  : auto  = VGsQl   + h    == 2     :: tYWn   % p7W       ;  LT  : array [ 0 ] of integer    = K   % xvi    <= ! y     :: m   && Y       ;  }    t , Bv9 , m3 , B , o  : void  = B   + DQ    % ! fij9     - ! ! Z      == ! ! B   && W       :: gLqi ( )      , ! false     != - - ""        , - q0    * ! dty     && - - Z       :: eZ   - F    || m   && YV     || - en   || Kv0        , "໅໇ក᱊᳐𑋰\\"\\r"    < ! ! fF    / p   % cS       :: t   + PN    && ! aRzuE     - - L   * y315        , T   && nc    / - N     || g ( )      :: true    / ! - z      == 0       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 512))

	def test_513(self):
		input = """dtCo : function void  ( inherit out u : auto    ) { { p , n , K , NXB , f  : array [ 0 , 5_7 ] of integer    ;  n , c  : auto  ;  { }   }   cH ( )  ;   nFe  : void  ;  if ( - U     :: m   * T      ) break ;     }    n6 , a , p , aPt , r  : array [ 292 , 0 , 0 , 30264238_5_9_1 ] of string    ;   BF : function auto  ( ) { while ( PA   || i    <= R     ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 513))

	def test_514(self):
		input = """c9p : function auto  ( inherit HJW : string     ) inherit Z { }    S : function float   ( ) inherit r { }    LB4 : function array [ 66_65 ] of float    ( inherit out H : string     ) { AB , j  : integer   = TPd ( )    <= ! v     :: Sv   && J      , V   / cjy    < - xP     :: _   && gZxMs       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 514))

	def test_515(self):
		input = """Ucv5 , i , LL  : array [ 6_0 , 0 ] of string    ;   cHw , tUWUb5M  : array [ 0 , 7 ] of integer    ;   z  : float   ;   h  : array [ 0 , 934541_153 ] of float    = v      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 515))

	def test_516(self):
		input = """W2 , fLtw  : float   = ! U   * Bf6b   % x        , { }     <= ! y   && h     && - wXp    && YeTxi   / g         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 516))

	def test_517(self):
		input = """Cs8PgW : function auto  ( ) { continue ;   }    rtrVihZuqcl : function string   ( ) { do { }  while ( ! O    != - tt      ) ;   }    Y  : boolean   ;   vU : function string   ( inherit out F : array [ 315 , 57 , 0 , 0 , 16 ] of integer      ) { }    p : function array [ 4 ] of string    ( ) { }    h : function array [ 42_008 , 0 ] of string    ( inherit Bi : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 517))

	def test_518(self):
		input = """u : function boolean   ( inherit vz : auto   , inherit out K : auto    ) { }    KN  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 518))

	def test_519(self):
		input = """gd : function auto  ( ) inherit Jrcl { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 519))

	def test_520(self):
		input = """P : function void  ( Mz : array [ 0 ] of boolean      ) inherit m4 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 520))

	def test_521(self):
		input = """L , b  : array [ 0 ] of boolean    = 6.8E-69    == - ! CPnp    || f   * n        , h      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 521))

	def test_522(self):
		input = """c , i , k  : void  ;   V02K , k , cCP , jPI  : void  ;   NM : function boolean   ( ) { do { }  while ( 3      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 522))

	def test_523(self):
		input = """A : function array [ 0 ] of integer    ( out pRX : auto   , i : void    ) inherit f { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 523))

	def test_524(self):
		input = """NN : function float   ( inherit o : auto   , inherit out X : array [ 1 ] of float      ) inherit V_ { for ( PzlKA  = - hA     :: - _Js      , ij   + F    != V   % A     :: Z   / n    >= - C      , ""    == hzr   % u     :: - f1    >= 5      ) zxC ( )  ;     Cl  : auto  = ! v    < O   || YXxzgf       ;  }    g : function void  ( inherit out EN : void   , v : array [ 0 , 0 , 0 ] of integer      ) { CD , cvM8  : auto  = Y   - W    <= kHX_   * MDW      , iM   * H4ab3uE    >= uiB54yv   - T       ;  }    u , T , xyD  : void  = uf   % K    + A   && B     && - T    * ! c        , I ( )    == - y   + r     / ! Y ( )       :: U8w   && L    || vV7   % C     && HNW2S      , - - ! O         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 524))

	def test_525(self):
		input = """R : function array [ 64_1 ] of boolean    ( inherit iD : float    , inherit s : array [ 4 ] of integer     , inherit M : auto    ) inherit Cj { }    v , T  : auto  ;   OXe , l_ , tpd , Tyz2y9 , hh  : void  = p   < u    :: o   || b0BEqb9    % H ( )     * v   || e    + L   && E        , - - b    / L   % Ul       :: j   < - qUKV    - - k     / ! - H5        , "\\b"    >= ! tV ( )      :: ! ""     % T67 ( )    && ! K        , ! ! u1 ( )      != ! C    / ! AZ     / P   && M      :: V ( )      , p ( )    - Bnw    * ! - M       :: - ! c    && A   / LDuME      <= cgl      ;   J : function void  ( K : auto   , inherit out X : string    , c : void   , inherit out W : auto    ) inherit YF { }    QYeaUvB : function array [ 4_7 ] of integer    ( ) inherit D { }    X  : array [ 3 ] of integer    = ! n   || g     && 0     < MH    :: jMTf   || u    && - NTp     * - M   && Ty6_      < kL6   - - Dwx     && 3    % c   * J         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 525))

	def test_526(self):
		input = """z , Aj , _wo , Fg3  : auto  = - ! ""      == - dx     :: d   > V   - i    / K   && czu     % u   - r    || o   || J        , R4Oq ( )    / Nu ( )    && U     == - z   / Y    - - b1       :: ow ( )    <= - IeVRZ   * _q    / - qsf        , Hb ( )    + ! Iw     + - - Ct      >= ! ! M    % f ( )       :: ""      , vHf    :: j   || Su0    * i   * b     - - k   % Y      >= - F   || l     || - m    - ! y         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 526))

	def test_527(self):
		input = """H : function void  ( inherit out H : auto    ) inherit zU { XT , Zd , xir  : array [ 0 , 0 ] of integer    = hto   || Vsc    <= A   + s      , R   * tF      , Xwn   || DIkr9    <= Uqrk5   || l       ;  }    z9 : function array [ 0 ] of boolean    ( inherit out W : array [ 246 ] of boolean     , nx : array [ 0 , 0 ] of integer     , out rf : integer    , inherit out z : array [ 21 ] of integer      ) inherit Z { a3 , muyN , t  : void  ;  }    Ya0  : integer   ;   U  : boolean   = ! s   + Hsf     || q   - Il    % Lh ( )       :: L   || z26PkXN    || mP ( )     - G   || CA    / z     != true    % a       ;   X  : void  = ! w   - f    * ! GYS       :: - o   - h     || Ge ( )     < - lXLXJt   - K    % Gopp1   % PS4W         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 527))

	def test_528(self):
		input = """Hvi5 : function auto  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 528))

	def test_529(self):
		input = """im : function void  ( inherit out F4 : auto    ) inherit IK { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 529))

	def test_530(self):
		input = """tkF , b  : auto  = GE   / e   || B     * - _GE ( )      < ! J   + s    || Z73   / vf        , - YkAeNd   % U0     && cp   && hO    || f   && FAa      >= O ( )     :: - j    / W    * - ! V      < - 5_4        ;   z7b  : array [ 80 , 0 ] of boolean    ;   Y6Y3 : function array [ 0 , 622 , 0 ] of string    ( ) { M  : void  = oP   % v       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 530))

	def test_531(self):
		input = """_  : auto  = bh   || K90   - NZ    + 0      != ! Fg    / - y    + XO   && jkPT       :: homA   + u    - A8Qk   - D     || K8 ( )     < - ! f   - pD         ;   B8 , SK  : void  ;   lr : function array [ 91_9_00_3_97_85 ] of string    ( ) { }    MEHF : function string   ( inherit X : auto   , out fB : void    ) inherit U { kC7sH  : array [ 76 , 0 ] of float    ;  return ;   }    Y , E , u  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 531))

	def test_532(self):
		input = """yr : function boolean   ( inherit T : array [ 0 ] of float      ) { for ( YjAS  = l   + h9P      , B   * y      , p   / i      ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 532))

	def test_533(self):
		input = """yhh , g  : auto  = fY ( )    % YqTz   - j     && ! ""        , ! Y   && oqD     || ""    * z   - I6h0      <= - - N    && F   && R       :: ! ! K     != - I    - MvIr   - Qs     + ! D   && Pn         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 533))

	def test_534(self):
		input = """W  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 534))

	def test_535(self):
		input = """z9YJXn , E  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 535))

	def test_536(self):
		input = """R  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 536))

	def test_537(self):
		input = """ZJK0v  : auto  = false    && I   * ""       :: r   * d    + - QL     - ! K   + Y      != P   * _    * - ZfD     / e   - Dnni    / - iR         ;   DfR : function float   ( inherit out _ : boolean    , X6 : array [ 0 , 89_46 , 0 , 6 ] of integer      ) { return MA   || z      ;   continue ;   }    OmeX : function void  ( ) { while ( _   && O     :: i6M   / H      ) return ;     VH ( )  ;   Tz  : float   ;  x ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 537))

	def test_538(self):
		input = """o : function void  ( ) { }    kk0  : array [ 5 , 8_7 , 3_175 ] of string    = ! Bi   / dy     && - - yS       :: ""    % z   / NH     * _vGE   + dy    + - S         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 538))

	def test_539(self):
		input = """a , wW7 , N_o  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 539))

	def test_540(self):
		input = """xy : function array [ 9_987 ] of string    ( out bO : float    , Z : array [ 0 ] of float     , m : array [ 2 ] of float      ) { _ , NfU , v99 , YEG  : integer   ;  B  : float   = _mk   || r     :: ""    == X_   || aHKO6d       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 540))

	def test_541(self):
		input = """okx : function array [ 1_1 ] of boolean    ( inherit fw : auto   , inherit u : array [ 7 , 1 , 0 , 4 , 0 ] of float     , out m : void    ) inherit l { L , p  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 541))

	def test_542(self):
		input = """m , S  : void  = - ""    - P ( )       :: - o_    + bPM   - EQ139     / - ! RD      < - h   - rB     && - - gCxd        , bB      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 542))

	def test_543(self):
		input = """SHg : function array [ 56409 ] of boolean    ( W : void   , K : float     ) inherit sYD { YH ( )  ;   S  : void  = - k       ;  BIGEqONh  : array [ 0 , 0 , 0 , 54848 , 2_5_1_859 , 4 , 5 , 8 , 0 ] of string    ;  }    HUQ , h , i  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 543))

	def test_544(self):
		input = """QJmkd : function string   ( AzbwcYADK : auto    ) { break ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 544))

	def test_545(self):
		input = """sFWO : function array [ 0 ] of boolean    ( ) { Af  : auto  = ! nj7     :: gu ( )    > - tR       ;  }    b : function void  ( X0I : auto    ) inherit Njqz { g  : auto  = 2    > r   && abO       ;  return ;   t , L , Ch  : auto  = E   / Zk     :: A   * e    <= T   * c5XU      , kc   + Q    <= S9   && Vet     :: ! E      , ! r       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 545))

	def test_546(self):
		input = """i , A  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 546))

	def test_547(self):
		input = """RW , fi3Z4 , K , Cy , cRt  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 547))

	def test_548(self):
		input = """gV , ONP , V , qfc  : array [ 3 , 6_3_246_8_0 ] of float    ;   uC55E : function auto  ( inherit out S6ym : auto   , out v : float     ) inherit T { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 548))

	def test_549(self):
		input = """uA : function auto  ( ) { }    S : function auto  ( ) { { break ;   }   qg  = - Z    <= RICvV ( )      ;   break ;   if ( SA6   || r    == - F     :: yN     ) h1 ( )  ;     u  : auto  ;  while ( aD ( )    != ! f     :: SB   && UlA    >= r ( )      ) Mc ( )  ;     }    t : function array [ 0 ] of string    ( ) inherit V6u { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 549))

	def test_550(self):
		input = """g  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 550))

	def test_551(self):
		input = """t  : void  = Y   == ! N    - u   && jD     + ! ! aR         ;   _fy8k  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 551))

	def test_552(self):
		input = """y , Qls , O  : array [ 0 , 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 552))

	def test_553(self):
		input = """j , m , D5A , iJi , _wo  : array [ 6 , 0 , 3_0 ] of integer    ;   JyM0Y , l  : auto  = - ! Us    % ! CsoI       :: ! - f    + _   - k      <= false      , ! ! pe     * yy2   && Y   + P         ;   i  : auto  ;   C : function array [ 0 ] of string    ( ) inherit SERG { }    C : function void  ( LjVovN : array [ 0 , 0 , 0 , 74 , 0 , 4_0 ] of boolean      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 553))

	def test_554(self):
		input = """R : function void  ( inherit nI : array [ 45674686_675_7_850_5 ] of float      ) { }    U : function auto  ( out w0M5 : void    ) { }    e : function float   ( ) { }    zgO : function array [ 0 , 0 , 6 ] of integer    ( inherit out i : auto   , ckj9 : void    ) { }    w , JM , ZjGw  : array [ 7313_2 , 0 ] of integer    ;   k289 , s8  : integer   = false    > ! h   % vJloJH    + ""        , ! l ( )    + - X      >= ! N    * F ( )     % U   - J    - - hqHV       :: rA3z   > P   || S    * - X7uc     * A ( )    || Nz6        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 554))

	def test_555(self):
		input = """u : function auto  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 555))

	def test_556(self):
		input = """AN : function void  ( ) { }    h : function auto  ( inherit out f : auto   , inherit S : float     ) inherit N { }    e96 : function array [ 0 ] of string    ( out K : void    ) inherit C { while ( H   / WCi    > j   * l      ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 556))

	def test_557(self):
		input = """lYm8 : function void  ( out Q5o : integer    , inherit out kL : float    , inherit out B : auto   , inherit Nu : void    ) { break ;   }    g1 , F  : float   ;   c1Mm , t  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 557))

	def test_558(self):
		input = """ks  : void  ;   c : function array [ 130_2 , 0 , 8_2_81 , 11_3_4_1_35228 , 99414 ] of integer    ( ) inherit W { rMak83  = DX   && V1    > Ox   && A     :: M   && ZCR      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 558))

	def test_559(self):
		input = """HF , a  : array [ 0 ] of float    = true    == .31E+3      , - A   * z     - q    >= ! B1   % OH6    && - u2       :: 5.1E761224    < false       ;   G : function auto  ( ) { Uk6  = xI   || wxK    > ! f      ;   h , zxa2  : array [ 0 , 3 , 486936 ] of float    = ! a     :: P   && h6    > F     , B   && w9_4     :: f5   / sbBkx       ;  for ( Z  = ! YD     :: hlx1   && kU      , nT   / Mpl    < Wh   + oh      , Gn7   + wxFPSD    < ujj     ) { }     }    P  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 559))

	def test_560(self):
		input = """w  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 560))

	def test_561(self):
		input = """U : function array [ 9 , 0 ] of boolean    ( inherit out Z : boolean     ) inherit N { }    EP : function float   ( s : void    ) { YI4  : auto  ;  break ;   }    CG : function array [ 8_65_07 , 0 , 6_1 ] of float    ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 561))

	def test_562(self):
		input = """h : function boolean   ( ) { }    o : function auto  ( ) { }    wZW , K  : auto  = r ( )    - ! q   || Xt       :: "\\f\\t\\\\"    < - ! J     % ! N0A   % Fr8        , - p ( )    + _t5   || D      > false     :: - n7h    > guSqR7   || X    || ! S7     && 0        ;   n : function array [ 19_4_19 , 0 , 0 ] of integer    ( D : auto   , u : string     ) inherit bfW { for ( Utv  = - T    <= Un5   - gE     :: j3 ( )      , F     , u   && i    != NU   - e     :: ! _    >= ! ck      ) continue ;     { { break ;   K , q  : string   ;  H  : boolean   ;  }   }   while ( aRF   || h    <= tgs   || J      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 562))

	def test_563(self):
		input = """GhXpCrMgVjpV , N , JxOvSTWM , Rl , doz , i  : void  = - - j    / f   * M      > Uy   - Ydf   / gA     / ! C      :: Z   * dX    && H   - t     * wn   * Abj    + - t        , ! bI   / tT     - - D    * ""       :: ! w   || O     + Me   % S    - fo       , ! ! av    - V   - zr      == 6    - ! - c       :: ! - k   % BghCTq      <= - CfY   / j    - kA   / HQbel        , ! ! JS    * - JPG      <= B0   + KH6nBPAYsXZ    && Q   - FF     / d   || eNpL    * - F       :: - - o     && ! aq    + 0      == h ( )      , "\\f\\n"    <= - b   && r7      :: L7   * HI   - fOF7xaqjE     || - ""      < ! { }        , - ! l     + ap ( )    * ax   + E5sj         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 563))

	def test_564(self):
		input = """G  : auto  = - ! t     - Sk ( )    % ! fsMba       :: - - W     / - zd   % vk      >= ! - C3vyh    || A   % Xj6         ;   g : function void  ( out i : array [ 0 , 0 , 0 , 15 ] of float     , out N : auto    ) { sN  = l   - Nm    > ! c0K      ;   return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 564))

	def test_565(self):
		input = """UekY : function void  ( ) inherit V { { Cx , PQ  : void  ;  break ;   break ;   }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 565))

	def test_566(self):
		input = """NO : function array [ 96_7_2540 ] of boolean    ( wh : string     ) inherit L { }    pH , vK  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 566))

	def test_567(self):
		input = """uj : function void  ( out a : void   , inherit out L : array [ 3964 ] of integer      ) { for ( P  = ! v      , mMb   % C     :: 6      , - p    < ""     :: i   > r ( )      ) return ;     }    nx , s , E , y  : array [ 9_5 , 0 , 9257573 ] of string    = ! F   || x     / u   - z4    / t   && N       :: ! s   * CVn     / ! B    * - gp        , U   || Wx    + G    % - - Qk       :: s   / Lf    / - Cg     - ! eG    - o   - SIKNrn      >= ! u    - g   || _     + B ( )       , true    + - - BY      <= - n    || - Z     || qD   + kgZ    + - o        , - ! v     - fyz       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 567))

	def test_568(self):
		input = """O , s  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 568))

	def test_569(self):
		input = """d3 : function void  ( out Q : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 569))

	def test_570(self):
		input = """j : function void  ( ) inherit c { nS  : string   = ! W     :: - X    == ! MuQ       ;  }    i  : integer   ;   WD : function void  ( w : void    ) { wo  : array [ 86 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 570))

	def test_571(self):
		input = """u  : array [ 8 ] of boolean    = ! g    / ! rFMt     || u0   + zIOz    || z_   % Oy      != ! - t    && C   / D         ;   wL , AXbmf , ZP , I , C  : auto  = ! - n    % WlMs      :: DJ ( )    % 0     < DcuA   % ! - xC        , q   * F    + bS   - hPi     - Kw ( )    % J9   + pba      == - - EI     || S4Z ( )    + 0        , - - tL     - ! L     <= U   + ! H4V    && - ki        , ! i4t   || jL    && lC   % KJj      >= ! PRq   && U    * - p        , - - B    || - Pjpb       :: - YF    && ZG   % u     / p   && z    / F   || r         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 571))

	def test_572(self):
		input = """f , dF  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 572))

	def test_573(self):
		input = """B : function auto  ( out d : void   , Q : void   , out Vc : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 573))

	def test_574(self):
		input = """uq : function void  ( inherit out gR : array [ 0 ] of float     , inherit out Dp : auto    ) inherit J { break ;   }    Q : function array [ 7 , 0 ] of boolean    ( inherit out RWl : void    ) inherit a { O , QX , n  : integer   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 574))

	def test_575(self):
		input = """E : function integer   ( ) { do { }  while ( F   + C    == N   * K      ) ;   V  : auto  ;  for ( s  = Ew   - LP7pl    <= OB   + PR4      , C     , ! r      ) h ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 575))

	def test_576(self):
		input = """bmeuxN  : auto  = - ! _m_     || Uwt   && T   % M      < wlj   && Rc1    - ! jnTo9     && _L   + fS    || QYFPV   && Cq         ;   Y  : auto  ;   Q  : array [ 27_1 ] of boolean    = 0.3167    == ! Al5    / - F     * - P    && - b         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 576))

	def test_577(self):
		input = """tZ : function array [ 0 ] of integer    ( ) inherit x { A  : auto  ;  j  : float   = MD   * C       ;  }    L  : auto  = - Vrzi   && I     + NI ( )    - - V      != ! ki    + VAa   || FGB2     || T   && A    - vip   && J3a_         ;   fba  : array [ 0 , 4_365606_030 , 0 , 0 ] of string    = - - S   * RSj      <= - DRv     :: - A05eQ    * F   % q6    + B   / s2      < - l7Zy7p   * s    + mo   && kQI         ;   H  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 577))

	def test_578(self):
		input = """XYi , I9 , Y , DL , Q , M  : void  = ! Mvh ( )     > ! ! Co    + w   + N        , - rGn    % D   % F     - ARTEb7   || Ne    || - u      >= - false       , - false     <= jS     , ! ! X    % J   + f      < ! DY    * h    % ! ! H       :: - x9Hf   + W9     && ! HZl ( )      == B ( )      , ! ! LN     <= - - F   - Wpo        , u   - S    - fuK   / NF     && ! ! t      != ! ! ! B       :: o   != ! - ae     * - op   || zn         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 578))

	def test_579(self):
		input = """xo9 : function auto  ( out L : float    , inherit H : auto   , out dUh2Xi : array [ 708818 , 0 ] of string      ) inherit moH6wj7aLx { c  : boolean   ;  Hl  : float   = - P       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 579))

	def test_580(self):
		input = """tJSl , whd , k  : void  ;   vr  : array [ 899 , 6 ] of float    ;   m , Y , h  : string   = ! L   || tUBAwxaV    % SPAmXxyAV7   + XN2      == - in    + Jd   - l     % - ie    * - kjx       :: - ""    && fs_   / b        , - ""     || - kpUikU   + FECw        , m ( )    && - wJqg4     && G   || _5    && 0      < 26       ;   Wu , AkG , n  : array [ 0 , 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 580))

	def test_581(self):
		input = """xMO1 , FpP  : auto  = bgkI   + y   + U     && C   || G    - 0      <= ! ! jaG      :: - - K   && t      != 45_7_01_32_810      , Mjf   / dp    % L   || B     - GR ( )    + ! C      > - nm   + zPt    % Q ( )       :: nW ( )    && - o   || _      != ""    + yEq76A   / TwQsC     && ! D    / D2S   + sp         ;   f7zU8 , W  : auto  = l    :: ""    / Yx   && q9A     * ! w    && ! cW      > k   - X    + TA   - C     + ! rsUe   + YxG        , - ! - q         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 581))

	def test_582(self):
		input = """K2pKo , q , FQ , nr  : void  = ! b   % k    / - I_      <= ! eP   / T    % G_   % VFB       :: - MH ( )     < ! ! I   / m        , ! m    || - Kr   / v      == - MM   || gL     - ! Vz   && c7       :: fcTiPp   % f    && n   && SA     * EE   - - rQTsH      > ! - UFq8X    * P   && jQ        , ! F   + V     / aHn ( )    || E   * K      != ! ! u     - P   + jP9    + Q   && i3       :: - ! n   - f7      >= ! _z   && eacn     || y   && e    + O   + wKw        , false     :: e   / b    % ""     % ! - s         ;   vZ , z3u53  : array [ 0 , 5_73 , 3_7057 , 75_20 , 0 , 6 , 8 , 0 ] of float    ;   lvY7 : function auto  ( inherit m : integer     ) inherit h { }    L , J , _wfW  : void  = ! R26u    && 2     + - czh    || yxr5mq   * W      != yP     , ! - 0      >= G4 ( )     :: ! E    * RsH   / a     + NQ ( )       , - - WR    - - W      != ! 0     + - k   || JT       :: 6_0    && ! m    % T   || e      == - - X   % Op         ;   LAp : function void  ( out X : auto   , yFXmy : void    ) inherit cU { for ( po  = h   + Ei    >= 0     :: ! V    <= ! Rt      , ! m2    >= - Rdx      , r   % h    >= ! x      ) return ;     M , B  : void  = ! F    < - zz     :: qi   * Wp5      , z5   || M    == - w     :: ! pR    > m      ;  continue ;   }    dXP : function array [ 3607 ] of float    ( F : void    ) inherit t { return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 582))

	def test_583(self):
		input = """L : function array [ 0 ] of float    ( ) { if ( o   / A    != - Ng      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 583))

	def test_584(self):
		input = """H5 , l , Q , SI , GE9PG  : array [ 0 , 0 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 584))

	def test_585(self):
		input = """_v4H1On  : auto  = - - H     || V   + kB    % ap ( )      > - NSiY   / rB     + B   - e    * - n         ;   J_H : function void  ( irsM : array [ 9_61322 ] of boolean      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 585))

	def test_586(self):
		input = """D1 : function auto  ( ) { gBfz , e , w , F4R  : void  ;  for ( H  = 8      , ea   - Mq    >= - EWSlgq     :: - w    == Y   + j      , Mc   + yzrbt4N     :: - Z    > ! bnGW8      ) { nE  : string   ;  }     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 586))

	def test_587(self):
		input = """H5 : function void  ( I : void   , out H : float    , out qE : auto   , inherit c : string     ) inherit l { W  : array [ 0 ] of integer    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 587))

	def test_588(self):
		input = """g : function auto  ( ) { uYgs  : boolean   = - E4lv8    < ! z     :: F      ;  }    Vo  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 588))

	def test_589(self):
		input = """a : function array [ 12_151 ] of boolean    ( out d : boolean     ) { sT , Ss  : auto  ;  }    a : function void  ( ) inherit ql { { continue ;   }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 589))

	def test_590(self):
		input = """sAc  : void  = X ( )    % dX   || g   || c8      < s   % n    * - M7u     - - q   - Oh         ;   QjpHZj : function array [ 48 , 0 , 0 ] of boolean    ( ) { va  : array [ 0 ] of integer    = e   - HLAD    > rz   + r     :: jzFx   * Dn       ;  B  : string   = - f04Sf3     :: R   || bk    == M_   % wC       ;  D1BM , eDE , Q  : array [ 55396 , 5_4 ] of integer    ;  }    N : function auto  ( ) { }    kdK  : float   ;   vx : function string   ( inherit out Z1j : auto    ) { G  : array [ 0 , 73 ] of integer    = - f     :: - m    != Rz   || uF       ;  }    _  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 590))

	def test_591(self):
		input = """n0Fe : function auto  ( out LM : boolean     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 591))

	def test_592(self):
		input = """z , Y , kr , v , Ae  : array [ 0 ] of integer    = - ! eK ( )       :: "᝔"    < I   && g    && ! P     % R   % E    * N   * Q        , ! N    * h6Q   - Xb4q     * ! Z ( )       :: - ! 0        , UHX   != ! ! U ( )        , xq   && E9WI    || o ( )     * y    >= XA94s   * DX    && - dA     || N      , - V   && h     || ! b    - ! H2fH4i3         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 592))

	def test_593(self):
		input = """j , ga , x  : array [ 1_37960_013378_38 ] of integer    ;   r : function void  ( ) inherit IoL { if ( v   * v    > E ( )     :: A3E3 ( )      ) { mul  : integer   ;  nT  : auto  ;  { }   A ( )  ;   return ;   }   else break ;     t , W19K  : array [ 0 , 0 ] of boolean    = - vI    <= ! hd     :: yr   % uyt    < ! qRO      , J9o   && OW    != EO      ;  pQ  : array [ 0 ] of string    = z   / f    > ! I     :: ! rL       ;  }    Z : function void  ( ) { Jq , h  : array [ 9 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 593))

	def test_594(self):
		input = """GA : function auto  ( inherit out g : string     ) inherit g { v , e , z3  : array [ 8 ] of boolean    ;  }    g : function void  ( inherit _ : float     ) inherit a { }    U : function array [ 2499_733 , 0 ] of string    ( out r : array [ 4_6 , 86 , 0 ] of integer     , out j : auto    ) inherit SC { }    NS : function void  ( inherit out KEuL8 : integer     ) { FrWUJ  : integer   = Na   % I    < - S     :: - M    <= x   || qW       ;  hs , A , Dy  : void  ;  M  : void  ;  F  : auto  = ! Ch    < h   && Nh       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 594))

	def test_595(self):
		input = """v : function void  ( inherit out B : string     ) inherit hP { }    e : function auto  ( ) { }    c , I  : auto  ;   wm : function float   ( m : auto    ) inherit R { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 595))

	def test_596(self):
		input = """EZZ : function array [ 0 , 0 ] of integer    ( ) inherit H { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 596))

	def test_597(self):
		input = """KW , vWy  : void  = R   && W    - TCUDxnunN   || xL     / b   || qxCq8P    % RCKv   * f       :: ! w   + rb    || - U      != - - b    / H       , - ! E     || I7   % D    - 0      >= a   || _    || ! eA     || - wJ    || ! m4c       :: - HQRznj3    * D   - H     - - - V      < - NK   && j     + uM       ;   v4 : function void  ( out DBn : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 597))

	def test_598(self):
		input = """ef : function auto  ( ) { e  : array [ 26_6 ] of float    ;  }    a4 , yB , K , l  : string   ;   j : function void  ( ) inherit Mt { l  : boolean   ;  V , RnT_  : array [ 4 ] of float    ;  }    gd : function void  ( MhIK : array [ 59_4 , 0 ] of integer     , inherit QFbK : boolean    , inherit out g : float    , inherit out vlRX : void    ) { break ;   for ( vVv  = EJou   * S     :: - t    != q   * bC      , H ( )     :: T   * H    >= v ( )      , ""      ) { r ( )  ;   }     }    KV : function float   ( ) inherit j { }    r , z  : float   ;   O , P , i  : auto  ;   q  : auto  = ! v   * fr    + z   && P      <= ! hU1Dc    || u   / YTA     || ! ! y       :: ! - ""         ;   x , y , M  : auto  ;   y : function string   ( YI8AY846h : string    , LJ : void    ) { }    poql7R , R  : void  = l   / sHf    + ww   && z     / - Z    || JP   - t9        , ""    < - G    % m7K   - w     * vx ( )    || - _nt         ;   u  : array [ 9_81507 , 0 ] of integer    ;   sT  : void  ;   N : function array [ 0 , 40394 ] of float    ( ) inherit xc6 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 598))

	def test_599(self):
		input = """R : function integer   ( inherit out N : void   , f : float    , out H : void    ) inherit k { tTvi4  = Z   + Zr    != - J4      ;   continue ;   tpIe5vtrm ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 599))

	def test_600(self):
		input = """M : function auto  ( inherit nly : boolean     ) { do { Eg9x1 , gE  : auto  ;  }  while ( Y   + SPm     :: fcg   + tqxN      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 600))

	def test_601(self):
		input = """u : function string   ( ) { }    Nz  : auto  = ! j    + LI   / t0     % ! ""         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 601))

	def test_602(self):
		input = """RU  : array [ 0 , 0 , 0 , 1_28387_3_70044551 , 0 , 9_80_4 ] of string    ;   py : function auto  ( ) inherit uF { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 602))

	def test_603(self):
		input = """L , r3 , c , _t  : auto  = ! ""     && - zOaF   * Yr_Y       :: ! - bc     - - JwnXsqYw0 ( )      == 2_33964360      , - - l       , - S   / K     + G   + T    && l   % MvLW        , - V   + WX     + { }         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 603))

	def test_604(self):
		input = """y : function boolean   ( ) { TxU , Tf_ , H7 , a  : auto  ;  V , Ix , Y  : auto  = z   - yz7    > ! Y9m      , z6   || T     :: jowe   && auc    < cPj   || B      , ! Gtu    <= - E       ;  break ;   return XSnUU   - v    <= Z   && _t     :: O5   % JCT      ;   ID  : array [ 5 , 6 ] of boolean    ;  mW , d  : auto  ;  if ( qP3o   - VkV3    >= GL   / Hi     :: ! AMrF    != d   || U      ) { }   else return ;     i , S4 , n  : array [ 26 , 1 , 0 , 0 ] of string    ;  QWB ( )  ;   l4  : void  = aX   || G       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 604))

	def test_605(self):
		input = """Q : function array [ 48 ] of float    ( ) inherit _g6 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 605))

	def test_606(self):
		input = """gpJ : function array [ 0 , 5 ] of integer    ( ) { }    OFQ : function array [ 0 , 8 , 2 ] of float    ( V : auto   , inherit out bg : array [ 6398 ] of integer     , out a : float    , inherit _ : void   , out e : array [ 7 , 1763 ] of float     , inherit j : auto   , out V1Xz8 : auto   , gU : float     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 606))

	def test_607(self):
		input = """EH : function auto  ( R : integer    , inherit o : void    ) { GRdbLJFIp , QI  : void  = - apN     :: Tt   - R    > ! J      , ""     :: - WgsfmX       ;  DzN  : float   ;  }    d : function auto  ( ) inherit P { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 607))

	def test_608(self):
		input = """s : function void  ( inherit D4 : boolean     ) { mw , GwVou  : auto  ;  }    c_MkS , T  : array [ 0 , 6_0_2 ] of integer    = ! ! U    && B   + zANTn      < - g8A    && ! NEe     && - K    + eA   && Q        , ! K2L   % DHb     / ! u   && bNyk         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 608))

	def test_609(self):
		input = """OQoI : function boolean   ( inherit out z : float    , inherit out JjxV : string     ) { }    HaWr , x2  : string   = ! ! S    * ""      <= - Nb   % PR9     + JgS   - n    && Z ( )        , ! ! ! XYA29      == y ( )    || - suA2ICjZ    + BtC   % L       :: mu ( )    - r ( )        ;   d , R , k  : array [ 6 , 59434_6 ] of boolean    = - ! X     || ! 9       :: z   || ""    - MU     >= - u   / n     - U      , I   * Hj    && ! L     + ""    || - wUWqM       :: o   * e    / X3   && GPccQI     + - Y1fKb     > - - D     % - C    && uJ   && QK        , ! yG    && X5D ( )     && l   || _    || Fn4Q   - v      >= ! PpN4g   - g    * M   && i       :: - Y    && w   && T     - aGQ   - n    * RAjc   - CDnoP      == ! 4    * - a9hG         ;   QP : function void  ( inherit Khh : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 609))

	def test_610(self):
		input = """T , gA , s , P  : auto  ;   fToWI , aw  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 610))

	def test_611(self):
		input = """daH : function float   ( ) inherit H7 { Yq  : array [ 0 , 0 , 51 , 0 ] of string    ;  }    M  : array [ 0 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 611))

	def test_612(self):
		input = """i : function array [ 0 ] of string    ( J4 : auto    ) inherit APYBq { }    o  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 612))

	def test_613(self):
		input = """nN8Qul : function array [ 0 , 0 ] of float    ( ) inherit I8tE3lZT { k  = - e      ;   }    E : function boolean   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 613))

	def test_614(self):
		input = """u : function void  ( ) { s7x ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 614))

	def test_615(self):
		input = """pBAO1 : function auto  ( inherit out k : integer     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 615))

	def test_616(self):
		input = """v  : array [ 0 , 647115 , 0 , 559_501_7 , 0 , 1 ] of integer    = DWVbcS2 ( )    && B09   - b     + - es    - LX   || f      < ! HI   && _k    / IY        ;   R  : string   = - lr   % D     / - - Yb      >= - - Sy     - x   % y   || jv         ;   EqB : function void  ( VrVz : array [ 79491984_64_8_931 ] of string     , inherit out zzf : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 616))

	def test_617(self):
		input = """U : function array [ 0 ] of float    ( ) { }    j , LAiX  : auto  = nrBVU ( )    == - C   + c     - G     :: ! ! YHHS   / z      >= ! a   && - L        , ! ! - U         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 617))

	def test_618(self):
		input = """P : function boolean   ( inherit V : void   , inherit Qo : void    ) inherit UWi1 { v  : array [ 85_9693528769_63 , 38237_7 , 0 , 0 , 4 ] of boolean    ;  N  : auto  ;  break ;   continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 618))

	def test_619(self):
		input = """l  : array [ 0 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 619))

	def test_620(self):
		input = """j : function string   ( inherit u : auto   , jx : auto    ) inherit sI { return LdU     ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 620))

	def test_621(self):
		input = """_qP  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 621))

	def test_622(self):
		input = """x , r , T , AH5  : array [ 116_96 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 622))

	def test_623(self):
		input = """D : function auto  ( i : auto    ) inherit BDBW { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 623))

	def test_624(self):
		input = """D : function auto  ( out G : void   , inherit FT : auto   , inherit out aw : integer    , I : void   , out hcO : string     ) { return Ys   - o     :: G   * Qq      ;   continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 624))

	def test_625(self):
		input = """v : function void  ( inherit out t : void   , out m : auto   , out iB : array [ 0 , 0 ] of float      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 625))

	def test_626(self):
		input = """FsNv  : integer   ;   lehM1cX8_ , PU  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 626))

	def test_627(self):
		input = """P , f  : auto  ;   h : function boolean   ( inherit out lH81cf : void   , out z : array [ 0 ] of integer      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 627))

	def test_628(self):
		input = """y  : auto  = ! F   + b0     % YJ ( )    && a   - x       :: yw   && LxRO   / HEk     || Oow ( )        ;   U2  : boolean   = M   / T    + - w     * L7b   * GUcI    && a   || b      != sy   - G    + L   - vO     % ! ! e       :: ! O7ve   % uP     || ! - V7      != - 0    && - C         ;   p  : auto  ;   lr : function void  ( H : array [ 6_1 ] of string      ) inherit GmoI { oda  : array [ 0 , 0 , 0 , 4 ] of string    = Bl_   / Z    >= ! zt     :: ""    > ""       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 628))

	def test_629(self):
		input = """J : function string   ( ) inherit Gar { o3Uo  : auto  ;  xY  : boolean   ;  while ( - l2     :: ls   && v      ) S0 ( )  ;     }    Z : function auto  ( ) inherit uv0 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 629))

	def test_630(self):
		input = """Q , c2  : array [ 9 ] of integer    = ! Ff ( )    || _   && L       :: - ! _z   || n        , ! true        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 630))

	def test_631(self):
		input = """C , tq , Q , D  : void  ;   x  : void  = g   % sf99    - PV   % u_0XA     - ! ! K         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 631))

	def test_632(self):
		input = """GM  : array [ 853 , 0 , 8_2 , 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 632))

	def test_633(self):
		input = """y : function auto  ( out nu8 : auto    ) inherit rPQ { uC , K  : void  ;  vAT ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 633))

	def test_634(self):
		input = """dB : function auto  ( inherit out B0C : void    ) inherit xRO { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 634))

	def test_635(self):
		input = """X : function auto  ( ) { K , dSvF2TwW , opLf , U , oip , li , xWUvy74yG , Zi  : array [ 0 ] of boolean    ;  N , k , To6X , j  : array [ 9_0 ] of boolean    = Z   && j    == pg ( )     :: s   % Q      , - BcnEB6     :: F   - c    >= ! J      , r   <= P   && J     :: - yj      , ! w     :: o      ;  w , wUdQ , Pk  : string   ;  }    P , Upf , c , Qzfm , p  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 635))

	def test_636(self):
		input = """D8v  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 636))

	def test_637(self):
		input = """p , _  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 637))

	def test_638(self):
		input = """b : function array [ 621 , 0 ] of float    ( inherit out GZU : array [ 84 , 0 , 4_2 , 0 , 82 ] of integer      ) inherit _j { }    u : function auto  ( ) inherit JE { }    X , I , Ml , AG , d  : float   ;   Bs  : void  = e   + b    - ! F     - H   && S    && n   % Nv      == - VW6F     :: 1_6000    + DL       ;   Z : function integer   ( p : auto    ) inherit P { PP ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 638))

	def test_639(self):
		input = """Aj , Wo  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 639))

	def test_640(self):
		input = """zdofw7T : function auto  ( ) inherit X { { }   for ( H  = ! i    == - y     :: ""    <= ! _      , I15   % i    == R ( )     :: L   || qd1    <= nx   && d      , ! T      ) P ( )  ;     h , J , d  : array [ 0 , 5_5_0 , 0 , 7711 , 30 , 27 ] of integer    ;  continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 640))

	def test_641(self):
		input = """h : function string   ( ) inherit pu { v  : array [ 8_64_90_63 , 4_2713 , 41_19581 , 888 , 946_3_5 ] of float    = ! A    != - c       ;  }    RO : function boolean   ( ) { RThRb  = N   && EtH      ;   }    M7 : function void  ( inherit Kn : boolean     ) inherit rDt { }    v : function string   ( p : auto   , inherit SyT : array [ 8868 ] of boolean      ) { do { U , p , X  : boolean   ;  }  while ( _   && V      ) ;   }    J : function boolean   ( out x : array [ 5 ] of integer      ) { hO ( )  ;   do { }  while ( ""      ) ;   f , r  : auto  ;  Q , W , R , yTG , N , R , Tu  : void  ;  }    z : function void  ( inherit tq : integer     ) inherit l { Ma  : float   ;  }    DWuH  : auto  = - Pz   + Jo     && Yj   || koz    * FDW   + q      >= ! "𑦪\\\\"        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 641))

	def test_642(self):
		input = """goX  : integer   ;   M , E  : array [ 697164_23_952678 ] of float    = xl   + b    && ! R     - C   && jf    - - Uq       :: { }       , - sT   / B8y    + K4   - q         ;   bIvNas , e  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 642))

	def test_643(self):
		input = """g25Y3 : function auto  ( ) { KDUCs_  : auto  = ! Wce    > 9     :: T   / k       ;  }    C : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 643))

	def test_644(self):
		input = """k : function string   ( ) inherit d { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 644))

	def test_645(self):
		input = """H6 , K  : integer   = M ( )    % true     > ! - - KI       :: ! { }        , - ! J   || tkiE5hx      > o    :: B   || RT8    / Y   % N     && - O    % ! T      == ! - F     / - Bce    && T   + DaGM         ;   u  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 645))

	def test_646(self):
		input = """Pi : function array [ 0 ] of integer    ( inherit mq : float     ) inherit MAd { }    T : function auto  ( ) inherit c { if ( Z   - b    >= H    :: C   / _B      ) continue ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 646))

	def test_647(self):
		input = """O , y , q  : auto  = a   * M   && P     * m   && BX    * 0       :: ! - V    && Rg     < ! PoF    % - h     * ! jmN    && l   % V4        , true    && - Sms    % - h        , - IC   % xJH    - cl   || y         ;   G : function void  ( S7 : auto   , inherit O2 : void   , inherit x : auto    ) inherit u { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 647))

	def test_648(self):
		input = """aY : function auto  ( out ui : array [ 26_3_1050136 ] of float     , out RT : auto    ) inherit c { fbygY  : array [ 0 ] of boolean    = Os   && _    > R      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 648))

	def test_649(self):
		input = """vb , T  : auto  = - b_7   - ez    * - Tr7K        , - ""    / oGWME   + jZ      < LG   % N    || E7    * w   * H    / X ( )         ;   B : function void  ( ) inherit Xd { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 649))

	def test_650(self):
		input = """exNcU  : array [ 89_80714_4616998 , 0 , 0 , 0 ] of float    = - ! WG_a   - zVZ_         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 650))

	def test_651(self):
		input = """C , Snv  : void  = T   / K    * cM   + W     && ! - MB        , - ! eUK     % ! l   / vk      <= ! l8e    / lux   || G     % 98267_1        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 651))

	def test_652(self):
		input = """V  : array [ 4 , 0 ] of integer    ;   A  : string   = - ! p   && W      != i5Bp   + - ! b       :: pOJM ( )    && - 0      <= x   || D    || ! D     - snHG ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 652))

	def test_653(self):
		input = """F : function void  ( ) { continue ;   return ;   }    KaWOEz : function auto  ( inherit out e : boolean    , H : void    ) inherit gr { L  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 653))

	def test_654(self):
		input = """Q  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 654))

	def test_655(self):
		input = """k  : void  = - P98   || O     * T   * y    * B   + h       :: ! ! CsN   || BigRm      < _ ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 655))

	def test_656(self):
		input = """z : function array [ 0 ] of float    ( inherit out M : string    , out dL : string    , out q : void    ) { eGv , e9 , snK , l  : float   ;  }    z : function float   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 656))

	def test_657(self):
		input = """o : function array [ 0 ] of boolean    ( W : array [ 6 , 0 ] of integer      ) { }    e , z  : array [ 0 ] of string    = ! ! WI    || - eb      >= ! Ry   / H1    + ! Q       :: - eDw   * mN     || ! LaonTd    + - C_        , gVf   && E    % UNo   + WH     / XC   && H    || G   % FlO         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 657))

	def test_658(self):
		input = """au  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 658))

	def test_659(self):
		input = """hR : function array [ 8 , 0 , 0 ] of integer    ( ) { }    a : function boolean   ( inherit o : auto   , inherit F : void   , inherit out c : array [ 3 , 0 ] of float     , WV : string    , out Vl : array [ 0 , 88 , 0 ] of boolean     , Jc45R : auto   , inherit out x : array [ 0 ] of integer     , inherit r : array [ 0 , 0 ] of boolean      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 659))

	def test_660(self):
		input = """n : function array [ 663_0 ] of integer    ( ) inherit Ghr { }    O : function array [ 91_14_191 , 27821052 ] of boolean    ( inherit out D3v : array [ 0 ] of integer     , inherit out fAQ : void   , DK0R : void    ) inherit Ky { GC  : void  ;  xXJ , bEvz  : void  ;  zg  : void  ;  Z , X82Gtor  : array [ 353 ] of boolean    = hLd   + p    < - Dbl      , - JFY     :: YM   + qUh1R    == - w       ;  }    E , M , J , po , d  : void  = ! - - z      == - zeH    / - y     / ! OR9_H4    && V   || js4        , zRp7kR   + a    + F   + XXq     && - gaT   && B        , - Hnb   * - l       :: - ! gI     % A   && x    % T   && _      > - - ! v        , i ( )      , - - - G      >= ! ! I    || fPi   - u         ;   j , TM  : array [ 1 ] of integer    ;   z : function integer   ( out o : float    , out tS : auto    ) inherit Y { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 660))

	def test_661(self):
		input = """u : function auto  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 661))

	def test_662(self):
		input = """u0R  : integer   = ! YYaLFZm   + s    + e   * Ey      > ! kY   - Qr     / ! o    || Z   - w       :: ! S    % jGn ( )     && C ( )    + Fq ( )         ;   t  : void  = { }     != B   - p    + V   || q     % lm       ;   f4 : function auto  ( ) inherit t { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 662))

	def test_663(self):
		input = """a7S8 , P7LLoe , M7  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 663))

	def test_664(self):
		input = """p : function array [ 0 ] of float    ( ) inherit czh { }    N : function boolean   ( ) inherit ZU7TatF3 { i8 ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 664))

	def test_665(self):
		input = """Qu : function void  ( inherit wS : integer     ) { N  : float   ;  return m0_g   / C    <= D   % QNo     :: 5      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 665))

	def test_666(self):
		input = """U : function string   ( ) { }    X  : void  ;   opy99 : function void  ( ) { while ( c   % a1f    >= d   + O     :: _   % o5    == oL   - bH      ) continue ;     }    VO : function auto  ( inherit X : string     ) inherit DMK { wAk , P , Ey  : void  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 666))

	def test_667(self):
		input = """uK3 : function void  ( M : auto    ) inherit MZ { }    jr4 , m  : boolean   ;   FJY : function float   ( ) { }    j : function array [ 653 ] of string    ( out Lx_7 : void    ) inherit a { }    F : function auto  ( out tQLJ : array [ 0 ] of float     , out o : boolean     ) { continue ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 667))

	def test_668(self):
		input = """Wt_V : function auto  ( inherit out B : auto    ) inherit Xb { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 668))

	def test_669(self):
		input = """xsp , l , dWIDc , HZ  : void  = - oQ    < NnV   / k      , ! ! FI    - b5   * yRhH      <= - ! G   && Z       :: O   * S    * ! AF     % G   + w   && bV      > ! - wS5    / u   || b        , .e8      , 8_9_50    >= p ( )     :: - true        ;   q  : auto  = ! - - x       :: ! a5   % wRj     && a   && u    || ! F1W      < k ( )       ;   IcP , Hs , pda  : void  = - b   / ! m       :: "𐓼ᝲ"      , ! v    + xlm6   || oY8buC     || - d   * yiGTK      >= ! C   % pCc_V     + - UdNTT   && AE       :: - o   % b    - - B        , w   / _    || j9   * W     || 5    || Ec   || E       :: kmym      ;   Zehi2 : function auto  ( inherit Io : void    ) inherit i { return ;   { return ;   }   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 669))

	def test_670(self):
		input = """wz : function array [ 8378 ] of string    ( inherit nq : array [ 9_29251 ] of integer     , inherit out i : array [ 0 , 0 ] of float     , inherit out s : integer    , out n : void   , out M : array [ 63848 , 62 ] of string      ) inherit dBCK { return ;   O ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 670))

	def test_671(self):
		input = """P  : array [ 0 , 5335_3_8986_56 , 5 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 671))

	def test_672(self):
		input = """p : function array [ 0 ] of integer    ( ) inherit l { jQu5 ( )  ;   }    Cw , y , V9A , q  : array [ 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 672))

	def test_673(self):
		input = """b  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 673))

	def test_674(self):
		input = """wJf : function void  ( ) { }    m : function void  ( ) inherit l { Fja , a , rkJb , V , u , Dm , Z  : array [ 3_9 ] of boolean    = ! W85    >= - L1      , m   + OE     :: D     , ! t    < hr   - ck      , N     , RvVBjmeC   * Y    != V3   + M     :: m   / kj3q      , Uhi   && h    < O_ZMg   && rG     :: X7   && Kx    == 0      , U   && x    > ! t       ;  return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 674))

	def test_675(self):
		input = """T9E  : array [ 0 , 0 ] of float    = .e16       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 675))

	def test_676(self):
		input = """e : function float   ( g : auto   , qUM : auto    ) inherit d { break ;   }    Q : function boolean   ( ) { }    U  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 676))

	def test_677(self):
		input = """BPY , i , d0 , _  : integer   ;   V : function array [ 9864 , 0 ] of integer    ( ) inherit o { { Q , w_  : float   ;  y , J  : integer   ;  { break ;   }   continue ;   rP ( )  ;   }   }    uP , qJe1 , R  : auto  ;   LsNl : function array [ 829 , 0 , 0 , 0 ] of integer    ( out f : auto    ) inherit u { }    u : function array [ 0 ] of integer    ( VT5 : array [ 7_8_084 , 99_67_2 , 9_358_8_54 ] of float     , inherit out j : array [ 0 ] of boolean     , uJ : array [ 0 , 0 ] of string      ) inherit O { }    O : function auto  ( inherit ue : auto   , out fAuT : array [ 384_9 ] of integer     , inherit W : array [ 809_3_1 ] of float     , out K : array [ 509 , 0 ] of integer     , out K : void    ) inherit M5 { }    Mh , E  : auto  = S ( )     :: { }     - W   - J    - ! N      > - YT    + ! J3     * z   || C    && Y ( )        , FJ   - s    % ! xe     + ZLUweU   % f    + - vB         ;   WrH : function array [ 92 , 0 ] of integer    ( out dSflgy4 : integer    , inherit t : auto    ) inherit _r { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 677))

	def test_678(self):
		input = """e : function integer   ( ) { V7 , b4 , U3 , oh39 , h , Z6  : float   = t   && Jv      , rB   + m    == ! vW     :: 2    < z   * C      , G   - eF      , p0i   || Z9    != - J      , - e4d     :: ! _      , A ( )     :: - t    <= - J       ;  return ;   if ( B0   == - oT3TJ     :: - DIFGXxkQx    != - t      ) break ;   else { }     }    S  : boolean   ;   Q , aU3hzciBiyH , p , DbDo , Z  : void  = ! - Q   % E      <= O   || m    - - rnChG     / ! ! lN       :: n ( )      , - - ACaB6_     % Z    == - - C   - M4       :: L   / v    % - Scz     || ! D8 ( )        , paD   * G    % ! G     / tHFJaVy   - b   || d      >= ! ! N    || - Z        , u ( )    < Umn ( )    && f   - cfWki     * Wxg     :: asUig   + F8    && E   + eH_     * - - _        , G ( )     :: - ! c     / ""        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 678))

	def test_679(self):
		input = """w : function integer   ( inherit out U : array [ 4 ] of boolean      ) { E  : boolean   = Q   % c     :: J3E   + G    != ! m       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 679))

	def test_680(self):
		input = """Cp : function float   ( ) { continue ;   return ;   while ( p   + Rv    <= - tzm     :: aNY   - a_      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 680))

	def test_681(self):
		input = """J0  : float   ;   u36 : function string   ( inherit out KoY : auto    ) { jf ( )  ;   x  = X   - R      ;   }    R : function string   ( q : float    , out Da0 : string     ) { }    e : function array [ 4726 , 0 ] of float    ( ) inherit D0bU { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 681))

	def test_682(self):
		input = """j7  : array [ 0 , 0 , 0 , 0 ] of integer    ;   B , l  : void  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 682))

	def test_683(self):
		input = """B  : string   = ! FD    && Jz ( )     || ! wA4    && - Rj         ;   gw , G , VaO , z  : float   ;   N : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 683))

	def test_684(self):
		input = """d_ , va , O , w  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 684))

	def test_685(self):
		input = """Sl : function array [ 0 ] of float    ( Ld : array [ 7_68_5 , 0 ] of string     , V : string    , inherit JEi : array [ 7295 , 5_56 , 0 ] of integer      ) { }    Sh : function void  ( ) { cb  = - B      ;   break ;   }    JO : function auto  ( ) { VI , af , I  : boolean   = ! VWe    > 0      , - B    > - _     :: j   + du23f4    < ! Ug4      , v ( )    >= iy   || A       ;  do { }  while ( - ENp    == ! wL_q6     :: ! nycez    >= A   - B      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 685))

	def test_686(self):
		input = """b : function string   ( out LR7IjP : boolean    , g : void    ) { do { eF , h , R_ , v , IbH  : auto  ;  }  while ( oD   || y    > - w      ) ;   while ( ""    != ! Bm     :: ! J    <= I   && P      ) FeY ( )  ;     qO , x , r , d  : array [ 0 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 686))

	def test_687(self):
		input = """nYa : function float   ( out r8 : auto    ) inherit h { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 687))

	def test_688(self):
		input = """Q : function void  ( out bzm2 : boolean     ) inherit T9 { }    B  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 688))

	def test_689(self):
		input = """R , j8  : string   ;   f : function void  ( ) { }    t : function auto  ( ) { }    ZrG , mr , ND4Q  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 689))

	def test_690(self):
		input = """HF1 , Wqz , S , a , D  : string   = ! m    / ""     - ! _2b    + nrt2   % CE      <= ! OO ( )     || ! oS_u   && z3WUDUAB       :: ! - PGt    && - FSLKkgVBu        , ! - 2        , g    :: ! dB1   / Y2     && - T2   * z      != ! ! - xojx        , ! - - M0e      == - o ( )       , D      ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 690))

	def test_691(self):
		input = """C1Su  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 691))

	def test_692(self):
		input = """ga  : auto  ;   UI : function void  ( inherit out IK : auto   , inherit out T : auto   , c : array [ 7919 ] of boolean      ) inherit Yx { while ( uwW   * uIO    == hA   || kn     :: L1KbXG   || hv    == ""      ) break ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 692))

	def test_693(self):
		input = """Z : function boolean   ( v6 : void   , out S : void   , w : void   , WL : array [ 0 ] of boolean     , fk : auto    ) inherit g { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 693))

	def test_694(self):
		input = """_  : array [ 6_6818_5 , 66_96 , 2 ] of integer    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 694))

	def test_695(self):
		input = """n , D , N , pAYAQo , W  : boolean   = H     , QR_     , ! Yzm0    / - a3     + VNcYR9oFaN   || eS    + - k0      < v7   + o   * wY    * ""       :: - kF   % N     - ""    % - z9        , s   / VPikGN6w    % ! CL     && ts   % e    || PZ ( )      < 0E2     :: aqnPO   + dFH_    + p   + hS     && g   && qxt    / kS   && s        , eS   || hU    * RyDt   || M     - zq   + xf    + ! lNch      < ! r7   % M6    + OHCb6   || W         ;   P : function array [ 2 ] of integer    ( inherit out oARJ : void   , inherit out B : void   , Z : void    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 695))

	def test_696(self):
		input = """Q , l , Va , wc0_e  : void  = - - m4    + ! ru      == ! - V    - ! lo        , { }     != - ! p     - - q    - wK   || Zx        , ! ye   + V     && ! j6   / rH      >= J   / r    || O3r   || y2p     / _   / Eed    % ! KW       :: - ! lvdT7    % jJ   + b      < j7   - m    + ! n     || ! kFxT ( )        , - jg    && KF ( )     && - U    && - q       :: ! - zt   || cL         ;   u4 : function integer   ( inherit out l : void    ) { iLhqFp  : array [ 0 ] of float    = - v    < nS   || oV       ;  }    e : function boolean   ( inherit out e : void    ) { CP  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 696))

	def test_697(self):
		input = """c_EJ : function array [ 3 , 0 ] of integer    ( out I : array [ 0 ] of boolean      ) { SF  : string   ;  continue ;   _MU  = lJB   || oOd      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 697))

	def test_698(self):
		input = """Z : function array [ 1 ] of float    ( inherit out rv : auto   , o9g : float     ) inherit If { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 698))

	def test_699(self):
		input = """yg : function array [ 0 , 46_2_54_4 ] of string    ( out q : array [ 0 , 0 , 0 , 6 , 0 ] of string      ) inherit Qkb { b , c , Q  : auto  = y ( )    <= q_   / o      , ! z      , 0       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 699))

	def test_700(self):
		input = """W : function auto  ( ) inherit M { Tb , mk , Ln , d , fb  : array [ 15637_341_75_660_3_733 , 0 , 34 ] of integer    = 7    < UC4eW   % CG     :: h   - pNb      , N   + _y7SEX     :: - B      , Zts1   + h    <= r   || yKQaVTpTy     :: ! soAo    != ! w27      , i   <= - KrOZ      , ! W     :: - x    > 6       ;  }    DCxsxE : function void  ( out V : integer     ) inherit kg { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 700))

