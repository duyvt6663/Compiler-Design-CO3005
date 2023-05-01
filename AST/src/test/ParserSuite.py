import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = """yqk : function auto   ( ) { }    pH : function void  ( inherit out I5gQ : array [ 0 ] of string      ) inherit Q { return y   * jJ    < R   - y      ;   F  : array [ 20_7 ] of integer    ;  return - wtlKa      ;   }    m : function void  ( inherit out v : float     ) { B  : array [ 8 , 0 , 0 ] of boolean    ;  }    K , C72 , x , m  : auto  = ! ! CM    % ! U      >= - - KG1BAu   && uG       :: ! ! - H_e        , BQozP77     , VKtux   + _    * - Li     && D   + _r    * ""      < dU ( )    - ! Y    || m   - Qfl       :: b     , - ! a     && J   + h    && 0         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = """rEB , eh , EPi , E  : array [ 0 ] of boolean    ;   iG : function array [ 0 , 8605 ] of float     ( ) { do { continue ;   { }   }  while ( - s      ) ;   }    u : function void  ( inherit out dM : array [ 11292722_4_20 ] of integer     , FXPUlp : auto    ) { for ( I  = r   - t     :: vPq1   * X2      , ! P     :: ! q9J      , M   + g    > P5O   / z      ) continue ;     }    A : function boolean    ( ) inherit n { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = """LJR : function void  ( inherit _ : auto   , inherit L : array [ 251 , 0 , 7_2 ] of boolean     , out pFr : array [ 0 , 0 ] of float      ) { R , OGg_  : float   ;  x , zskl , Y , Qj  : auto  = - C     :: tR   && RXbEs      , rH   == ""     :: D   && f      , viH   + NK     :: iT   * xO      , - q2oJ       ;  e  : array [ 3_336 , 3366 , 0 ] of string    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = """ou  : auto  = ! N3       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = """SamXRra  : array [ 0 ] of boolean    = nO ( )    || ! X    * FF0   + fCC      != ! F    + Yu   - a     % ! yU4glPb      :: "\\b"    + F ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = """pxvj  : boolean   ;   pcud2 : function void  ( ) inherit k { h , N  : boolean   ;  U  : array [ 4_7_86641 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = """h : function auto   ( ) inherit I { O  : auto  = F6Nk   / H    >= u4   - mn       ;  u  : integer   ;  do { { vk  : auto  ;  }   }  while ( ITo   && vb    <= ! F      ) ;   continue ;   if ( - UfH    < z   && P     :: - v    == Ev   / ocVAv      ) break ;     }    VV , RJ , jA5 , p  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = """T3  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = """Ts  : boolean   ;   H : function void  ( inherit out v : auto    ) { }    O : function void  ( inherit D : auto    ) inherit VZ { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = """_ , pF , aNN  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = """o5riUzY  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = """o  : array [ 8_0 ] of float    ;   yKUCh : function array [ 80_77 , 0 , 2 , 0 ] of boolean     ( ) { }    bjkO , B , E  : array [ 0 ] of float    ;   Z , b  : auto  = ! - k52D   - WXA      != deO   - Z    && C   + WM     % 4    && w   + bfLSI6J        , kV9    :: b   + oJ    && F   - p     * K   - L    * ! e      == - { }         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = """k  : array [ 369_4369621_1_0_33_51002_16 ] of integer    = ! D    || - nl     / Zg   - R    + - kY       :: mA ( )    || U   - nV    / o2   % L         ;   F  : auto  = - ""     - ! - P         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = """J  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = """h , p , ab  : auto  = C   || - cRh   % O       :: ybwKI   * PCyC    % w49   * Kr     && "\\""       , i ( )    < 0      , - "\#\\\'"     < ! ""    / n   - uY0         ;   i6R , y , UH , r , o  : integer   = yM   && ki    + 2     + n   % C7    && w   || c      >= - W    % DY2   - SX     - U1      , W_dOo   / i    || ! _     || - wch    && cLizl_   && bx       :: ! ZL1   / Z     * - mQHmi       , - - ! Nv      <= - - oE    && 2       :: - b    + ""     + p5   * F_D    * n   - E        , C ( )    * - So   * EZb       :: h   - e    + jrr   / ur1     && ! j   / YYy        , - - ""      == - - PwAWS   % Tq       :: ! ! s     % ! - I         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = """s51NWTkG , _zn , N  : array [ 0 ] of float    ;   B  : array [ 8 , 0 ] of boolean    = ! W    * O72   || UC     + - R   + b1_         ;   n4 : function void  ( ) { }    D : function void  ( ) { }    Lv  : auto  = ! CM   + _     + ! ! U      < - a   || Q    / b3   * qaE         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = """zK : function integer    ( ) inherit e { XZ  = d   || rw      ;   k , o  : float   = ASZ56F   && X      , S   + a    > sy      ;  do { }  while ( Fw_oft ( )     :: V7z2   + j    >= Us   && rq      ) ;   gr , Ls , Np , nb  : array [ 0 ] of string    ;  }    iz : function void  ( ) { continue ;   while ( h   && y      ) { }     }    CD : function void  ( ) { return ;   Q ( )  ;   K  : auto  = V ( )       ;  RkX1cuf  : integer   ;  aWA  : array [ 0 ] of string    = _   - p79qi    > - D       ;  }    n : function void  ( inherit L : integer    , inherit r : auto   , r : auto    ) { }    sz  : auto  ;   Z  : auto  = ""    + ! E     != - ! C8   && OW         ;   o , oj  : boolean   = ! ! _    - S   && Go      == - 0    / ! Lqrbw       :: ! W   || t     || x      , OU    :: vO   + DS    % KbQjZJf   % m     * xo   + 4      >= ! K    % q   && zX     && tZ ( )        ;   w  : array [ 0 ] of boolean    = z ( )    || K2g   - S5    % e ( )       :: ! KBQh6   || g    || s   / Ab      >= vq   - Nh    || gs   - b     / uU   % q5sS    - ! JX         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = """dr : function auto   ( inherit RJxw : boolean    , out T : auto   , inherit E : float     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = """_ , Dr35H , eO  : auto  ;   V : function auto   ( out Mr : auto   , inherit out eG : auto   , B : auto    ) inherit jr { }    NR : function void  ( inherit q : array [ 84_6_19_82_8 , 0 , 3 , 0 ] of float      ) inherit Fvq { XNz ( )  ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = """K , l , Q , t  : boolean   = ! ! b     && h   || Crp    * o   && F      >= ! TQNN4    || ""     && ! F    / ! Z        , j   - AbbI0    + - Gy     - ! Jlc   && Y        , ! HL   % SR    + aC   / qE5      != Q ( )    + VuF   % dH    || n       , d   || 4    + Y   + ks       :: ""]"    < 0E8428       ;   Q  : float   ;   U : function array [ 12_66 , 0 , 0 , 0 , 0 , 3_4 , 1164_8128 ] of integer     ( V : array [ 991_28_7_75 ] of boolean      ) inherit L5 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = """T , K  : array [ 4_4100_0 , 0 , 5_192 , 0 ] of boolean    ;   S : function void  ( ) inherit r { G , e  : boolean   ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = """yJ  : array [ 0 , 0 , 0 ] of integer    = - W   * kG     - ! S ( )      >= - s8    || ! b0     * - D      :: L   * C    + - i     - F   && zE    / S   && Dor         ;   aC  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = """H  : auto  = Gj ( )     :: ! - n   || D      <= ! BA       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = """zY : function float    ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = """Q9k , g9xuc_R  : string   = "\\r]"     :: ! uQ   - q    || ! l8        , F    :: 7_0082    <= ! Ua   || l    || YsA        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = """S , w  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = """U , k , M , Z  : float   = ! - CHx    || Y   * w       :: - T    * v    + ! PA    - sd   || a      == a     , - ! KBQ     - zi ( )      :: "\\b"    + ! lKK    + - Cb        , - J    / K     :: _v ( )    - ! qh    - ! U        , l ( )       ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = """r5n : function auto   ( inherit out X : auto   , inherit out MQ : auto    ) inherit m { t  : integer   ;  }    a3 , Q2  : integer   ;   x2 : function void  ( inherit out cd : auto   , inherit out QUotor1 : boolean    , P : array [ 0 ] of boolean     , inherit B : array [ 97 ] of float     , lo : integer    , inherit out Dz : array [ 0 ] of float     , inherit out e : auto    ) inherit aYHJ { }    ap : function void  ( inherit J : auto    ) { O , VDUEDDZ8 , q_gfuJ , i  : array [ 86_36743506 , 279_60 ] of boolean    = A   >= ""      , - Lv    < wR   % gNgd5E     :: - e      , Jj   || L      , Uppn   || Zt    > Fs   + d     :: rpgM   + wO    < AcgZ8b ( )       ;  Ci  : array [ 0 ] of boolean    ;  rb  : array [ 68190 ] of integer    = ! _       ;  break ;   }    V : function float    ( inherit out k : integer     ) { G  : integer   = t   != EP   && k       ;  Fe  : auto  ;  for ( b  = q    :: d   || F      , f ( )    < m2W     , PInQ   - Fb      ) l ( )  ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = """N_ : function array [ 3 , 0 ] of string     ( out UK : auto   , j : string     ) inherit OT { return ;   { continue ;   h1vkIa3 ( )  ;   m ( )  ;   break ;   { return ;   }   K  : boolean   ;  UFxH5TX , uz  : float   ;  }   { a  : array [ 0 , 171 ] of integer    ;  x  : auto  ;  Hh  : boolean   ;  FT ( )  ;   return ;   }   break ;   }    j  : string   ;   Q5T : function auto   ( out r : auto   , inherit nS8 : array [ 0 ] of string     , out ybNug : array [ 0 , 4_0_26_17 ] of string      ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = """fGrhe : function string    ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = """H  : array [ 0 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = """y  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = """oI0k  : float   = R   - x    || 0     * ! b1    || f   + L      > ! - wH    / - yLDw6         ;   b : function void  ( ) inherit T { x , hV , J  : array [ 0 , 0 , 0 ] of integer    = e_   / rX6      , 2    <= - t      , ! C       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = """wg3vf , CPJ3 , C0a  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = """BD : function void  ( ) inherit c { }    FIW , k  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = """U : function array [ 0 , 3 ] of integer     ( ) inherit q { }    v : function void  ( ) inherit H { X , M  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = """_ : function void  ( out H : auto    ) { _V5 , TI , Q  : array [ 762391991_361_6 , 0 , 0 , 0 , 0 ] of string    = u   && O      , ! z     :: C   && P    != ! s      , - D     :: M   + x       ;  }    H  : auto  = ! y   || q    && ! n      <= ! - - udR       :: L   || o    - W   && aWjJ     && O   && KNK    + W   || V      > sT ( )       ;   h : function void  ( ) inherit n { while ( VA   != oY   / C     :: nKl ( )    >= Y   && P      ) continue ;     kz7II  : array [ 4953_07_7_8 , 0 , 58 , 0 , 984_67 ] of string    = B2   - b    >= BD   && BJM     :: U   - P3nx       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = """R  : auto  ;   nYK  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = """ZIDvDv : function void  ( ) { }    BX , L  : auto  = - - tmVL     * z   || K    || Id ( )      < op     , ! aM   * pSP    * YOWFO   || y         ;   a : function array [ 0 , 0 , 0 , 0 ] of boolean     ( ) inherit g { return ;   }    X : function void  ( inherit XpAY : array [ 65 , 0 , 782_13 ] of float      ) inherit E_ { }    wjc : function void  ( ) { do { H ( )  ;   U ( )  ;   }  while ( M   + H    <= L   + u      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = """cm , CUC5O26 , Qh  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = """SC  : array [ 15_0 , 0 ] of float    = Wu   + J    && ! x     + "\]"      :: - QV   % Ms    - ! P      < - Go   / 7         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = """rYQiMZ  : auto  ;   X : function float    ( ) { }    Rm : function void  ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = """TOnE1Kl  : array [ 0 ] of string    = ZI ( )    * vP    < - ! j     - ! 7       :: - - F     - ttC   && D    + v   || UHLetlvw      != ! ! F     || n3uX   * y    - ! Kh         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = """k  : auto  = J   * r   && M     + - ! D         ;   v : function void  ( ) { do { QwJ ( )  ;   QV  : array [ 12170_755 , 9_6_75 , 0 ] of float    ;  }  while ( a ( )    > ! EM     :: J_DSsr   % TJWW    >= - z      ) ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = """QXFWx , vekjm  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = """Y  : array [ 0 ] of string    = ! d   || p    && 5      == E0C   - I    % - NcG     || as ( )    || LZ ( )         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = """i7 : function array [ 356 ] of boolean     ( inherit H : auto   , AFb : array [ 2_8 , 0 , 0 ] of float      ) { d7  = E ( )      ;   Fej  : auto  ;  { break ;   BXtJ , l , C  : array [ 0 , 1_5196 , 0 ] of boolean    ;  o , LwW  : integer   ;  }   H  : array [ 3_1_39 , 293 ] of integer    ;  kb , sNN  : array [ 0 ] of boolean    ;  PCEH , fQO , ICP  : float   = v   + ueE     :: - lY    < q   + xpd2f      , c   / OfL     :: ! pX9K    > o   * CUMv      , - G       ;  Z , K  : boolean   = pe   || Hw     :: ! n    >= C   || v1      , 0    != - Z     :: iU   != - wu       ;  DN  : auto  = a   / jG     :: w   && RC       ;  }    eq : function array [ 419_2030_9846 ] of boolean     ( ) inherit xI { }    DM : function auto   ( AOQd : array [ 28 ] of string      ) { u  : float   = - m       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = """k  : string   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = """wp0 : function auto   ( ) inherit L { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = """Bkee , jg , u , F , gUdF , d  : integer   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = """Gg  : array [ 0 , 0 , 0 ] of boolean    = - os    % - JUayA     || g     :: ! ! Js     / - R   || xa         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = """Iao  : array [ 4_374 , 66124_912 , 0 , 24_892976 , 4_39_7 , 0 , 9 , 92_9 ] of string    = r2   / zHo    / - S     - - j    % - ve         ;   m : function array [ 5_45 ] of string     ( out s : array [ 0 , 0 , 4 , 0 , 32 , 0 , 0 ] of float     , inherit w : array [ 8 ] of float     , inherit t : boolean    , out A : boolean     ) inherit ofpXO5bQ { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = """v  : string   ;   r : function integer    ( ) { }    TuWE  : integer   = "#\\\'"     :: - d ( )        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = """s , tWh  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = """_e : function void  ( ) inherit v { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = """m : function void  ( ) inherit V9N { r  = w   == e   % DXb     :: ! NL    > D   + Dt      ;   }    d : function array [ 0 , 1 , 6 , 1_257_9 ] of boolean     ( out ON : array [ 0 , 1 ] of integer     , out g : auto   , K : float    , inherit Z : auto    ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = """c1z5T : function void  ( out _ : auto   , out H : integer     ) inherit tmcH { _  : string   = iGI ( )     :: d   * g    != N      ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = """r  : integer   = ! k    * - ! aL3YW       :: XUb   || w   / r     - a   / _m    && 6         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = """zu  : auto  ;   az : function float    ( inherit ZC : array [ 0 , 0 ] of integer      ) inherit d { d , E , Td  : auto  ;  }    b  : array [ 7 , 0 , 0 ] of integer    = ! ! RCAHc3    || ""      != - - J    || _   && fka         ;   u : function auto   ( ) { KV , i , A , eE  : array [ 0 , 0 ] of float    ;  p , g , C , sl , XfnD , r , y  : integer   = SH   + _    != KC   - cr     :: F   + B4GR      , S8wm   + BI    != k   % t6      , - YiB      , J ( )    == ""     :: J   - U6      , - v    == A   - y9     :: cZLP   / Ts      , N   - _      , ! K     :: ! ZU_sZ    <= l7   || b       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = """U , XN , _ , M  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = """pG : function string    ( inherit out S : array [ 62 ] of boolean      ) { }    fc : function void  ( ) { if ( E4   || fh4K    < _   / P     :: uB   / QnQ    <= vz     ) continue ;     }    hyPF , akf , Yn  : array [ 54 , 5_7_1_9 ] of string    = ! ""    || ymtN   / C        , - fD    <= o   % B    - ax   + bR6     * - z   % s3r        , ! - GT     || H   - E    - - rhV         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = """T , th  : array [ 82_7_0_8 ] of integer    ;   ol  : array [ 5240_5 ] of float    = - ""     != ! - 1         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = """e : function void  ( inherit _agJ : float     ) inherit J { UE0  = - J9DR     :: ! M    > j   * x      ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = """m , b , H , r  : auto  = ! ! zzP    || u     < ! - ! bZP       :: ! 0     / - iL ( )        , - ItBrZE     :: F ( )    % PcfMUPC ( )    / - Z      <= wi     , - ! - A        , - q   / S    + yr7DLFy   - t9      >= wIFE ( )       ;   IFe : function void  ( ) inherit T { while ( i0oGK   || g0    < KAA   || G      ) break ;     }    iV : function string    ( inherit yIWlk : array [ 0 ] of float     , out a : array [ 2 , 0 ] of string     , o5P8 : auto   , out yip : array [ 0 ] of string     , inherit out l : array [ 0 ] of integer      ) { }    P : function integer    ( inherit B : integer    , pG : array [ 2 , 249_3_4 ] of float     , inherit out C : boolean     ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = """GthB  : float   = ! ! zvm2     && LNnu    >= - ! l    + iaq   + lqCd8         ;   Wx , Gox , n  : boolean   = - - o   || f      == ! - r     % ! CB   || zWj        , ! - Tf    * - o3wu      > ! E   * w     || g6      , XV ( )    < ! a   * kz    - E   - kA         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = """wqvvT0 : function auto   ( ) { }    r2 , z , QVB  : auto  ;   N : function void  ( inherit Z : array [ 996_3 , 96 , 53 , 0 , 16_34 , 0 ] of string     , out pl : boolean     ) inherit U9CJ { }    g : function void  ( ) inherit ii5CpY { { }   break ;   }    kK  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = """Z9 : function float    ( ) inherit nl7 { }    Hu8E , Ha , O , i0  : float   ;   UP : function void  ( ) { s  : auto  = hLZ   - Y    != m   && _       ;  break ;   }    lKCo  : auto  = ! V ( )     && o   / M    * B626 ( )       :: ! ! Gn     / - ! rrN      > ! ! m90PuXw     + - VQh ( )         ;   eQZi4 , U , x , Tijg  : array [ 7_31 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = """Fd01  : array [ 0 , 0 ] of float    ;   J : function auto   ( inherit d : array [ 80610529_3 ] of integer      ) inherit Pr { f , bY  : boolean   ;  I ( )  ;   }    V : function array [ 6 ] of float     ( inherit out qL_ : auto    ) inherit h { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = """FS  : boolean   = 0    > r   || false        ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = """ox , J  : auto  = - w6Gm   && z    || 0      >= - ! ""        , ! j    - quUF   % QoYOK     + ! c    - aZ   - Blm      <= OJr   - j   % l    % - qS       :: vK   - RQ    % ou_   && L     && YF   - mdO    * b ( )      == ny      ;   Q0kIER , M2  : auto  ;   NI : function auto   ( inherit out w : array [ 0 , 0 , 2 ] of boolean     , O81vV : boolean     ) { hWa9  = m   % s      ;   srldI8F  : auto  = - u    > M ( )     :: ! QdTqPt    == YZ   % A       ;  b  : float   = - V    <= w   - uMA       ;  }    F , U , j  : auto  ;   H8pQ : function string    ( inherit out U : auto   , inherit out C : auto   , out gui : array [ 95 ] of integer     , inherit n : string     ) { for ( Mk  = ! d    == _Q   * ssH0     :: UxqqlL2A   || e      , wR   || Wr    == qT   || PhKu     :: smD   * JP      , - X      ) break ;     }    b , H  : boolean   = "\\b"    + ! oYBX1p   + SqBH      >= ! i ( )      :: ! - ! vX      >= - ! w    % ! Xt        , ! ! wW    - ! FY         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = """I : function void  ( ) inherit i { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = """K , l , HPLP  : boolean   = - rC   || l    + ""      < sPsHpKKH   * h    % A    * o     :: ! Tcq   * cMc    - h9   - G        , ! ""     + v   + OV    || C7   % M       :: ! F    || ea   - w    && X   + aVF      <= E     , - WeS    % rye9Di4   + O1p     + O    < - z   || RB     / ! k    * ! D3       :: I ( )    && - - L         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = """BND : function integer    ( ) inherit KEAR { lP1s  : auto  = - z    != ! n28     :: g   || IM       ;  d  : array [ 96_76_75_311 ] of string    ;  }    jQ9PG9 , I , K , y , Vh , w , co  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = """Qp8 : function array [ 0 ] of float     ( ) inherit G { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = """Od , Q , X5Q  : array [ 0 , 0 ] of boolean    = ! 0     + R   + c    && y   + Z       :: z ( )      , ! N   + d     || PoE5C    > - ! Xe ( )        , ! - FWZ   || VP       :: ! d   - z    && - y1      > - c    || ! T     && GJ   * ZW    && W   * ez         ;   n , N , J , RsV  : auto  ;   OZV : function array [ 0 ] of float     ( ) inherit p { WqH  = ! w5P    < - p     :: acSXtN3rq4   / za      ;   LYX  = zWINr   || f6      ;   UJh  : auto  ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = """nA : function array [ 0 ] of integer     ( ) { }    fXx  : array [ 7 ] of boolean    ;   Oa : function auto   ( ) inherit O { obAj , G  : auto  ;  YC , nqHf , rb , qk , F , jBx  : auto  = - gL02Qnxo    >= ! _D      , - LB4     :: ! R    >= 6      , Uz   - X    <= ! YS     :: _I   / _    == ! Lsmj      , zk9   - v    > - O     :: Ev1   > q   % O      , ZYI   + H3jg    >= TMxF ( )     :: p7   * X      , R   / C    >= M ( )     :: U ( )    > ! UL0O       ;  for ( s  = W   % F    != - c     :: 6      , u   / QCjW      , Y   && vp    > - _     :: - q      ) continue ;     }    f  : array [ 0 ] of integer    ;   kK : function auto   ( inherit out G : array [ 0 , 0 , 34 ] of float     , inherit v : array [ 0 ] of boolean      ) inherit qM { b , UY  : array [ 0 , 9_4 ] of boolean    ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = """vacb , gP  : array [ 4 , 0 ] of integer    = Gc   * u    * A    && - Pd   / pc      >= S_ ( )     :: - - Jd   % Np      != ! b ( )     && - ! m        , - qN   && S    || V   / ITsA       :: ! sU    || D   % JEt     * x   || pl    || ""      == x6   / R    + I   % pU     + QSg ( )        ;   C : function void  ( ) inherit z { }    iQ  : auto  ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = """q : function array [ 0 ] of string     ( inherit _ : string    , out m : auto    ) { do { }  while ( ABj   * K     :: K   <= - l      ) ;   }    C : function auto   ( ) inherit f9ia { x  : boolean   ;  if ( l   || p     :: - W    <= 0      ) Wy ( )  ;   else aF ( )  ;     w , w  : float   = Y   <= o   - k     :: 8      , ! M_     :: E ( )       ;  { }   continue ;   break ;   }    mV  : boolean   ;   J : function array [ 71 , 7 , 0 , 7 , 0 , 0 , 0 , 8493 , 0 ] of string     ( ) inherit _E { }    t : function void  ( ) inherit R { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = """MZ , E  : auto  ;   P , Z  : array [ 2 , 94 , 16_36_304 ] of boolean    = ! j    - Li    - ! Qnw   % Q       :: ! LgEZ   % FS    * eO   || U        , - z    + FB   % i     + pELoU   - F    && Zk   || at       :: - ! m   / l      == ! CQ    && gu   || t     || md3FgL2   + m    && iNlI   % VZJ         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = """R : function void  ( out XA6f : auto   , e : string    , inherit lt : auto   , G : boolean     ) inherit ha { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = """ykfO : function auto   ( j : integer     ) { }    u0  : array [ 0 , 0 ] of string    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = """Z , nv  : auto  ;   Y : function void  ( ) inherit fO { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = """Jnd , k , X , w  : string   ;   m , w , H  : auto  = ! qx    * - w    || - w      != - r   / H6    % ! P       :: t ( )    || - r    - v   || T0      != q   * esbSD   || oq    && - r        , true    > ! - d   / s        , igJ   <= ! - HJnwNI      :: - vr    && ! B     + { }      >= m   && eEb    % meKul   + q     / ! efk   || D         ;   d : function void  ( K7 : integer     ) { }    j  : array [ 906626 ] of float    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = """y : function void  ( inherit out V5 : boolean     ) { }    ed , t , NG , ak  : array [ 37_6_9 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = """F : function string    ( ) { z , Ly  : auto  = ! dIT    > o     , - IS7u    >= v   && l       ;  }    wOL : function auto   ( inherit out X : string     ) { a , q  : array [ 0 , 2 , 986_26 ] of integer    = y   / D     :: w   && ldvG      , ! s       ;  break ;   }    B : function array [ 0 , 8 ] of integer     ( ) { l , m , htUhV  : array [ 5585_10 ] of string    ;  T  : boolean   = - H     :: h   && Ii    >= IpGEeSJ   && X       ;  }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = """R70m , D , ySG  : boolean   = _GH5xR ( )    || Xohq6   / i    / wX   + s        , fAiAz ( )    < ljjl ( )     :: Kk ( )    / Z   % ww     || ! - Kb        , Y   || l ( )     <= ! NGb    % GH   || P     % - z    && - o         ;   Ve_ : function void  ( ) inherit e { EOpx  : auto  ;  }    t , K , T  : auto  ;   Ni  : string   ;   B , T  : auto  ;   Fa , oJwO4z4 , Yu  : float   = ! NL   / mb    || G   || b       :: ! u    + H   || Mpe     % "\\b"     < K6   && ! Wl     * false       , ! Tl    - - H     * - A   % T      < ! M   * K     || ! ! y        , E ( )    < K   % QV    + - K     || ! WuBHP   % C       :: " "    || ! V7si    % Y   - O         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = """w : function void  ( ) inherit k8 { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = """p_ , wv  : float   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = """OD , Mga , HEeA , rE0r7 , a  : float   = e ( )    - O   || afB     || ! q    * ! DOXW        , YelBR2Pv   >= false      , - ""     / - L ( )        , v3jk   != ! jo    % b   - W    + Tx   && F        , - - - B      >= - - f     % ! ""         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = """ra : function auto   ( ) inherit b { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = """K : function auto   ( out G : integer     ) inherit F { }    _DE : function array [ 0 , 4_5 ] of integer     ( ) inherit fW { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = """L  : array [ 0 ] of boolean    ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = """i : function array [ 0 ] of integer     ( ) inherit j { Z74vKPj  : boolean   = Ra   * m     :: DvY      ;  }    _v , z  : array [ 2 , 1778 ] of integer    ;   Sa : function void  ( ) inherit x { }    f : function void  ( iur : auto   , out aml : integer    , inherit out BP : integer     ) inherit MXB { do { }  while ( M   || tF    >= - u      ) ;   return ;   }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = """Myf7h5qPQ , I , z7  : auto  ;   nQ , Z  : auto  = ! Z   + ixxq    + - t      >= Q ( )    % ! - U        , - N ( )    - - Ik0      < - - ! k         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = """YPO  : boolean   ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = """AjCt : function auto   ( ) { while ( f   % n    == Ev   * u      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = """TJ  : auto  = "\\f"    == - t    * ! Ook     % ! Ga   && E         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = """E  : float   = nP   % - ! Q       :: ! ! j ( )      != ! J    * q   || Re     || ! mT_fUO   && g         ;   """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = """v , C , K , H6 , cI  : auto  = ! e   % eJt    % rt   / qiqP7      == ! - e     - MB   || a    || ! X       :: ! uGs    / J   - f     || MX6j   / qy    / ! El        , - ""       , ! ! F   || H        , - eT   / p     - - t     <= 0    % - ! IYt       :: Y   < ! - N   && G        , ! Wws   % GP     / z   - ! t      < y6 ( )       ;   G : function auto   ( ) { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = """p_OR : function boolean    ( ) inherit j { }    y9Ko : function array [ 1_933 , 6 , 9_64_2_52427_2_495563 , 70_6_2 , 6 ] of boolean     ( ) { if ( x   + L      ) return ;     }    B : function auto   ( out C : auto   , C : string    , inherit out b : auto   , inherit tiq : auto   , out h4_ : auto   , inherit e : auto    ) inherit AW { }    K : function void  ( out _84 : float     ) inherit _cRtdV { pG , r  : auto  = Y   && GIZ    > - e      , r7   || u       ;  }    i  : array [ 0 , 79111 ] of integer    = - YQYQk   * A    && g0   || Iy       :: C ( )    - - ! _7e0B         ;   D : function auto   ( ) { r  = - qb    >= W3fs   * l3u     :: WJK   || T    > ""      ;   F , _ , hP , VatliV  : boolean   ;  }    l4 : function array [ 0 ] of string     ( out U : float    , inherit out eX : auto    ) inherit JIO { }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 300))
	def test_301(self):
		input = """AP  : array [ 0 , 0 , 0 , 8 ] of float    = ! H   * Fw   / h      > RK    :: "\t"    < "\""       ;   t : function auto  ( out R : integer    , inherit G : array [ 0 ] of boolean      ) inherit O { while ( _   || o      ) return ;     }    """
		expect = "successful"
		self.assertTrue(TestParser.test(input, expect, 301))
		
	def test_330(self):
	    input = """a:string = "\\f"; """
	    expect = "successful"
	    self.assertTrue(TestParser.test(input, expect, 330))