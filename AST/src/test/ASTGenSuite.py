import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
	#########################################################################
	#                           TEST DECLARATION                            #
	#########################################################################
	def test_300_short_vardecl(self):
		input = """x: integer;"""
		expect = str(Program([VarDecl("x", IntegerType())]))
		self.assertTrue(TestAST.test(input, expect, 300))

	def test_301_full_vardecl(self):
		input = """x, y, z: integer = 1, 2, 3;"""
		expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302_vardecls(self):
		input = """x, y, z: integer = 1, 2, 3;
		a, b: float;"""
		expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 302))
	#########################################################################
	#                         TEST COMPLEX PROGRAM                          #
	#########################################################################

	def test_303_simple_program(self):
		"""Simple program"""
		input = """main: function void () {
		}"""
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304_complex_program_1(self):
		"""More complex program"""
		input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
main: function void () {
	 printInteger(4);
}"""
		expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_306_complex_program_2(self):
		input = """
		rJ  : auto  = - B    :: eH   + X     < wfvN   && X    * ! Dv0       ;
		t  : auto  = - N0jPYFF    :: ""       ;
		mr , l , m7  : array [ 46 , 0 , 0 , 0 ] of integer    ;
		l2U : function auto   ( ) {
			break ;
			c , gSuc , Xh  : integer   ;
		}
		WW , t  : array [ 17 , 4 , 6822_1 , 0 ] of string    ;
		B_ : function auto   ( ) inherit IC {
			continue ;
			Gue , BtP_nZ  : integer   ;
		}
		P : function auto   ( j1 : auto    ) inherit F6KUr { }
		W : function auto   ( inherit c : auto    ) inherit jn { }    """
		expect = """Program([
	VarDecl(rJ, AutoType, BinExpr(::, UnExpr(-, Id(B)), BinExpr(<, BinExpr(+, Id(eH), Id(X)), BinExpr(&&, Id(wfvN), BinExpr(*, Id(X), UnExpr(!, Id(Dv0)))))))
	VarDecl(t, AutoType, BinExpr(::, UnExpr(-, Id(N0jPYFF)), StringLit()))
	VarDecl(mr, ArrayType([46, 0, 0, 0], IntegerType))
	VarDecl(l, ArrayType([46, 0, 0, 0], IntegerType))
	VarDecl(m7, ArrayType([46, 0, 0, 0], IntegerType))
	FuncDecl(l2U, AutoType, [], None, BlockStmt([BreakStmt(), VarDecl(c, IntegerType), VarDecl(gSuc, IntegerType), VarDecl(Xh, IntegerType)]))
	VarDecl(WW, ArrayType([17, 4, 68221, 0], StringType))
	VarDecl(t, ArrayType([17, 4, 68221, 0], StringType))
	FuncDecl(B_, AutoType, [], IC, BlockStmt([ContinueStmt(), VarDecl(Gue, IntegerType), VarDecl(BtP_nZ, IntegerType)]))
	FuncDecl(P, AutoType, [Param(j1, AutoType)], F6KUr, BlockStmt([]))
	FuncDecl(W, AutoType, [InheritParam(c, AutoType)], jn, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_320_complex_program_3(self):
		input = """
		W , nzD  : string   ;
		G : function auto   ( out o : auto   , m : array [ 3 , 0 ] of boolean     , off : auto    ) { }
		M : function void  ( out u : array [ 0 ] of string      ) inherit O {
			YA  : array [ 0 , 0 ] of float    = mD   - SE    <= tZN1   - H       ;
			Un  : boolean   ;
		}    """
		expect = """Program([
	VarDecl(W, StringType)
	VarDecl(nzD, StringType)
	FuncDecl(G, AutoType, [OutParam(o, AutoType), Param(m, ArrayType([3, 0], BooleanType)), Param(off, AutoType)], None, BlockStmt([]))
	FuncDecl(M, VoidType, [OutParam(u, ArrayType([0], StringType))], O, BlockStmt([VarDecl(YA, ArrayType([0, 0], FloatType), BinExpr(<=, BinExpr(-, Id(mD), Id(SE)), BinExpr(-, Id(tZN1), Id(H)))), VarDecl(Un, BooleanType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321_complex_program_4(self):
		input = """
		Zo : function void  ( ) {
			o  : integer   = x   && A_     :: c   && NUMQx    != qQ   || Rm       ;
		}
		Ds : function void  ( out v : array [ 756 , 463_01 , 5_1 ] of boolean      ) inherit O {
			XKD , t61xzS  : array [ 0 ] of string    = - K    < v   && A     :: ! go      , V   || t     :: C   % C    < - _o       ;
		}
		Ye : function void  ( ) {
			for ( qO  = ! t    != Z3   / oZ     :: ! lC    >= - y4n      , off   || o4    != ! b     :: 3    == ""      , Q   || cdBAD      )
				return ;
			break ;
			S5Ri0 , gXRUg7 , QJ , A , CSq , b , x , VLo  : array [ 0 ] of float    ;
		}
		y : function void  ( ) inherit b { }    """
		expect = """Program([
	FuncDecl(Zo, VoidType, [], None, BlockStmt([VarDecl(o, IntegerType, BinExpr(::, BinExpr(&&, Id(x), Id(A_)), BinExpr(!=, BinExpr(&&, Id(c), Id(NUMQx)), BinExpr(||, Id(qQ), Id(Rm)))))]))
	FuncDecl(Ds, VoidType, [OutParam(v, ArrayType([756, 46301, 51], BooleanType))], O, BlockStmt([VarDecl(XKD, ArrayType([0], StringType), BinExpr(::, BinExpr(<, UnExpr(-, Id(K)), BinExpr(&&, Id(v), Id(A))), UnExpr(!, Id(go)))), VarDecl(t61xzS, ArrayType([0], StringType), BinExpr(::, BinExpr(||, Id(V), Id(t)), BinExpr(<, BinExpr(%, Id(C), Id(C)), UnExpr(-, Id(_o)))))]))
	FuncDecl(Ye, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(qO), BinExpr(::, BinExpr(!=, UnExpr(!, Id(t)), BinExpr(/, Id(Z3), Id(oZ))), BinExpr(>=, UnExpr(!, Id(lC)), UnExpr(-, Id(y4n))))), BinExpr(::, BinExpr(!=, BinExpr(||, Id(off), Id(o4)), UnExpr(!, Id(b))), BinExpr(==, IntegerLit(3), StringLit())), BinExpr(||, Id(Q), Id(cdBAD)), ReturnStmt()), BreakStmt(), VarDecl(S5Ri0, ArrayType([0], FloatType)), VarDecl(gXRUg7, ArrayType([0], FloatType)), VarDecl(QJ, ArrayType([0], FloatType)), VarDecl(A, ArrayType([0], FloatType)), VarDecl(CSq, ArrayType([0], FloatType)), VarDecl(b, ArrayType([0], FloatType)), VarDecl(x, ArrayType([0], FloatType)), VarDecl(VLo, ArrayType([0], FloatType))]))
	FuncDecl(y, VoidType, [], b, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 321))
	#########################################################################
	#                           TEST EXPRESSION                             #
	#########################################################################

	def test_305_complex_expr(self):
		"""Expression"""
		input = """x:integer = -1+2||"ditmemay"*x&&44::rrow-3-4--2;"""
		expect = """Program([
	VarDecl(x, IntegerType, BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(-, IntegerLit(1)), IntegerLit(2)), BinExpr(*, StringLit(ditmemay), Id(x))), IntegerLit(44)), BinExpr(-, BinExpr(-, BinExpr(-, Id(rrow), IntegerLit(3)), IntegerLit(4)), UnExpr(-, IntegerLit(2)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_307_operands_1(self):
		"""Operands"""
		input = """x:integer = (213+_djw::kew(ditmemay))*(srr::kek);"""
		expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, BinExpr(::, BinExpr(+, IntegerLit(213), Id(_djw)), FuncCall(kew, [Id(ditmemay)])), BinExpr(::, Id(srr), Id(kek))))
])"""
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_326_operands_2(self):
		"""Operands"""
		input = """x:string = {b[1],foo(),1.1,22_1,"\t",(h-h)}"""
		expect = """Program([
	VarDecl(x, StringType, ArrayLit([ArrayCell(b, [IntegerLit(1)]), FuncCall(foo, []), FloatLit(1.1), IntegerLit(221), StringLit(	), BinExpr(-, Id(h), Id(h))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327_relational_expr(self):
		"""Relational Expr"""
		input = """x:string = (x==y)!=h;"""
		expect = """Program([
	VarDecl(x, StringType, BinExpr(!=, BinExpr(==, Id(x), Id(y)), Id(h)))
])"""
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328_all_op(self):
		"""Relational Expr"""
		input = """x:auto=x[x]::x>=!x&&x+x%-x"""
		expect = """Program([
	VarDecl(x, AutoType, BinExpr(::, ArrayCell(x, [Id(x)]), BinExpr(>=, Id(x), BinExpr(&&, UnExpr(!, Id(x)), BinExpr(+, Id(x), BinExpr(%, Id(x), UnExpr(-, Id(x))))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_331_unary_expr(self):
		"""Relational Expr"""
		input = """x:string = -!!-a[2];"""
		expect = """Program([
	VarDecl(x, StringType, UnExpr(-, UnExpr(!, UnExpr(!, UnExpr(-, ArrayCell(a, [IntegerLit(2)]))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 331))
	#########################################################################
	#                             TEST STATEMENT                            #
	#########################################################################

	def test_308_scalar_var(self):
		"""scalar variable and for loop"""
		input = """
		K6y : function void  ( ) inherit sz {
			wc  : array [ 43781 ] of integer     = gB0   && Rn     :: u5n ( )       ;
		}
		d4 , wl  : integer   ;
		g3D  : array [ 2_0 ] of string    ;
		a : function void  ( inherit out g : auto    ) inherit Z {
			for ( j = Mji   * P      , ""     :: - f    != lgw   || T      , J   + d     :: t   || k9    < _     )
				return ;
			oz , p  : auto  = s ( )    < - s      , Sg   % B    == - IZ       ;
		}"""
		expect = """Program([
	FuncDecl(K6y, VoidType, [], sz, BlockStmt([VarDecl(wc, ArrayType([43781], IntegerType), BinExpr(::, BinExpr(&&, Id(gB0), Id(Rn)), FuncCall(u5n, [])))]))
	VarDecl(d4, IntegerType)
	VarDecl(wl, IntegerType)
	VarDecl(g3D, ArrayType([20], StringType))
	FuncDecl(a, VoidType, [InheritOutParam(g, AutoType)], Z, BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(*, Id(Mji), Id(P))), BinExpr(::, StringLit(), BinExpr(!=, UnExpr(-, Id(f)), BinExpr(||, Id(lgw), Id(T)))), BinExpr(::, BinExpr(+, Id(J), Id(d)), BinExpr(<, BinExpr(||, Id(t), Id(k9)), Id(_))), ReturnStmt()), VarDecl(oz, AutoType, BinExpr(<, FuncCall(s, []), UnExpr(-, Id(s)))), VarDecl(p, AutoType, BinExpr(==, BinExpr(%, Id(Sg), Id(B)), UnExpr(-, Id(IZ))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309_scalar_var(self):
		"""scalar variable and assign statement"""
		input = """
		jZ : function auto   ( ) inherit ho {
			iq = jG   - E     :: ! H    == s3Mc ( )      ;
			for ( AA = ! bJkg    == l   - vk      , ! x      , - AS     :: ht6pi ( )    < ! o      )
				_H ( )  ;
			keke[423,2+jj::boo]=_329(duca);
		}"""
		expect = """Program([
	FuncDecl(jZ, AutoType, [], ho, BlockStmt([AssignStmt(Id(iq), BinExpr(::, BinExpr(-, Id(jG), Id(E)), BinExpr(==, UnExpr(!, Id(H)), FuncCall(s3Mc, [])))), ForStmt(AssignStmt(Id(AA), BinExpr(==, UnExpr(!, Id(bJkg)), BinExpr(-, Id(l), Id(vk)))), UnExpr(!, Id(x)), BinExpr(::, UnExpr(-, Id(AS)), BinExpr(<, FuncCall(ht6pi, []), UnExpr(!, Id(o)))), CallStmt(_H, )), AssignStmt(ArrayCell(keke, [IntegerLit(423), BinExpr(::, BinExpr(+, IntegerLit(2), Id(jj)), Id(boo))]), FuncCall(_329, [Id(duca)]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310_funcall_callstmt(self):
		"""scalar variable and assign statement"""
		input = """
		jZ : function auto   ( ) inherit ho {
			calm(dem, as::3928<_dw,_bitch(_dun(sun,!hux--m)));
			x:string=lemw(bu,tu,9,_0(_0));
		}"""
		expect = """Program([
	FuncDecl(jZ, AutoType, [], ho, BlockStmt([CallStmt(calm, Id(dem), BinExpr(::, Id(as), BinExpr(<, IntegerLit(3928), Id(_dw))), FuncCall(_bitch, [FuncCall(_dun, [Id(sun), BinExpr(-, UnExpr(!, Id(hux)), UnExpr(-, Id(m)))])])), VarDecl(x, StringType, FuncCall(lemw, [Id(bu), Id(tu), IntegerLit(9), FuncCall(_0, [Id(_0)])]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311_ifstmt(self):
		"""if statement"""
		input = """kw: function auto (){
			if ( GP ( )     :: Wd   + E    != x   + d4      )
				if (x > 23/meme)
					if (dumm != dummew(dumew_(3)))
						calm(stem);
			else bN ( )  ;
		}"""
		expect = """Program([
	FuncDecl(kw, AutoType, [], None, BlockStmt([IfStmt(BinExpr(::, FuncCall(GP, []), BinExpr(!=, BinExpr(+, Id(Wd), Id(E)), BinExpr(+, Id(x), Id(d4)))), IfStmt(BinExpr(>, Id(x), BinExpr(/, IntegerLit(23), Id(meme))), IfStmt(BinExpr(!=, Id(dumm), FuncCall(dummew, [FuncCall(dumew_, [IntegerLit(3)])])), CallStmt(calm, Id(stem)), CallStmt(bN, ))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312_whilestmt(self):
		"""while/do while statement"""
		input = """aa: function void(){
			do {
				j , y  : string   ;
				while( yolov == mum*32.1e9)
					return 922;
			}
			while ( yy   / s    >= U   / IAliRy      ) ;
		}"""
		expect = """Program([
	FuncDecl(aa, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>=, BinExpr(/, Id(yy), Id(s)), BinExpr(/, Id(U), Id(IAliRy))), BlockStmt([VarDecl(j, StringType), VarDecl(y, StringType), WhileStmt(BinExpr(==, Id(yolov), BinExpr(*, Id(mum), FloatLit(32100000000.0))), ReturnStmt(IntegerLit(922)))]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 312))
	#########################################################################
	#                           TEST CONVERT LITERAL                        #
	#########################################################################

	def test_313_float_1(self):
		"""Float Literal"""
		input = """dd:string= 1.e3;"""
		expect = """Program([
	VarDecl(dd, StringType, FloatLit(1000.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314_float_2(self):
		"""Float Literal"""
		input = """d:string= .1e2;"""
		expect = """Program([
	VarDecl(d, StringType, FloatLit(10.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315_float_3(self):
		"""Float Literal"""
		input = """fl:float=1_1.1e1;"""
		expect = """Program([
	VarDecl(fl, FloatType, FloatLit(111.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316_float_4(self):
		"""Float Literal"""
		input = """ed:float=.e4;"""
		expect = """Program([
	VarDecl(ed, FloatType, FloatLit(0.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_322_float_4(self):
		"""Float Literal"""
		input = """ed:float=.E4;"""
		expect = """Program([
	VarDecl(ed, FloatType, FloatLit(0.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_317_string_1(self):
		"""String Literal"""
		input = """stri:string="11";"""
		expect = """Program([
	VarDecl(stri, StringType, StringLit(11))
])"""
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318_bool_1(self):
		"""Bool Literal"""
		input = """boo:boolean=true;"""
		expect = """Program([
	VarDecl(boo, BooleanType, BooleanLit(True))
])"""
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319_int_1(self):
		"""Integer Literal"""
		input = """arr:array[2,3] of integer ={2,d/4,9};"""
		expect = """Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(2), BinExpr(/, Id(d), IntegerLit(4)), IntegerLit(9)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 319))
	#########################################################################
	#                           TEST TYPE CONFLICT                          #
	#########################################################################
	def test_323_type_2(self):
		"""bool type"""
		input = """boo:auto;"""
		expect = """Program([
	VarDecl(boo, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 323))
	#########################################################################
	#                         TEST NAME/ID PLACEMENT                        #
	#########################################################################

	def test_324_name_1(self):
		"""array cell"""
		input = """main:function void(){bam[1,2,3] = "";}"""
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(bam, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), StringLit())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325_name_2(self):
		"""func call"""
		input = """main:function void(){bam = foo();}"""
		expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(bam), FuncCall(foo, []))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_329_name_3(self):
		"""param decl"""
		input = """main:function void(x: string){}"""
		expect = """Program([
	FuncDecl(main, VoidType, [Param(x, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 329))
	#########################################################################
	#                               TEST RANDOM                             #
	#########################################################################

	def test_332(self):
		input = """Dykmx : function void ( ) inherit _E { G , lu , QK , r  : auto  = Ju   + eQ    != i   - s      , bR   + t     :: 3      , ! l      , t   || q    != ! h     :: - FZy       ;  while ( ! T    == ! ZR      ) continue ;     }    """
		expect = """Program([
	FuncDecl(Dykmx, VoidType, [], _E, BlockStmt([VarDecl(G, AutoType, BinExpr(!=, BinExpr(+, Id(Ju), Id(eQ)), BinExpr(-, Id(i), Id(s)))), VarDecl(lu, AutoType, BinExpr(::, BinExpr(+, Id(bR), Id(t)), IntegerLit(3))), VarDecl(QK, AutoType, UnExpr(!, Id(l))), VarDecl(r, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, Id(t), Id(q)), UnExpr(!, Id(h))), UnExpr(-, Id(FZy)))), WhileStmt(BinExpr(==, UnExpr(!, Id(T)), UnExpr(!, Id(ZR))), ContinueStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = """N , uej  : auto  = - F   % AV7P     % cUf   * wT    || _   - U        , - ! I   - aaF         ;   """
		expect = """Program([
	VarDecl(N, AutoType, BinExpr(||, BinExpr(*, BinExpr(%, BinExpr(%, UnExpr(-, Id(F)), Id(AV7P)), Id(cUf)), Id(wT)), BinExpr(-, Id(_), Id(U))))
	VarDecl(uej, AutoType, BinExpr(-, UnExpr(-, UnExpr(!, Id(I))), Id(aaF)))
])"""
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = """HC , mQ  : auto  = e ( )    < - ldWx     :: _   && p    + i   - eglM2O2     + ""    / r   / J        , - m   % Z    && w   || WJ         ;   """
		expect = """Program([
	VarDecl(HC, AutoType, BinExpr(::, BinExpr(<, FuncCall(e, []), UnExpr(-, Id(ldWx))), BinExpr(&&, Id(_), BinExpr(+, BinExpr(-, BinExpr(+, Id(p), Id(i)), Id(eglM2O2)), BinExpr(/, BinExpr(/, StringLit(), Id(r)), Id(J))))))
	VarDecl(mQ, AutoType, BinExpr(||, BinExpr(&&, BinExpr(%, UnExpr(-, Id(m)), Id(Z)), Id(w)), Id(WJ)))
])"""
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = """Zq : function void ( inherit out a : auto   , M3 : auto    ) { }    """
		expect = """Program([
	FuncDecl(Zq, VoidType, [InheritOutParam(a, AutoType), Param(M3, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = """r : function void ( ) inherit I { edjMa  : array [ 0 , 7_5_9 , 0 ] of boolean    ;  }    r , n , iZ , HeRAkG , sQF , n  : auto  ;   b : function integer   ( ) inherit a { }    """
		expect = """Program([
	FuncDecl(r, VoidType, [], I, BlockStmt([VarDecl(edjMa, ArrayType([0, 759, 0], BooleanType))]))
	VarDecl(r, AutoType)
	VarDecl(n, AutoType)
	VarDecl(iZ, AutoType)
	VarDecl(HeRAkG, AutoType)
	VarDecl(sQF, AutoType)
	VarDecl(n, AutoType)
	FuncDecl(b, IntegerType, [], a, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = """v8 , kveaI  : auto  ;   """
		expect = """Program([
	VarDecl(v8, AutoType)
	VarDecl(kveaI, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = """eH : function auto  ( inherit f5 : array [ 0 ] of boolean     , out H : array [ 0 , 74873 , 0 , 384_85 ] of string     , tT : boolean    , inherit xck : array [ 0 ] of float     , inherit out gTKO990Xl : array [ 58 ] of float      ) { }    """
		expect = """Program([
	FuncDecl(eH, AutoType, [InheritParam(f5, ArrayType([0], BooleanType)), OutParam(H, ArrayType([0, 74873, 0, 38485], StringType)), Param(tT, BooleanType), InheritParam(xck, ArrayType([0], FloatType)), InheritOutParam(gTKO990Xl, ArrayType([58], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = """wY : function void ( ) { n  : array [ 21_6 , 0 , 0 ] of integer    ;  }    """
		expect = """Program([
	FuncDecl(wY, VoidType, [], None, BlockStmt([VarDecl(n, ArrayType([216, 0, 0], IntegerType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = """h : function string   ( ) { zK , DXY  : float   = Lw   && J    < Kw   + z     :: ! fkEa      , D3   && qo    >= - MF45Tz     :: ! dL    == x   - Lzs       ;  U  : auto  ;  r , OFp , AJdR2ea , q  : float   ;  while ( - f6    == ! XhH5      ) return ;     }    v , j , O3 , IJ , TGkhe  : float   ;   m : function float   ( ) inherit A5 { ncO , jX , i9  : auto  ;  }    f3 , W , P  : array [ 8 , 0 , 8_2 ] of integer    ;   c : function void ( ) inherit S { }    """
		expect = """Program([
	FuncDecl(h, StringType, [], None, BlockStmt([VarDecl(zK, FloatType, BinExpr(::, BinExpr(<, BinExpr(&&, Id(Lw), Id(J)), BinExpr(+, Id(Kw), Id(z))), UnExpr(!, Id(fkEa)))), VarDecl(DXY, FloatType, BinExpr(::, BinExpr(>=, BinExpr(&&, Id(D3), Id(qo)), UnExpr(-, Id(MF45Tz))), BinExpr(==, UnExpr(!, Id(dL)), BinExpr(-, Id(x), Id(Lzs))))), VarDecl(U, AutoType), VarDecl(r, FloatType), VarDecl(OFp, FloatType), VarDecl(AJdR2ea, FloatType), VarDecl(q, FloatType), WhileStmt(BinExpr(==, UnExpr(-, Id(f6)), UnExpr(!, Id(XhH5))), ReturnStmt())]))
	VarDecl(v, FloatType)
	VarDecl(j, FloatType)
	VarDecl(O3, FloatType)
	VarDecl(IJ, FloatType)
	VarDecl(TGkhe, FloatType)
	FuncDecl(m, FloatType, [], A5, BlockStmt([VarDecl(ncO, AutoType), VarDecl(jX, AutoType), VarDecl(i9, AutoType)]))
	VarDecl(f3, ArrayType([8, 0, 82], IntegerType))
	VarDecl(W, ArrayType([8, 0, 82], IntegerType))
	VarDecl(P, ArrayType([8, 0, 82], IntegerType))
	FuncDecl(c, VoidType, [], S, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = """ONmL : function void ( ) { }    """
		expect = """Program([
	FuncDecl(ONmL, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = """WE : function array [ 0 ] of boolean    ( RT : integer     ) { while ( vUL7KqI9   / YWp     :: eC   || bC    == - _      ) Gq ( )  ;     return ;   }    qfX  : float   ;   gsv , oF , q1C , Df , Vf , q  : auto  = ! ! _1Ui     && - ! J      <= ! oP7   && aAM     * A ( )       , { }     && - e   / T      <= ! N    && Zy   - A     - ! G    + 0       :: n49   / W    - - t6     - - l    + w   - z_      > - W   / yz    + Em       , m99   / K    || c   && b     || j      , - - t    + m_a   / gRA        , ! ! ! k      > ! c   || D    || ! Q        , N   + q    && D   * a_     - C ( )     != ! ! O   + z         ;   """
		expect = """Program([
	FuncDecl(WE, ArrayType([0], BooleanType), [Param(RT, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(/, Id(vUL7KqI9), Id(YWp)), BinExpr(==, BinExpr(||, Id(eC), Id(bC)), UnExpr(-, Id(_)))), CallStmt(Gq, )), ReturnStmt()]))
	VarDecl(qfX, FloatType)
	VarDecl(gsv, AutoType, BinExpr(<=, BinExpr(&&, UnExpr(!, UnExpr(!, Id(_1Ui))), UnExpr(-, UnExpr(!, Id(J)))), BinExpr(&&, UnExpr(!, Id(oP7)), BinExpr(*, Id(aAM), FuncCall(A, [])))))
	VarDecl(oF, AutoType, BinExpr(::, BinExpr(<=, BinExpr(&&, ArrayLit([]), BinExpr(/, UnExpr(-, Id(e)), Id(T))), BinExpr(&&, UnExpr(!, Id(N)), BinExpr(+, BinExpr(-, BinExpr(-, Id(Zy), Id(A)), UnExpr(!, Id(G))), IntegerLit(0)))), BinExpr(>, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(/, Id(n49), Id(W)), UnExpr(-, Id(t6))), UnExpr(-, Id(l))), Id(w)), Id(z_)), BinExpr(+, BinExpr(/, UnExpr(-, Id(W)), Id(yz)), Id(Em)))))
	VarDecl(q1C, AutoType, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(/, Id(m99), Id(K)), Id(c)), Id(b)), Id(j)))
	VarDecl(Df, AutoType, BinExpr(+, UnExpr(-, UnExpr(-, Id(t))), BinExpr(/, Id(m_a), Id(gRA))))
	VarDecl(Vf, AutoType, BinExpr(>, UnExpr(!, UnExpr(!, UnExpr(!, Id(k)))), BinExpr(||, BinExpr(||, UnExpr(!, Id(c)), Id(D)), UnExpr(!, Id(Q)))))
	VarDecl(q, AutoType, BinExpr(!=, BinExpr(&&, BinExpr(+, Id(N), Id(q)), BinExpr(-, BinExpr(*, Id(D), Id(a_)), FuncCall(C, []))), BinExpr(+, UnExpr(!, UnExpr(!, Id(O))), Id(z))))
])"""
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = """y , p  : boolean   ;   R , iiJ , u8myb5Yhd3 , M , a  : boolean   ;   L  : array [ 5 , 6 , 0 ] of boolean    = ! C    && G   - QPY     + ! ! Y       :: - Yk    <= ! YPmKKu5qJ   + G     / true        ;   e : function array [ 6_7_5 ] of integer    ( ) { P2  : string   ;  break ;   }    """
		expect = """Program([
	VarDecl(y, BooleanType)
	VarDecl(p, BooleanType)
	VarDecl(R, BooleanType)
	VarDecl(iiJ, BooleanType)
	VarDecl(u8myb5Yhd3, BooleanType)
	VarDecl(M, BooleanType)
	VarDecl(a, BooleanType)
	VarDecl(L, ArrayType([5, 6, 0], BooleanType), BinExpr(::, BinExpr(&&, UnExpr(!, Id(C)), BinExpr(+, BinExpr(-, Id(G), Id(QPY)), UnExpr(!, UnExpr(!, Id(Y))))), BinExpr(<=, UnExpr(-, Id(Yk)), BinExpr(+, UnExpr(!, Id(YPmKKu5qJ)), BinExpr(/, Id(G), BooleanLit(True))))))
	FuncDecl(e, ArrayType([675], IntegerType), [], None, BlockStmt([VarDecl(P2, StringType), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = """mYto : function void ( inherit skAk : auto    ) { }    YIP : function void ( ) inherit mpwa7 { }    """
		expect = """Program([
	FuncDecl(mYto, VoidType, [InheritParam(skAk, AutoType)], None, BlockStmt([]))
	FuncDecl(YIP, VoidType, [], mpwa7, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = """a , Pi3 , N  : auto  ;   """
		expect = """Program([
	VarDecl(a, AutoType)
	VarDecl(Pi3, AutoType)
	VarDecl(N, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = """XX : function void ( ) { do { }  while ( E   + T    != eo   || H      ) ;   }    Y : function void ( inherit uo1c : array [ 0 ] of float      ) { Au , oPOmp  : array [ 0 , 64 ] of boolean    = Ko   * Q    >= ! W      , G      ;  }    """
		expect = """Program([
	FuncDecl(XX, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, BinExpr(+, Id(E), Id(T)), BinExpr(||, Id(eo), Id(H))), BlockStmt([]))]))
	FuncDecl(Y, VoidType, [InheritParam(uo1c, ArrayType([0], FloatType))], None, BlockStmt([VarDecl(Au, ArrayType([0, 64], BooleanType), BinExpr(>=, BinExpr(*, Id(Ko), Id(Q)), UnExpr(!, Id(W)))), VarDecl(oPOmp, ArrayType([0, 64], BooleanType), Id(G))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = """Hv  : array [ 8381 ] of float    = _ ( )    > z ( )     :: - k ( )        ;   D  : boolean   ;   IvlY , A  : array [ 0 ] of float    ;   bPyO : function float   ( sc : array [ 0 , 883693_011_44 , 8 , 66 ] of boolean      ) inherit wU6 { f6  : float   ;  }    """
		expect = """Program([
	VarDecl(Hv, ArrayType([8381], FloatType), BinExpr(::, BinExpr(>, FuncCall(_, []), FuncCall(z, [])), UnExpr(-, FuncCall(k, []))))
	VarDecl(D, BooleanType)
	VarDecl(IvlY, ArrayType([0], FloatType))
	VarDecl(A, ArrayType([0], FloatType))
	FuncDecl(bPyO, FloatType, [Param(sc, ArrayType([0, 88369301144, 8, 66], BooleanType))], wU6, BlockStmt([VarDecl(f6, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = """nE : function void ( mnho0WR9 : auto    ) inherit rnuQ { }    Ak  : integer   = ! - F     || - i    % _TEP   - J      >= S      ;   SBrwW , p , k , Uwka , FU  : string   = ! - UL    * q3ujDP   + mK0      <= - - vbvB    + - sxg        , ""    || BOnQ   && _     || - x1    - 8       :: ! ! ! k1        , - ! Sgk    || ikn5 ( )      >= - - 0       :: yx   <= ! vA    - - w     / 1    * LQ   || ZA        , - ! - v      < - - d9     % LiS     :: - SB3f    * g   % fUh5     || y   - BJD    && ! w      < l   && H    + s   + F     || ! k6s   - x        , - K   - Z     * M3R ( )     > ! ! - G         ;   """
		expect = """Program([
	FuncDecl(nE, VoidType, [Param(mnho0WR9, AutoType)], rnuQ, BlockStmt([]))
	VarDecl(Ak, IntegerType, BinExpr(>=, BinExpr(||, UnExpr(!, UnExpr(-, Id(F))), BinExpr(-, BinExpr(%, UnExpr(-, Id(i)), Id(_TEP)), Id(J))), Id(S)))
	VarDecl(SBrwW, StringType, BinExpr(<=, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, Id(UL))), Id(q3ujDP)), Id(mK0)), BinExpr(+, UnExpr(-, UnExpr(-, Id(vbvB))), UnExpr(-, Id(sxg)))))
	VarDecl(p, StringType, BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(||, StringLit(), Id(BOnQ)), Id(_)), BinExpr(-, UnExpr(-, Id(x1)), IntegerLit(8))), UnExpr(!, UnExpr(!, UnExpr(!, Id(k1))))))
	VarDecl(k, StringType, BinExpr(::, BinExpr(>=, BinExpr(||, UnExpr(-, UnExpr(!, Id(Sgk))), FuncCall(ikn5, [])), UnExpr(-, UnExpr(-, IntegerLit(0)))), BinExpr(<=, Id(yx), BinExpr(||, BinExpr(-, UnExpr(!, Id(vA)), BinExpr(*, BinExpr(/, UnExpr(-, Id(w)), IntegerLit(1)), Id(LQ))), Id(ZA)))))
	VarDecl(Uwka, StringType, BinExpr(::, BinExpr(<, UnExpr(-, UnExpr(!, UnExpr(-, Id(v)))), BinExpr(%, UnExpr(-, UnExpr(-, Id(d9))), Id(LiS))), BinExpr(<, BinExpr(&&, BinExpr(||, BinExpr(%, BinExpr(*, UnExpr(-, Id(SB3f)), Id(g)), Id(fUh5)), BinExpr(-, Id(y), Id(BJD))), UnExpr(!, Id(w))), BinExpr(||, BinExpr(&&, Id(l), BinExpr(+, BinExpr(+, Id(H), Id(s)), Id(F))), BinExpr(-, UnExpr(!, Id(k6s)), Id(x))))))
	VarDecl(FU, StringType, BinExpr(>, BinExpr(-, UnExpr(-, Id(K)), BinExpr(*, Id(Z), FuncCall(M3R, []))), UnExpr(!, UnExpr(!, UnExpr(-, Id(G))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = """Oqt : function array [ 0 , 0 ] of float    ( out F : boolean    , inherit q : auto   , inherit G : array [ 1 , 0 , 0 ] of float      ) inherit q { dx  : float   = - i    <= - oF_       ;  Wz , g  : array [ 0 ] of boolean    = I ( )    == 8     :: ! i      , - D     :: s   * E       ;  }    X , lzB , T , Nb , E , jW , Updo  : array [ 1 ] of float    ;   """
		expect = """Program([
	FuncDecl(Oqt, ArrayType([0, 0], FloatType), [OutParam(F, BooleanType), InheritParam(q, AutoType), InheritParam(G, ArrayType([1, 0, 0], FloatType))], q, BlockStmt([VarDecl(dx, FloatType, BinExpr(<=, UnExpr(-, Id(i)), UnExpr(-, Id(oF_)))), VarDecl(Wz, ArrayType([0], BooleanType), BinExpr(::, BinExpr(==, FuncCall(I, []), IntegerLit(8)), UnExpr(!, Id(i)))), VarDecl(g, ArrayType([0], BooleanType), BinExpr(::, UnExpr(-, Id(D)), BinExpr(*, Id(s), Id(E))))]))
	VarDecl(X, ArrayType([1], FloatType))
	VarDecl(lzB, ArrayType([1], FloatType))
	VarDecl(T, ArrayType([1], FloatType))
	VarDecl(Nb, ArrayType([1], FloatType))
	VarDecl(E, ArrayType([1], FloatType))
	VarDecl(jW, ArrayType([1], FloatType))
	VarDecl(Updo, ArrayType([1], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = """DY , E , Ej , wv  : string   ;   """
		expect = """Program([
	VarDecl(DY, StringType)
	VarDecl(E, StringType)
	VarDecl(Ej, StringType)
	VarDecl(wv, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = """ETLZsS , O , v , WTXBSO , xT  : array [ 6 ] of boolean    ;   """
		expect = """Program([
	VarDecl(ETLZsS, ArrayType([6], BooleanType))
	VarDecl(O, ArrayType([6], BooleanType))
	VarDecl(v, ArrayType([6], BooleanType))
	VarDecl(WTXBSO, ArrayType([6], BooleanType))
	VarDecl(xT, ArrayType([6], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = """I , t  : integer   = - Va4w5K8 ( )       , - ! W     / p   + Wny    || ! sF4M         ;   iN : function boolean   ( ) inherit eT_JY0lTgrd7fu { { }   return - X2      ;   }    """
		expect = """Program([
	VarDecl(I, IntegerType, UnExpr(-, FuncCall(Va4w5K8, [])))
	VarDecl(t, IntegerType, BinExpr(||, BinExpr(+, BinExpr(/, UnExpr(-, UnExpr(!, Id(W))), Id(p)), Id(Wny)), UnExpr(!, Id(sF4M))))
	FuncDecl(iN, BooleanType, [], eT_JY0lTgrd7fu, BlockStmt([BlockStmt([]), ReturnStmt(UnExpr(-, Id(X2)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = """O  : array [ 0 , 0 , 0 , 9 ] of string    = - KIlN   && j    && LAD   && d      < ""    - - ! Q       :: - Ae    + uWO   + k    - ! VSG      == i      ;   """
		expect = """Program([
	VarDecl(O, ArrayType([0, 0, 0, 9], StringType), BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(KIlN)), Id(j)), Id(LAD)), Id(d)), BinExpr(-, StringLit(), UnExpr(-, UnExpr(!, Id(Q))))), BinExpr(==, BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(-, Id(Ae)), Id(uWO)), Id(k)), UnExpr(!, Id(VSG))), Id(i))))
])"""
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = """Uh : function array [ 34 , 97_39_10 ] of integer    ( ) { }    nU : function void ( ) inherit Gcp { }    m5 : function array [ 0 , 10 ] of boolean    ( ) { Pi ( )  ;   while ( - b6l9a     :: UW ( )    > X   - yvYV      ) return ;     }    o : function string   ( ) { }    """
		expect = """Program([
	FuncDecl(Uh, ArrayType([34, 973910], IntegerType), [], None, BlockStmt([]))
	FuncDecl(nU, VoidType, [], Gcp, BlockStmt([]))
	FuncDecl(m5, ArrayType([0, 10], BooleanType), [], None, BlockStmt([CallStmt(Pi, ), WhileStmt(BinExpr(::, UnExpr(-, Id(b6l9a)), BinExpr(>, FuncCall(UW, []), BinExpr(-, Id(X), Id(yvYV)))), ReturnStmt())]))
	FuncDecl(o, StringType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = """X , F  : auto  ;   """
		expect = """Program([
	VarDecl(X, AutoType)
	VarDecl(F, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = """k  : auto  = ! - C   || TH      == v    :: s   == K9      ;   """
		expect = """Program([
	VarDecl(k, AutoType, BinExpr(::, BinExpr(==, BinExpr(||, UnExpr(!, UnExpr(-, Id(C))), Id(TH)), Id(v)), BinExpr(==, Id(s), Id(K9))))
])"""
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = """O  : auto  ;   Z , k  : auto  ;   """
		expect = """Program([
	VarDecl(O, AutoType)
	VarDecl(Z, AutoType)
	VarDecl(k, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = """jSVn07 : function void ( ) inherit mbR { while ( ! kgdEny      ) continue ;     veGK , M  : boolean   = p3O   * Bm    > - F     :: ""      , Ej   * Vk       ;  }    D : function integer   ( ) { }    quwZQu : function void ( ) { }    RW , fQd , ABbA  : boolean   = ! N   / XU8     % q ( )     > ! mV ( )    || ST   % t       :: - ! E    && d     < - ! - N4gb        , ""    >= gnsU ( )    * i   && C     + - qR   % Ci       :: g   + ""     < ! s ( )    * ! y        , - "\\b\\\'"        ;   """
		expect = """Program([
	FuncDecl(jSVn07, VoidType, [], mbR, BlockStmt([WhileStmt(UnExpr(!, Id(kgdEny)), ContinueStmt()), VarDecl(veGK, BooleanType, BinExpr(::, BinExpr(>, BinExpr(*, Id(p3O), Id(Bm)), UnExpr(-, Id(F))), StringLit())), VarDecl(M, BooleanType, BinExpr(*, Id(Ej), Id(Vk)))]))
	FuncDecl(D, IntegerType, [], None, BlockStmt([]))
	FuncDecl(quwZQu, VoidType, [], None, BlockStmt([]))
	VarDecl(RW, BooleanType, BinExpr(::, BinExpr(>, BinExpr(%, BinExpr(/, UnExpr(!, Id(N)), Id(XU8)), FuncCall(q, [])), BinExpr(||, UnExpr(!, FuncCall(mV, [])), BinExpr(%, Id(ST), Id(t)))), BinExpr(<, BinExpr(&&, UnExpr(-, UnExpr(!, Id(E))), Id(d)), UnExpr(-, UnExpr(!, UnExpr(-, Id(N4gb)))))))
	VarDecl(fQd, BooleanType, BinExpr(::, BinExpr(>=, StringLit(), BinExpr(&&, BinExpr(*, FuncCall(gnsU, []), Id(i)), BinExpr(+, Id(C), BinExpr(%, UnExpr(-, Id(qR)), Id(Ci))))), BinExpr(<, BinExpr(+, Id(g), StringLit()), BinExpr(*, UnExpr(!, FuncCall(s, [])), UnExpr(!, Id(y))))))
	VarDecl(ABbA, BooleanType, UnExpr(-, StringLit(\\b\\')))
])"""
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = """l : function void ( ) inherit b_ { iRPJYJ , Ug , ZX , FtmZ  : array [ 0 ] of float    ;  reFbqv  : auto  ;  }    """
		expect = """Program([
	FuncDecl(l, VoidType, [], b_, BlockStmt([VarDecl(iRPJYJ, ArrayType([0], FloatType)), VarDecl(Ug, ArrayType([0], FloatType)), VarDecl(ZX, ArrayType([0], FloatType)), VarDecl(FtmZ, ArrayType([0], FloatType)), VarDecl(reFbqv, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = """s0nZ : function boolean   ( ) inherit d { Zm , uFEy  : auto  = ""    > s0   && y      , K   && N7R     :: v8   || M       ;  }    YsG  : string   = ! n    || WNn   / UQ     || - ! L       :: 0e6       ;   Y  : array [ 72 , 0 ] of integer    = - - ! JG         ;   """
		expect = """Program([
	FuncDecl(s0nZ, BooleanType, [], d, BlockStmt([VarDecl(Zm, AutoType, BinExpr(>, StringLit(), BinExpr(&&, Id(s0), Id(y)))), VarDecl(uFEy, AutoType, BinExpr(::, BinExpr(&&, Id(K), Id(N7R)), BinExpr(||, Id(v8), Id(M))))]))
	VarDecl(YsG, StringType, BinExpr(::, BinExpr(||, BinExpr(||, UnExpr(!, Id(n)), BinExpr(/, Id(WNn), Id(UQ))), UnExpr(-, UnExpr(!, Id(L)))), FloatLit(0.0)))
	VarDecl(Y, ArrayType([72, 0], IntegerType), UnExpr(-, UnExpr(-, UnExpr(!, Id(JG)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = """SQmS6 : function void ( inherit out KE : boolean     ) inherit OB { do { n , p  : auto  ;  }  while ( _3   / SM     :: ! J    != Q   - XESDnP      ) ;   Aq  = T   % vCc    >= - Q     :: H     ;   t , U  : array [ 0 ] of float    = ! OL    <= 5      , v   - P    > y    :: FR   * ZH1       ;  }    ur7T_ , _ , rF , S  : auto  ;   YB3 : function void ( r : boolean     ) { }    """
		expect = """Program([
	FuncDecl(SQmS6, VoidType, [InheritOutParam(KE, BooleanType)], OB, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(/, Id(_3), Id(SM)), BinExpr(!=, UnExpr(!, Id(J)), BinExpr(-, Id(Q), Id(XESDnP)))), BlockStmt([VarDecl(n, AutoType), VarDecl(p, AutoType)])), AssignStmt(Id(Aq), BinExpr(::, BinExpr(>=, BinExpr(%, Id(T), Id(vCc)), UnExpr(-, Id(Q))), Id(H))), VarDecl(t, ArrayType([0], FloatType), BinExpr(<=, UnExpr(!, Id(OL)), IntegerLit(5))), VarDecl(U, ArrayType([0], FloatType), BinExpr(::, BinExpr(>, BinExpr(-, Id(v), Id(P)), Id(y)), BinExpr(*, Id(FR), Id(ZH1))))]))
	VarDecl(ur7T_, AutoType)
	VarDecl(_, AutoType)
	VarDecl(rF, AutoType)
	VarDecl(S, AutoType)
	FuncDecl(YB3, VoidType, [Param(r, BooleanType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = """YQRT : function boolean   ( ) inherit WtTB { while ( BGG   && u     :: 0    == - t      ) J ( )  ;     eC  = R9   + apH      ;   while ( vLDg   * n40    >= X   % e     :: c   * RI    == O6Nh   / r      ) { pE , Hu , NC , R , T , q , b  : boolean   ;  B  : float   ;  }     }    Nu , l , j , c , G  : float   ;   """
		expect = """Program([
	FuncDecl(YQRT, BooleanType, [], WtTB, BlockStmt([WhileStmt(BinExpr(::, BinExpr(&&, Id(BGG), Id(u)), BinExpr(==, IntegerLit(0), UnExpr(-, Id(t)))), CallStmt(J, )), AssignStmt(Id(eC), BinExpr(+, Id(R9), Id(apH))), WhileStmt(BinExpr(::, BinExpr(>=, BinExpr(*, Id(vLDg), Id(n40)), BinExpr(%, Id(X), Id(e))), BinExpr(==, BinExpr(*, Id(c), Id(RI)), BinExpr(/, Id(O6Nh), Id(r)))), BlockStmt([VarDecl(pE, BooleanType), VarDecl(Hu, BooleanType), VarDecl(NC, BooleanType), VarDecl(R, BooleanType), VarDecl(T, BooleanType), VarDecl(q, BooleanType), VarDecl(b, BooleanType), VarDecl(B, FloatType)]))]))
	VarDecl(Nu, FloatType)
	VarDecl(l, FloatType)
	VarDecl(j, FloatType)
	VarDecl(c, FloatType)
	VarDecl(G, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = """T  : string   ;   """
		expect = """Program([
	VarDecl(T, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = """rn , E  : auto  ;   s : function integer   ( ) { ZJ , Da  : boolean   = LNe   || U    > - E      , H ( )     :: - iTPG2       ;  }    c : function auto  ( inherit out HH : auto    ) { G3G ( )  ;   }    """
		expect = """Program([
	VarDecl(rn, AutoType)
	VarDecl(E, AutoType)
	FuncDecl(s, IntegerType, [], None, BlockStmt([VarDecl(ZJ, BooleanType, BinExpr(>, BinExpr(||, Id(LNe), Id(U)), UnExpr(-, Id(E)))), VarDecl(Da, BooleanType, BinExpr(::, FuncCall(H, []), UnExpr(-, Id(iTPG2))))]))
	FuncDecl(c, AutoType, [InheritOutParam(HH, AutoType)], None, BlockStmt([CallStmt(G3G, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = """H , x  : array [ 0 , 5_38_2115 ] of string    = uC   && GA4yAe    || f   - W     - ! z   / ez        , { }        ;   """
		expect = """Program([
	VarDecl(H, ArrayType([0, 5382115], StringType), BinExpr(||, BinExpr(&&, Id(uC), Id(GA4yAe)), BinExpr(-, BinExpr(-, Id(f), Id(W)), BinExpr(/, UnExpr(!, Id(z)), Id(ez)))))
	VarDecl(x, ArrayType([0, 5382115], StringType), ArrayLit([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = """D : function string   ( out Stpc : boolean    , ZR : string    , YdG : auto   , inherit out _wP : auto    ) inherit M { }    hQ  : array [ 8 , 7_5_0 ] of string    = vGt ( )    == c   + TY    % Mt ( )     - ! V5a    - K   && mt         ;   BE : function array [ 0 , 1_2563_918_0 , 96 ] of boolean    ( ) { }    nmoZ : function auto  ( inherit Bg : string     ) inherit CZJ5M { return o1   && MT    != sCOYdD   + MHBY     :: Sqw9   - n    < l7   % x      ;   }    f : function auto  ( ) { while ( W   + H     :: - KV    != v   / T      ) break ;     C  : float   ;  }    """
		expect = """Program([
	FuncDecl(D, StringType, [OutParam(Stpc, BooleanType), Param(ZR, StringType), Param(YdG, AutoType), InheritOutParam(_wP, AutoType)], M, BlockStmt([]))
	VarDecl(hQ, ArrayType([8, 750], StringType), BinExpr(==, FuncCall(vGt, []), BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(c), BinExpr(%, Id(TY), FuncCall(Mt, []))), UnExpr(!, Id(V5a))), Id(K)), Id(mt))))
	FuncDecl(BE, ArrayType([0, 125639180, 96], BooleanType), [], None, BlockStmt([]))
	FuncDecl(nmoZ, AutoType, [InheritParam(Bg, StringType)], CZJ5M, BlockStmt([ReturnStmt(BinExpr(::, BinExpr(!=, BinExpr(&&, Id(o1), Id(MT)), BinExpr(+, Id(sCOYdD), Id(MHBY))), BinExpr(<, BinExpr(-, Id(Sqw9), Id(n)), BinExpr(%, Id(l7), Id(x)))))]))
	FuncDecl(f, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(+, Id(W), Id(H)), BinExpr(!=, UnExpr(-, Id(KV)), BinExpr(/, Id(v), Id(T)))), BreakStmt()), VarDecl(C, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = """col : function void ( inherit out Teub_ : array [ 4 ] of string      ) inherit B7C { N , q  : array [ 0 , 895_53_4_044215_9345 , 6986 , 47_452_5 ] of string    = i   + DH     :: ! d    < B   / Fo      , lY   * iEOXlx     :: zq ( )       ;  xcO , qz , hA , t  : array [ 0 , 3_00_17 , 0 ] of integer    ;  K , G , v , k , B  : integer   = bO   * kDq      , - zV    <= ! i      , - u      , JI   * yA     :: - P6    > Gn3I   && GcDyUH      , - x    > er      ;  s  : integer   ;  sqZ3qCS  : integer   = ! brMa4     :: J ( )    < Km   - j       ;  }    A , h , w  : boolean   ;   """
		expect = """Program([
	FuncDecl(col, VoidType, [InheritOutParam(Teub_, ArrayType([4], StringType))], B7C, BlockStmt([VarDecl(N, ArrayType([0, 8955340442159345, 6986, 474525], StringType), BinExpr(::, BinExpr(+, Id(i), Id(DH)), BinExpr(<, UnExpr(!, Id(d)), BinExpr(/, Id(B), Id(Fo))))), VarDecl(q, ArrayType([0, 8955340442159345, 6986, 474525], StringType), BinExpr(::, BinExpr(*, Id(lY), Id(iEOXlx)), FuncCall(zq, []))), VarDecl(xcO, ArrayType([0, 30017, 0], IntegerType)), VarDecl(qz, ArrayType([0, 30017, 0], IntegerType)), VarDecl(hA, ArrayType([0, 30017, 0], IntegerType)), VarDecl(t, ArrayType([0, 30017, 0], IntegerType)), VarDecl(K, IntegerType, BinExpr(*, Id(bO), Id(kDq))), VarDecl(G, IntegerType, BinExpr(<=, UnExpr(-, Id(zV)), UnExpr(!, Id(i)))), VarDecl(v, IntegerType, UnExpr(-, Id(u))), VarDecl(k, IntegerType, BinExpr(::, BinExpr(*, Id(JI), Id(yA)), BinExpr(>, UnExpr(-, Id(P6)), BinExpr(&&, Id(Gn3I), Id(GcDyUH))))), VarDecl(B, IntegerType, BinExpr(>, UnExpr(-, Id(x)), Id(er))), VarDecl(s, IntegerType), VarDecl(sqZ3qCS, IntegerType, BinExpr(::, UnExpr(!, Id(brMa4)), BinExpr(<, FuncCall(J, []), BinExpr(-, Id(Km), Id(j)))))]))
	VarDecl(A, BooleanType)
	VarDecl(h, BooleanType)
	VarDecl(w, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = """i  : auto  = ! g   - N7G0SI1    - EJ      :: ! ! ! z         ;   w , iBGe  : array [ 0 ] of string    = CXdrpO   && hQ    * - VvCnK     || H7Z   && B    % tUre   || pj       :: uQmg   >= b   * uvA    + 2     / ! F    && R   / T8d        , 0    && G_   % z     % B   || dW    && Aw   + r       :: ! w   / G7    || K   / qD         ;   """
		expect = """Program([
	VarDecl(i, AutoType, BinExpr(::, BinExpr(-, BinExpr(-, UnExpr(!, Id(g)), Id(N7G0SI1)), Id(EJ)), UnExpr(!, UnExpr(!, UnExpr(!, Id(z))))))
	VarDecl(w, ArrayType([0], StringType), BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(CXdrpO), BinExpr(*, Id(hQ), UnExpr(-, Id(VvCnK)))), Id(H7Z)), BinExpr(%, Id(B), Id(tUre))), Id(pj)), BinExpr(>=, Id(uQmg), BinExpr(&&, BinExpr(+, BinExpr(*, Id(b), Id(uvA)), BinExpr(/, IntegerLit(2), UnExpr(!, Id(F)))), BinExpr(/, Id(R), Id(T8d))))))
	VarDecl(iBGe, ArrayType([0], StringType), BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(&&, IntegerLit(0), BinExpr(%, BinExpr(%, Id(G_), Id(z)), Id(B))), Id(dW)), BinExpr(+, Id(Aw), Id(r))), BinExpr(||, BinExpr(/, UnExpr(!, Id(w)), Id(G7)), BinExpr(/, Id(K), Id(qD)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = """TM : function void ( out rF : integer     ) { k  : float   = W   && VG     :: - L       ;  }    """
		expect = """Program([
	FuncDecl(TM, VoidType, [OutParam(rF, IntegerType)], None, BlockStmt([VarDecl(k, FloatType, BinExpr(::, BinExpr(&&, Id(W), Id(VG)), UnExpr(-, Id(L))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = """a : function auto  ( io : auto    ) { p  = G ( )    < B   + kB     :: mi     ;   m  : array [ 0 ] of boolean    ;  QK , M  : array [ 0 ] of string    ;  while ( X   * m    <= - Z     :: fH   * V      ) break ;     s , D  : auto  = z53   && w      , jl5r ( )    == Z      ;  M , zaK73  : float   ;  if ( - O      ) break ;   else return ;     }    p : function void ( out z : array [ 32 ] of string     , inherit out aA : array [ 0 ] of float      ) inherit R { return ! D      ;   }    L : function void ( ) inherit cW { }    """
		expect = """Program([
	FuncDecl(a, AutoType, [Param(io, AutoType)], None, BlockStmt([AssignStmt(Id(p), BinExpr(::, BinExpr(<, FuncCall(G, []), BinExpr(+, Id(B), Id(kB))), Id(mi))), VarDecl(m, ArrayType([0], BooleanType)), VarDecl(QK, ArrayType([0], StringType)), VarDecl(M, ArrayType([0], StringType)), WhileStmt(BinExpr(::, BinExpr(<=, BinExpr(*, Id(X), Id(m)), UnExpr(-, Id(Z))), BinExpr(*, Id(fH), Id(V))), BreakStmt()), VarDecl(s, AutoType, BinExpr(&&, Id(z53), Id(w))), VarDecl(D, AutoType, BinExpr(==, FuncCall(jl5r, []), Id(Z))), VarDecl(M, FloatType), VarDecl(zaK73, FloatType), IfStmt(UnExpr(-, Id(O)), BreakStmt(), ReturnStmt())]))
	FuncDecl(p, VoidType, [OutParam(z, ArrayType([32], StringType)), InheritOutParam(aA, ArrayType([0], FloatType))], R, BlockStmt([ReturnStmt(UnExpr(!, Id(D)))]))
	FuncDecl(L, VoidType, [], cW, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = """i , b2  : array [ 0 ] of float    = - uFqL   + pHtM     + ! vP   && O      == ! ! ""        , - B ( )     % b   / F    && P   * u         ;   R , vHT  : auto  = - z   && K    / bne   + G        , - N    + T    % ! Y   + JZ9s         ;   j : function void ( ) { }    O , Kl  : string   ;   """
		expect = """Program([
	VarDecl(i, ArrayType([0], FloatType), BinExpr(==, BinExpr(&&, BinExpr(+, BinExpr(+, UnExpr(-, Id(uFqL)), Id(pHtM)), UnExpr(!, Id(vP))), Id(O)), UnExpr(!, UnExpr(!, StringLit()))))
	VarDecl(b2, ArrayType([0], FloatType), BinExpr(&&, BinExpr(/, BinExpr(%, UnExpr(-, FuncCall(B, [])), Id(b)), Id(F)), BinExpr(*, Id(P), Id(u))))
	VarDecl(R, AutoType, BinExpr(&&, UnExpr(-, Id(z)), BinExpr(+, BinExpr(/, Id(K), Id(bne)), Id(G))))
	VarDecl(vHT, AutoType, BinExpr(+, BinExpr(+, UnExpr(-, Id(N)), BinExpr(%, Id(T), UnExpr(!, Id(Y)))), Id(JZ9s)))
	FuncDecl(j, VoidType, [], None, BlockStmt([]))
	VarDecl(O, StringType)
	VarDecl(Kl, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = """r : function array [ 8_6_5816_491 , 0 ] of boolean    ( out m : integer     ) { }    m , u2  : string   = sm    :: ! ! ""        , d   - N    + vZs   / i     && Q ( )    / - yPA      == - - ! d       :: ! f   % s8B    && 0      <= z   + n    / - Qloh     - YM   * UL    + L   + d         ;   """
		expect = """Program([
	FuncDecl(r, ArrayType([865816491, 0], BooleanType), [OutParam(m, IntegerType)], None, BlockStmt([]))
	VarDecl(m, StringType, BinExpr(::, Id(sm), UnExpr(!, UnExpr(!, StringLit()))))
	VarDecl(u2, StringType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(+, BinExpr(-, Id(d), Id(N)), BinExpr(/, Id(vZs), Id(i))), BinExpr(/, FuncCall(Q, []), UnExpr(-, Id(yPA)))), UnExpr(-, UnExpr(-, UnExpr(!, Id(d))))), BinExpr(<=, BinExpr(&&, BinExpr(%, UnExpr(!, Id(f)), Id(s8B)), IntegerLit(0)), BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, Id(z), BinExpr(/, Id(n), UnExpr(-, Id(Qloh)))), BinExpr(*, Id(YM), Id(UL))), Id(L)), Id(d)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = """S : function void ( ) { do { }  while ( gKi   && Rt     :: GC2   + b      ) ;   }    vT : function array [ 0 , 80_7_8 , 0 ] of string    ( out ig : auto   , v : boolean    , t_T : auto    ) inherit o0e5qpJ { }    """
		expect = """Program([
	FuncDecl(S, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(&&, Id(gKi), Id(Rt)), BinExpr(+, Id(GC2), Id(b))), BlockStmt([]))]))
	FuncDecl(vT, ArrayType([0, 8078, 0], StringType), [OutParam(ig, AutoType), Param(v, BooleanType), Param(t_T, AutoType)], o0e5qpJ, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = """mkw : function void ( inherit out i : auto    ) { return ;   }    """
		expect = """Program([
	FuncDecl(mkw, VoidType, [InheritOutParam(i, AutoType)], None, BlockStmt([ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = """m8Ah : function void ( out S : auto    ) inherit Am { }    Mc : function array [ 0 ] of float    ( ) inherit A { }    """
		expect = """Program([
	FuncDecl(m8Ah, VoidType, [OutParam(S, AutoType)], Am, BlockStmt([]))
	FuncDecl(Mc, ArrayType([0], FloatType), [], A, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = """V5l : function void ( out JF : boolean     ) { We9  : array [ 71 ] of float    ;  }    """
		expect = """Program([
	FuncDecl(V5l, VoidType, [OutParam(JF, BooleanType)], None, BlockStmt([VarDecl(We9, ArrayType([71], FloatType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = """Y  : array [ 6_89_5 , 0 ] of string    = xc   % W    || - kOw     % H    >= h ( )    / - D    + P        ;   """
		expect = """Program([
	VarDecl(Y, ArrayType([6895, 0], StringType), BinExpr(>=, BinExpr(||, BinExpr(%, Id(xc), Id(W)), BinExpr(%, UnExpr(-, Id(kOw)), Id(H))), BinExpr(+, BinExpr(/, FuncCall(h, []), UnExpr(-, Id(D))), Id(P))))
])"""
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = """SXZib : function void ( out zbt : string    , inherit out Qsy : array [ 0 , 7_0496_610070 ] of float      ) { }    """
		expect = """Program([
	FuncDecl(SXZib, VoidType, [OutParam(zbt, StringType), InheritOutParam(Qsy, ArrayType([0, 70496610070], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = """IoS : function void ( ) inherit p { }    """
		expect = """Program([
	FuncDecl(IoS, VoidType, [], p, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = """H : function boolean   ( ) inherit tg { P , G , b  : auto  ;  }    j , GB , SG1h  : integer   ;   gbgVWUQ : function array [ 0 , 65_28_22_88290_3_07 , 3_23_9 ] of boolean    ( ) inherit DxV2 { WKXVN  : array [ 6_4_000_0 , 56 , 8_9_9_33_8_1_3_0 , 4 ] of string    ;  }    """
		expect = """Program([
	FuncDecl(H, BooleanType, [], tg, BlockStmt([VarDecl(P, AutoType), VarDecl(G, AutoType), VarDecl(b, AutoType)]))
	VarDecl(j, IntegerType)
	VarDecl(GB, IntegerType)
	VarDecl(SG1h, IntegerType)
	FuncDecl(gbgVWUQ, ArrayType([0, 65282288290307, 3239], BooleanType), [], DxV2, BlockStmt([VarDecl(WKXVN, ArrayType([640000, 56, 899338130, 4], StringType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = """iq : function void ( ) { }    w : function void ( ) inherit l { }    """
		expect = """Program([
	FuncDecl(iq, VoidType, [], None, BlockStmt([]))
	FuncDecl(w, VoidType, [], l, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = """xt : function integer   ( Sfn : string     ) { }    """
		expect = """Program([
	FuncDecl(xt, IntegerType, [Param(Sfn, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = """yHEnX : function void ( ) inherit r { { rZ  : array [ 634 , 0 , 0 , 0 , 0 ] of boolean    ;  }   }    """
		expect = """Program([
	FuncDecl(yHEnX, VoidType, [], r, BlockStmt([BlockStmt([VarDecl(rZ, ArrayType([634, 0, 0, 0, 0], BooleanType))])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = """q : function void ( inherit WS : integer    , inherit YZ : auto    ) { Z  : array [ 314 , 0 , 1_9787019 , 0 ] of integer    = H6t   || ib     :: - v68       ;  }    """
		expect = """Program([
	FuncDecl(q, VoidType, [InheritParam(WS, IntegerType), InheritParam(YZ, AutoType)], None, BlockStmt([VarDecl(Z, ArrayType([314, 0, 19787019, 0], IntegerType), BinExpr(::, BinExpr(||, Id(H6t), Id(ib)), UnExpr(-, Id(v68))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = """p  : float   ;   """
		expect = """Program([
	VarDecl(p, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = """h , O , v  : array [ 0 , 6 , 0 ] of boolean    ;   i , O  : array [ 3_74_85_81 , 742 ] of string    ;   """
		expect = """Program([
	VarDecl(h, ArrayType([0, 6, 0], BooleanType))
	VarDecl(O, ArrayType([0, 6, 0], BooleanType))
	VarDecl(v, ArrayType([0, 6, 0], BooleanType))
	VarDecl(i, ArrayType([3748581, 742], StringType))
	VarDecl(O, ArrayType([3748581, 742], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = """W : function void ( ) { }    r  : auto  = Em   < ! rm     :: - - c     > - U   + f     - e   && YK    / 0         ;   """
		expect = """Program([
	FuncDecl(W, VoidType, [], None, BlockStmt([]))
	VarDecl(r, AutoType, BinExpr(::, BinExpr(<, Id(Em), UnExpr(!, Id(rm))), BinExpr(>, UnExpr(-, UnExpr(-, Id(c))), BinExpr(&&, BinExpr(-, BinExpr(+, UnExpr(-, Id(U)), Id(f)), Id(e)), BinExpr(/, Id(YK), IntegerLit(0))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = """Wp  : auto  = ! B   + H     || - Ro    + y   && RupZeeD      < ""     :: ""    % ! 0      == I ( )    - ! ""         ;   """
		expect = """Program([
	VarDecl(Wp, AutoType, BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(!, Id(B)), Id(H)), BinExpr(+, UnExpr(-, Id(Ro)), Id(y))), Id(RupZeeD)), StringLit()), BinExpr(==, BinExpr(%, StringLit(), UnExpr(!, IntegerLit(0))), BinExpr(-, FuncCall(I, []), UnExpr(!, StringLit())))))
])"""
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = """nEwd  : array [ 47 , 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(nEwd, ArrayType([47, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = """L3K , Qzv , m , KC  : array [ 0 ] of integer    = - rAF   && hi     / K2   && t    - ! ZeNl3        , ! a   / uR    / tg   - j      != - G   || e     && - O ( )        , VJY   % SeQUA   * nOm     + ! s1J   || E        , 0    % xRP   && H   && z         ;   t : function void ( ) { }    """
		expect = """Program([
	VarDecl(L3K, ArrayType([0], IntegerType), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(rAF)), BinExpr(/, Id(hi), Id(K2))), BinExpr(-, Id(t), UnExpr(!, Id(ZeNl3)))))
	VarDecl(Qzv, ArrayType([0], IntegerType), BinExpr(!=, BinExpr(-, BinExpr(/, BinExpr(/, UnExpr(!, Id(a)), Id(uR)), Id(tg)), Id(j)), BinExpr(&&, BinExpr(||, UnExpr(-, Id(G)), Id(e)), UnExpr(-, FuncCall(O, [])))))
	VarDecl(m, ArrayType([0], IntegerType), BinExpr(||, BinExpr(+, BinExpr(*, BinExpr(%, Id(VJY), Id(SeQUA)), Id(nOm)), UnExpr(!, Id(s1J))), Id(E)))
	VarDecl(KC, ArrayType([0], IntegerType), BinExpr(&&, BinExpr(&&, BinExpr(%, IntegerLit(0), Id(xRP)), Id(H)), Id(z)))
	FuncDecl(t, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = """j : function array [ 59_612_5_7_4 , 0 , 94_72 , 0 ] of float    ( ) { }    gcNRs , muZ  : string   ;   D : function void ( lWh : array [ 94 ] of boolean      ) inherit F { }    N : function void ( ) inherit e { }    """
		expect = """Program([
	FuncDecl(j, ArrayType([59612574, 0, 9472, 0], FloatType), [], None, BlockStmt([]))
	VarDecl(gcNRs, StringType)
	VarDecl(muZ, StringType)
	FuncDecl(D, VoidType, [Param(lWh, ArrayType([94], BooleanType))], F, BlockStmt([]))
	FuncDecl(N, VoidType, [], e, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = """b  : boolean   = c   > ""    && - - Dh       :: - - - QTdpF         ;   eEzT  : auto  ;   """
		expect = """Program([
	VarDecl(b, BooleanType, BinExpr(::, BinExpr(>, Id(c), BinExpr(&&, StringLit(), UnExpr(-, UnExpr(-, Id(Dh))))), UnExpr(-, UnExpr(-, UnExpr(-, Id(QTdpF))))))
	VarDecl(eEzT, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = """v , mY  : float   ;   """
		expect = """Program([
	VarDecl(v, FloatType)
	VarDecl(mY, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = """D : function string   ( out ghCcS : array [ 0 ] of string     , h : array [ 0 ] of boolean      ) inherit WPuM { Q  = ! Cu     :: ! BP      ;   i , EGEu  : auto  = C   % b    != fD   + ktd      , Z   / oB    == s4qY   % GR     :: - T       ;  return ;   }    U , vRT , r_  : auto  ;   """
		expect = """Program([
	FuncDecl(D, StringType, [OutParam(ghCcS, ArrayType([0], StringType)), Param(h, ArrayType([0], BooleanType))], WPuM, BlockStmt([AssignStmt(Id(Q), BinExpr(::, UnExpr(!, Id(Cu)), UnExpr(!, Id(BP)))), VarDecl(i, AutoType, BinExpr(!=, BinExpr(%, Id(C), Id(b)), BinExpr(+, Id(fD), Id(ktd)))), VarDecl(EGEu, AutoType, BinExpr(::, BinExpr(==, BinExpr(/, Id(Z), Id(oB)), BinExpr(%, Id(s4qY), Id(GR))), UnExpr(-, Id(T)))), ReturnStmt()]))
	VarDecl(U, AutoType)
	VarDecl(vRT, AutoType)
	VarDecl(r_, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = """rvKsvh : function void ( inherit sk : float     ) { Ip  : string   = D   && t     :: ""    == pKY   || U       ;  }    """
		expect = """Program([
	FuncDecl(rvKsvh, VoidType, [InheritParam(sk, FloatType)], None, BlockStmt([VarDecl(Ip, StringType, BinExpr(::, BinExpr(&&, Id(D), Id(t)), BinExpr(==, StringLit(), BinExpr(||, Id(pKY), Id(U)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = """O , WB , k , b , khTdd , t0  : float   ;   """
		expect = """Program([
	VarDecl(O, FloatType)
	VarDecl(WB, FloatType)
	VarDecl(k, FloatType)
	VarDecl(b, FloatType)
	VarDecl(khTdd, FloatType)
	VarDecl(t0, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = """ti : function integer   ( out TtTYgr : boolean    , inherit out wyD : float    , out F : array [ 94 , 3 ] of integer     , G : string     ) { }    """
		expect = """Program([
	FuncDecl(ti, IntegerType, [OutParam(TtTYgr, BooleanType), InheritOutParam(wyD, FloatType), OutParam(F, ArrayType([94, 3], IntegerType)), Param(G, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = """M , _L , v  : auto  ;   eR , U , Z9I  : float   ;   """
		expect = """Program([
	VarDecl(M, AutoType)
	VarDecl(_L, AutoType)
	VarDecl(v, AutoType)
	VarDecl(eR, FloatType)
	VarDecl(U, FloatType)
	VarDecl(Z9I, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = """A : function integer   ( inherit out A : auto    ) { }    HPyLP , wLLVxM , b  : auto  = - - RvAqj    - - j5      >= - ! GA8      :: ! Rf   * do1     && ! A    + Dl   - ba        , - UU    && p   && N     && C ( )    % ! Nss       :: - R    && - yuJ     / ! e   || c        , B9w ( )    + K   && o    % j   || y      == ! Yz   % Sn     / ! aK   % x         ;   IXR : function void ( ) { return R   + hwtD    < ! rKF     :: cC   && B      ;   }    """
		expect = """Program([
	FuncDecl(A, IntegerType, [InheritOutParam(A, AutoType)], None, BlockStmt([]))
	VarDecl(HPyLP, AutoType, BinExpr(::, BinExpr(>=, BinExpr(-, UnExpr(-, UnExpr(-, Id(RvAqj))), UnExpr(-, Id(j5))), UnExpr(-, UnExpr(!, Id(GA8)))), BinExpr(&&, BinExpr(*, UnExpr(!, Id(Rf)), Id(do1)), BinExpr(-, BinExpr(+, UnExpr(!, Id(A)), Id(Dl)), Id(ba)))))
	VarDecl(wLLVxM, AutoType, BinExpr(::, BinExpr(&&, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(UU)), Id(p)), Id(N)), BinExpr(%, FuncCall(C, []), UnExpr(!, Id(Nss)))), BinExpr(||, BinExpr(&&, UnExpr(-, Id(R)), BinExpr(/, UnExpr(-, Id(yuJ)), UnExpr(!, Id(e)))), Id(c))))
	VarDecl(b, AutoType, BinExpr(==, BinExpr(||, BinExpr(&&, BinExpr(+, FuncCall(B9w, []), Id(K)), BinExpr(%, Id(o), Id(j))), Id(y)), BinExpr(%, BinExpr(/, BinExpr(%, UnExpr(!, Id(Yz)), Id(Sn)), UnExpr(!, Id(aK))), Id(x))))
	FuncDecl(IXR, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(::, BinExpr(<, BinExpr(+, Id(R), Id(hwtD)), UnExpr(!, Id(rKF))), BinExpr(&&, Id(cC), Id(B))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = """P  : array [ 0 ] of float    = weO   <= ! ! kW     % - x   + wzgIsCJ         ;   m : function void ( inherit out f : auto    ) { xnfln  : array [ 0 ] of boolean    = - A     :: ! h    > a   / d       ;  G , M  : array [ 4_38_00_846 , 1 , 0 , 7 ] of float    ;  }    """
		expect = """Program([
	VarDecl(P, ArrayType([0], FloatType), BinExpr(<=, Id(weO), BinExpr(+, BinExpr(%, UnExpr(!, UnExpr(!, Id(kW))), UnExpr(-, Id(x))), Id(wzgIsCJ))))
	FuncDecl(m, VoidType, [InheritOutParam(f, AutoType)], None, BlockStmt([VarDecl(xnfln, ArrayType([0], BooleanType), BinExpr(::, UnExpr(-, Id(A)), BinExpr(>, UnExpr(!, Id(h)), BinExpr(/, Id(a), Id(d))))), VarDecl(G, ArrayType([43800846, 1, 0, 7], FloatType)), VarDecl(M, ArrayType([43800846, 1, 0, 7], FloatType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 400))
