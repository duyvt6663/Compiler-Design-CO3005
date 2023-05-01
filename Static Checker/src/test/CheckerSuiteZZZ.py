import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8051
    def test_401(self):
        input = """
        foo: function void(a: float)
        {
            a  = 1;
        }

        bar: function void(a: auto, b: integer)
        {
            a = a + b;
        }

        main: function void()
        {
            foo(1);
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8066
    def test_402(self):
        input = """
        main: function void()
        {
            a: auto = 1.0 != 1.0;
        }
        """
        expect = """Type mismatch in expression: BinExpr(!=, FloatLit(1.0), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (1)
    def test_403(self):
        input = """
        main: function void()
        {
            a: integer = 5.4;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8057 (2)
    def test_404(self):
        input = """
        main: function void()
        {
            a: integer;
            a = 5.4;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8083
    def test_405(self):
        input = """
        main: function void()
        {
            return 1;
            end: auto;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7989
    def test_406(self):
        input = """
        foo: function void(out x: integer){}
        main: function void()
        {
            foo(2);
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    # TODO: https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7991
    def test_407(self):
        input = """
                    main: function void() {
                        a: integer = 1 + "float";
                    }
                """
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), StringLit(float))"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8047
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9221
    def test_408(self):
        input = """
        main: function void()
        {
            a: auto = 2 + 3.4;
            b: auto = 1 != true;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (1)
    def test_409(self):
        input = """
        y: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            x = 5;
            x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (2)
    def test_410(self):
        input = """
        //x: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            {
                x = 5;
            }
            x: integer;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988 (3)
    def test_411(self):
        input = """
        // x: auto = foo();
        foo: function integer(){}
        main: function void()
        {
            {
                x: integer;
            }
            x = 5;
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8110
    def test_412(self):
        input = """
        main: function void()
        {
            x = 5;
        }
        x: auto = 1;
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (1)
    def test_413(self):
        input = """
        a: function void (p : array [1] of integer) {}
        foo: function auto(){}
        bar: function auto(){}
        goo: function auto(){}
        gar: function auto(){}
        main: function void()
        {
            a({1});
            b: boolean = foo() == bar();
            c: float = goo() + gar();
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8149 (2)
    def test_414(self):
        input = """
        foo: function auto(){}
        bar: function auto(){}
        goo: function auto(){}
        main: function void()
        {
            a: auto = foo() + bar();
            b: integer = foo(); // ?
            c: auto = -goo();
            d: integer = goo(); // ?
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8610
    def test_415(self):
        input = """
        foo1: function auto(){}
        foo2: function auto(){}
        a: array [2] of integer = { foo1(), foo2() };
        b: integer = foo1();
        c: integer = foo2();
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8106
    def test_416(self):
        input = """
        foo: function void(a: auto) {}
        bar: function void(a: auto) inherit foo {}
        main: function void(){}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7977
    def test_417(self):
        input = """
        foo: function void(a: auto)
        {
            return 1;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""  # Hay k có lỗi do k duyệt body, tại hàm k đc gọi?
        self.assertTrue(TestChecker.test(input, expect, 417))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8098
    def test_418(self):
        input = """
        main: function void()
        {
            // a: auto = {}; -> Not in testcases
            // a: array [0] of integer; -> Not in testcases
            a: array [5] of integer = {1, 2, 3};
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8087
    def test_419(self):
        input = """
        main: function void()
        {
            // a: auto = {}; -> Not in testcases
            // a: array [0] of integer; -> Not in testcases
            a: array [5] of integer = {1, 2, 3};
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8399
    def test_420(self):
        input = """
        main: function void()
        {
            a: auto = 1.5 < 2;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8317
    def test_421(self):
        input = """
        foo: integer = 2;
        foo: function void () {}
        main: function void() {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8170
    def test_422(self):
        input = """
        foo: function auto() { return 10; }
        foo2: function void() { a: string = foo(); }
        main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8642
    def test_423(self):
        input = """
        foo: function integer(inherit x: integer) inherit bar
        {
            super(2);
        }

        bar: function integer(inherit y: integer) inherit foo2
        {
            super("Hi");
        }

        foo2: function integer(inherit z: float){}
        """
        expect = """Type mismatch in expression: StringLit(Hi)"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8646
    def test_424(self):
        input = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer)
        {
            return a + b;
        }
        b: float = foo(1, 2);
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8657
    def test_425(self):
        input = """
        a: integer = 2.3; //1
        b: auto; //2
        foo: function void(a: integer, b: float) {} //3
        bar: function void() inherit foo {} //4
        a: function void() {} //5
        main: function void(){}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.3))"""  # "trong khi duyệt sơ bộ mình không cần phải check Redeclared"
        self.assertTrue(TestChecker.test(input, expect, 425))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8660
    def test_426(self):
        input = """
        x, y: integer = 1, foo(1, 2, 3);
        x, y: string;
        foo: function integer (x: integer, y: integer, x: integer){}
        main: function void(){}
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8679
    def test_427(self):
        input = """
        x: function void() {}
        main: function void() inherit x
        {
            super();
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8703
    def test_428(self):
        input = """
        x: auto = {4,5,6};
        y: auto = x[1,2];
        main: function void() {}
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8839
    def test_429(self):
        input = """
        a: auto = 1;
        main: function void()
        {
            b: auto = a();
        }
        """
        expect = """Undeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8913
    def test_430(self):
        input = """
        a: array [1, 1] of boolean;
        foo: function auto(){}
        main: function void()
        {
            a[foo(), 1+4] = 222;
            b: integer = foo();
            end: auto;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [FuncCall(foo, []), BinExpr(+, IntegerLit(1), IntegerLit(4))]), IntegerLit(222))"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8943
    def test_431(self):
        input = """
        foo: function integer(){}
        a: auto = foo;
        main: function void()
        {
            a[foo(), 1 + 4] = 222;
            b: integer = foo();
        }
        """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8936
    def test_432(self):
        input = """
        foo: function auto(){}
        main: function void()
        {
            foo();
            a: boolean = foo();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8813 (1)
    def test_433(self):
        input = """
        x: function void (a: auto) {}
        main: function void()
        {
            x();
        }
        """
        expect = """Type mismatch in statement: CallStmt(x, )"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8813 (2)
    def test_434(self):
        input = """
        x: function void (a: auto) {}
        main: function void()
        {
            x(1, 2);
        }
        """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9108
    def test_435(self):
        input = """
        super: function integer(){}
        main: function void(){}
        """
        expect = """Redeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9055
    def test_436(self):
        input = """
        foo: function auto () {}
        foo: function auto (a: integer, b: integer ) inherit bar {}
        main: function void() {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9057
    def test_437(self):
        input = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        main: function void () {}
        """
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9107
    def test_438(self):
        input = """
        a: string = 12 :: "str";
        main: function void() {}
        """
        expect = """Type mismatch in expression: BinExpr(::, IntegerLit(12), StringLit(str))"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9036
    def test_439(self):
        input = """
        foo: function integer(a: string){}
        main: function void()
        {
            a: integer = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9113
    def test_440(self):
        input = """
            printFloat: auto = 100;
        """
        expect = """Redeclared Variable: printFloat"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9117
    def test_441(self):
        input = """
        foo: function auto()
        {
            return 1;
            return true;
        }
        main: function void()
        {
            a: boolean = foo();
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9120
    def test_442(self):
        input = """
        main: function void() {}
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer)
        {
            return a + b;
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9122
    def test_443(self):
        input = """
        main: function void() {}
        foo: function auto(a: string, b: string)
        {
            return a::b;
        }
        a: float = foo("hello", "Hi");
        """
        expect = """Type mismatch in statement: Return(???)"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8969 (1)
    def test_444(self):
        input = """
        main: function void() {}
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8969 (2)
    def test_445(self):
        input = """
        bar: function void (inherit a: integer) {}
        foo: function void (a: integer) inherit bar
        {
            preventDefault();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9208
    def test_446(self):
        input = """
        main: function void() {}
        foo: function void(inherit a: auto)
        {
            a: auto = 1;
        }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9291 (1)
    def test_447(self):
        input = """
        main: function void() {}
        foo: function void (b: auto, c: auto)
        {
	        a: string = b + c;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9291 (2)
    def test_448(self):
        input = """
        main: function void() {}
        inc : function void (out n : integer, n: float) inherit foo
        {
            super(0.1, 1);
            n: string = 124;
        }
        foo : function auto (inherit n: float, b: integer){}
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9146 (wrong)
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9315
    def test_449(self):
        input = """
        a: auto;
        """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9047
    def test_450(self):
        input = """
        main: function void()
        {
            x: auto = x + 10;
            y: integer = x;
            z: auto = z + z;
            w: string = z;
            t: string = z;
            u: integer = z;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(w, StringType, Id(z))"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9190
    def test_451(self):
        input = """
        main: function void()
        {
            a: integer;
            for (a = 1, 1, a + 1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(a), IntegerLit(1)), IntegerLit(1), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9192
    def test_452(self):
        input = """
        main: function void() {}
        foo: function string(foo: integer)
        {
            a: integer = foo;
            b: string = foo(a);
            c: auto;
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [Id(a)])"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9354
    def test_453(self):
        input = """
        main: function void()
        {
            a = b;
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9346
    def test_454(self):
        input = """
        main: function void() {}
        M: function void (a: integer) inherit N {}
        N: function void (inherit a: integer) {}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9202
    def test_455(self):
        input = """
        main: function void() {}
        x: array [1,2,3] of integer;
        y: auto = x[2 < 3];
        """
        expect = """Type mismatch in expression: BinExpr(<, IntegerLit(2), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9352
    def test_456(self):
        input = """
        main: function void() {}
        a: array[2] of integer = { {1}, {2} };
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9239
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9258
    def test_457(self):
        input = """
        main: function void() {}
        a: array [2, 3, 2] of integer = {{{1, 2}, {1, 2}}, {{1, 2}, {1, "2"}, {1, 2}}};
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])])"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9258
    def test_458(self):
        input = """
        main: function void() {}
        a: auto = { {1 , 2}, { 1,1.5} };
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), FloatLit(1.5)])])"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9390
    def test_459(self):
        input = """
        main: function void() {}
        foo: function auto() {}
        a: float = -foo();
        b: float = foo();
        c: integer = foo();
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    # CONFLICTING
    # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9395
    def test_460(self):
        input = """
        test1 : function string(y : auto)
        {
            y = 2;
            return;
        }
        main: function void()
        {
            test1(true);
        }
        """
        expect = """Type mismatch in statement: Assign(Id(y), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 460))
