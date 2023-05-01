import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    ############################################################## 
    #                        CHECK VARDECL                       #
    ##############################################################
    def test_401_test_vardecl_1(self):
        input = """
            main: function void(){
                y: auto = y;
                x: auto = y != 1; 
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_402_test_vardecl_2(self):
        input = """
            main: function void(){
                y: auto = y- 1;
                x: auto = y != 1;
                z: auto = -y; 
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_403_test_vardecl_3(self):
        input = """
            main: function void(){
                x, y: integer = 100.3, 20;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(100.3))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_404_swap_float_int(self):
        input = """
        foo: function auto() {}
        a: float = -foo();
        c: integer = foo();
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    ############################################################## 
    #                      NO ENTRY POINT                        #
    ############################################################## 
    def test_405_no_entry(self):
        input = """main: function integer(mem: string){}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_406_no_entry(self):
        input = """main: function integer(){}"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_407_entry_sym_table(self):
        input = """
            mai: string = "boo";
            main: function void(){}
            man: function integer(inherit dun: float){
                keke: integer = 239;
                if(keke < 565){
                    surigame: string = mai::"dumdum";
                }
                {
                    tes: auto = 34;
                    main();
                }
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 407))
    ############################################################## 
    #                     CHECK INHERITANCE                      #
    ##############################################################
    def test_408_invalid_param_1(self):
        input = """
            foo: function integer(inherit k: integer){}
            man: function void(out k: string)inherit foo{ }
            main: function void(){}
        """
        # this case needs more attention
        expect = "Invalid Parameter: k"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_409_check_inherit_1(self):
        input = """
            man: function void(out k: string)inherit foo{
                super(1);
                d = "bro";
            }
            foo: function integer(inherit c: integer)inherit bar{}
            bar: function void(inherit d: string){}
            main: function void(){}
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_410_check_inherit_2(self):
        input = """
            man: function void(out k: string)inherit foo{
                c = 1000;
            }
            foo: function integer(inherit c: integer){}
            main: function void(){}
        """
        expect = "Invalid statement in function: man"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_411_check_inherit_3(self):
        input = """
            man: function void(out k: string)inherit foo{
                super(12);
            }
            foo: function integer(inherit c: integer){}
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_412_check_inherit_4(self):
        input = """
            man: function void(out k: string)inherit foo{ }
            main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_413_check_inherit_5(self):
        input = """
            main: function void(out k: integer, k: string){super();}
        """
        expect = "Redeclared Parameter: k"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_414_check_inherit_6(self):
        input = """
            main: function void(out k: integer, a: string){super();}
        """
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_415_check_inherit_7(self):
        input = """
            boo: function void(a: integer){}
            main: function void(a: integer) inherit boo{super(1, "dum");}
        """
        expect = "Type mismatch in expression: StringLit(dum)"
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_416_check_inherit_8(self):
        input = """
            boo: function void(a: integer){}
            main: function void(boo: integer) inherit boo{super(1);}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_417_check_inherit_9(self):
        input = """
        bar: function void (inherit a: integer) {}
        foo: function void (a: integer) inherit bar
        {
            preventDefault();
            end: auto;
        }
        """
        expect = """Invalid Variable: end"""
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_418_check_inherit_10(self):
        input = """
        x: auto = 1000.0;
        bar: function void (inherit a: integer) {}
        foo: function void (r: integer) inherit bar{
            super(x);
        }
        """
        expect = """Type mismatch in expression: Id(x)"""
        self.assertTrue(TestChecker.test(input, expect, 418))
    ############################################################## 
    #                          REDECLARED                        #
    ############################################################## 
    def test_419_redeclared_1(self):
        input = """
            main: function integer(){}
            main: function void(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_420_redeclared_2(self):
        input = """
            mamn: function void(out man: string){ 
                man: integer;
            }
            main: function void(){}
        """
        expect = "Redeclared Variable: man"
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test_421_redeclared_3(self):
        input = """
            foo: function integer(inherit k: integer){}
            man: function void(out sk: string)inherit foo{ 
                super(1000);
                k:string;
            }
            main: function void(){}
        """
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_422_redeclared_4(self):
        input = """
            a: integer = 1;
            foo: function void (b: integer) inherit a { super("kek"); }
            a: function string (inherit c: string) {}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_423_redeclared_5(self):
        input = """
            a: function void (b: integer) inherit a { super(1); }
            foo: function void(){
                a: integer = 1000;
            }
            a: function string (inherit c: string) {}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_424_redeclared_6(self):
        input = """
            printFloat: function integer (b: integer) { return 1000; }
        """
        expect = "Redeclared Function: printFloat"
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_425_redeclared_7(self):
        input = """
            readInteger: auto = 1000;
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input, expect, 425))
    ############################################################## 
    #                        MUST IN LOOP                        #
    ############################################################## 
    def test_426_not_in_loop_1(self):
        input = """
            main: function void(){
                V, v, R, Htd, OW, Lq, M: integer;
                for ( V = - v, v < Htd, 1000) 
                    main();     
                break;
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_427_in_loop_1(self):
        input = """
            main: function void(){
                V, v, R, Htd, OW, Lq, M: integer;
                for ( V = - v, R + Htd > R, Lq* M) {
                    main ();     
                    break;
                }
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_428_in_loop_2(self):
        input = """
            main: function void(){
                V, v, R, Htd, OW, Lq, M: integer;
                for ( V = - v, R + Htd < 2, Lq* M) {
                    main ();  
                    while(v < 4439) 
                        do{
                            break;
                            dem: string = "yo passed";
                        } 
                        while(R + Htd > 3);
                    break;
                }
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 428))
    ############################################################## 
    #                          UNDECLARED                        #
    ############################################################## 
    def test_429_undeclared_1(self):
        input = """
            man: function void(out sk: string)inherit foo{ }
            main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_430_undeclared_2(self):
        input = """
            main: function void(){
                x = 43;
                x: integer;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_431_undeclared_3(self):
        input = """
            main: function void(){
                {
                    x = 43;
                }
                x: integer;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_432_undeclared_4(self):
        input = """
            main: function void(){
                V, v, R, Htd, OW, Lq, M: integer;
                for ( V = - v, false, 1000 + i) 
                    main();     
            }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433_undeclared_5(self):
        input = """
            main: function void(){
                mam();
            }
        """
        expect = "Undeclared Function: mam"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_434_undeclared_6(self):
        input = """
            main: function void(){
                o: integer = mam();
            }
        """
        expect = "Undeclared Function: mam"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_435_test_do_while(self):
        input = """
            main: function void(){
                do{
                    x: integer = 1;
                }
                while(x > 1);
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 435))
    ############################################################## 
    #                   TYPE MISMATCH IN EXPR                    #
    ############################################################## 
    def test_436_func_overshadowed(self):
        input = """
            V: function integer(){}
            main: function void(){
                V: integer;
                a: string = V ();     
            }
        """
        expect = "Type mismatch in expression: FuncCall(V, [])"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_437_args_num_1(self):
        input = """
            V: function integer(x: integer, y: string){}
            main: function void(){ V();  }
        """
        expect = "Type mismatch in statement: CallStmt(V, )"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_438_args_num_2(self):
        input = """
            V: function integer(x: integer, y: string){}
            main: function void() inherit V{ super(1);  }
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_439_args_num_3(self):
        input = """
            V: function integer(x: integer, y: string){}
            main: function void() inherit V{ super(1,2);  }
        """
        expect = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_440_args_num_4(self):
        input = """
            V: function integer(x: integer, y: string){}
            main: function void() inherit V{ super(1,2,3);  }
        """
        expect = "Type mismatch in expression: IntegerLit(3)"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_441_comp_type(self):
        input = """
            main: function void(){
                a: boolean = 1 == false;
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_442_div_op(self):
        input = """
            main: function void(){
                x: auto = 5.5;
                a: integer = x % 55;
            }
        """
        expect = "Type mismatch in expression: BinExpr(%, Id(x), IntegerLit(55))"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_443_arr_cell_index(self):
        input = """
            main: function void(){
                x, y: auto = {1,2,3}, y;
                a: integer = x[y];
                y = "hehe";
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(y), StringLit(hehe))"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_444_wrong_index(self):
        input = """
            main: function void(){
                a: auto = {1, 2, 3};
                x: integer = a["haha"];
            }
        """
        expect = "Type mismatch in expression: StringLit(haha)"
        self.assertTrue(TestChecker.test(input, expect, 444))
    ############################################################## 
    #                   TYPE MISMATCH IN STMT                    #
    ############################################################## 
    def test_445_call_overshadowed(self):
        input = """
            V: function integer(){}
            main: function void(){
                V: integer;
                V ();     
            }
        """
        expect = "Type mismatch in statement: CallStmt(V, )"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_446_assign_wrong_typ(self):
        input = """
            main: function void(){
                main = 2988;  
            }
        """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_447_assign_wrong_typ_2(self):
        input = """
            main: function integer(){}
            boo: function void(){
                main = main;
            }
        """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_448_call_stmt(self):
        input = """
            boo: function void(a: integer){
                boo("heh");
            }
        """
        expect = "Type mismatch in statement: CallStmt(boo, StringLit(heh))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_449_funcall(self):
        input = """
        foo: function integer(a: string){}
        main: function void(){
            a: integer = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_450_call_stmt_2(self):
        input = """
        foo: function integer(a: string){}
        main: function void(){
            foo();
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_451_call_stmt_2(self):
        input = """
        foo: function integer(a: string){}
        main: function void(){
            a: integer = foo;
        }
        """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    ############################################################## 
    #                        TYPE INFERENCE                      #
    ############################################################## 
    def test_452_test_coercion_1(self):
        input = """
            main: function void(){
                V: auto = 22;
                a: integer = V+48.6;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, Id(V), FloatLit(48.6)))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_453_test_coercion_2(self):
        input = """
            main: function void(){
                V: auto = 22;
                a: float = V+48;
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_454_test_coercion_3(self):
        input = """
            main: function void(){
                V: auto = V;
                a: integer = V+33;
                V = 3.3;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(V), FloatLit(3.3))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_455_test_coercion_4(self):
        input = """
            foo: function integer(a: float){return 1000;}
            main: function void(){
                foo(100);
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_456_test_coercion_5(self):
        input = """
            main: function void(){
                x, y: auto = x, y;
                z: integer = (x + 1)+y;
                y = 100.0;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(y), FloatLit(100.0))"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_457_test_coercion_6(self):
        input = """
            foo: function auto() {}
            a: integer = -foo();  
            x: auto = x + foo();
            bar: function void(){ x = 100.0; }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(100.0))"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_458_test_coercion_7(self):
        input = """
            bar: function void(){
                x, y: auto;
                z: auto = x + 1;
            }
        """
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_459_test_coercion_8(self):
        input = """
            bar: function void(){
                x: array[3] of float = {1, 2, 3};
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_460_test_coercion_9(self):
        input = """
        a: auto = -2.3;
        c: integer;
        foo: function auto() {c = a;}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(c), Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_461_test_coercion_10(self):
        input = """
        c: auto = 1000.0;
        foo: function auto(a: integer) {foo(c);}
        """
        expect = """Type mismatch in statement: CallStmt(foo, Id(c))"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_462_test_arrlit_infer_1(self):
        input = """
            main: function void(){
                x: auto = x+1; 
                y: auto = y-2; 
                v: auto = {x, y}; 
                x = 24.3; 
                y = 1;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(24.3))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_463_test_arrlit_infer_2(self):
        input = """
            main: function void(){
                v: auto = {1,2}
                v = 492;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(v), IntegerLit(492))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_464_test_string_int(self):
        input = """
            main: function void(){
                v: string = 1000;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(v, StringType, IntegerLit(1000))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_465_test_param_string_int(self):
        input = """
            mam: function void(b: string){
                b = 100;
            }
            main: function void(){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), IntegerLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_466_test_param_auto(self):
        input = """
            mam: function void(b: auto){
                mam(100);
                b = "string";
            }
            main: function void(){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test_467_test_comparison(self):
        input = """
            mam: function void(b: integer){
                x: boolean = 2 != true;
            }
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 467))
    ############################################################## 
    #                          CHECK LITERAL                     #
    ############################################################## 
    def test_468_test_arrlit_1(self):
        input = """
            main: function void(){
                v: array[2,2] of integer = {{1,2}, {2,3}};
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_469_test_arrlit_2(self):
        input = """
            main: function void(){
                v: array[2,2] of integer = {{1,2}, {2,3,3}};
            }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_470_test_arrlit_3(self):
        input = """
            main: function void(){
                v: array[2] of integer = {1, 2.3};
            }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.3)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_471_test_arrlit_4(self):
        input = """
            main: function void(){
                v: array[2] of float = {1.2, 2};
            }
        """
        expect = "Illegal array literal: ArrayLit([FloatLit(1.2), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_472_test_arrlit_5(self):
        input = """
            main: function void(){
                v: array[2, 2] of float = {{1.2, 3.5}, {1.0, 3.543}};
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_473_test_arrlit_6(self):
        input = """
            main: function void(){
                v: array[2, 2] of float = {{1.2, 3}, {1.0, 3.543}};
            }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([FloatLit(1.2), IntegerLit(3)]), ArrayLit([FloatLit(1.0), FloatLit(3.543)])])"
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_474_test_arrlit_7(self):
        input = """
            main: function void(){
                x, y: auto = 1000, 22.4;
                v: array[2] of float = {x,y};
            }
        """
        expect = "Illegal array literal: ArrayLit([Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
    ############################################################## 
    #                       CHECK ARRAY CELL                     #
    ##############################################################
    def test_475_test_arr_cell_1(self):
        input = """
            mam: function void(b: string){
                v: array[2] of integer = {1,2};
                x: integer = v[0];
            }
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_476_test_arr_cell_2(self):
        input = """
            mam: function void(b: string){
                v: array[2,2] of integer = {{1,2},{3,4}};
                x: integer = v[0];
            }
            main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, ArrayCell(v, [IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_477_test_arr_cell_3(self):
        input = """
            mam: function void(b: string){
                v: array[2,2] of integer = {{1,2},{3,4}};
                x: integer = v[0,0,0];
            }
            main: function void(){}
        """
        expect = "Type mismatch in expression: ArrayCell(v, [IntegerLit(0), IntegerLit(0), IntegerLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_478_test_arr_cell_4(self):
        input = """
            mam: function void(b: string){
                v: array[2,2] of integer = {{1,2},{3,4}};
                v[0,0] = 1000;
            }
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_479_test_arr_cell_5(self):
        input = """
            mam: function void(b: string){
                v: string = "kek";
                a: integer = v[1];
            }
            main: function void(){}
        """
        expect = "Type mismatch in expression: ArrayCell(v, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_480_test_arr_cell_6(self):
        input = """
            mam: function void(b: string){
                x: array[3] of integer = {1,2,3};
                v: auto = 3.5;
                a: integer = x[v];
            }
            main: function void(){}
        """
        expect = "Type mismatch in expression: Id(v)"
        self.assertTrue(TestChecker.test(input, expect, 480))
    ############################################################## 
    #                CHECK FUNCCALL AND CALLSTMT                 #
    ############################################################## 
    def test_481_test_func_call_1(self):
        input = """
            foo: function string(){return "zam";}
            main: function void(){
                v: string = foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_482_test_func_call_2(self):
        input = """
            foo: function integer(){return "zam";}
            main: function void(){}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(zam))"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_483_test_func_call_3(self):
        input = """
            foo: function auto(){}
            main: function void(){
                a: auto = foo();
                foo();
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_484_test_func_call_4(self):
        input = """
            foo: function integer(){}
            main: function void(){
                a: string = foo();
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_485_test_call_stmt_1(self):
        input = """
            foo: function auto(){}
            main: function void(){
                a: string = foo();
                foo();
                m: integer = foo();
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_486_test_params_1(self):
        input = """
            foo: function void(a: integer, b: integer){}
            main: function void(){
                foo(3, 4);
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_487_test_params_2(self):
        input = """
            foo: function void(a: float, b: float){}
            main: function void(){
                x: auto = x;
                foo(x, x+2);
                x = 3.3;
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_488_test_params_3(self):
        input = """
            foo: function void(a: float, b: float){
                d: auto = a + 1;
            }
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_489_test_params_4(self):
        input = """
            foo: function void(a: auto, b: float){
                a = b;
                a = 1000.6;
            }
            main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 489))
    ############################################################## 
    #                          SCOPE CHECK                       #
    ##############################################################
    def test_490_after_decl_1(self):
        input = """
            main: function void(){
                a: float = v;
                v: integer = 3;
            }
        """
        expect = "Undeclared Identifier: v"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_491_after_decl_2(self):
        input = """
            main: function void(){
                a: float = v;
            }
            v: integer = 3;
        """
        expect = "Undeclared Identifier: v"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_492_global_func(self):
        input = """
            main: function void(){
                mam();
            }
            mam: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_493_global_var(self):
        """Global vars cant be declared after usage"""
        input = """
            main: function void(){
                x: integer = a;
            }
            a: integer = 1000;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 493))
    ############################################################## 
    #                      CHECK ORDER OF ERROR                 #
    ############################################################## 
    def test_494_test_params_2(self):
        input = """
            main: function void(a: float, b: float){a = "1000";}
            main: function void(){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(1000))"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_495_test_do_while(self):
        input = """
            main: function void(){
                do{
                    x: integer = "hehe";
                }
                while(x > 1);
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(hehe))"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_496_index(self):
        input = """
            main: function void(){
                a: auto = {1, 2, 3};
                x: integer = a["haha", 1+"haha"];
            }
        """
        expect = "Type mismatch in expression: StringLit(haha)"
        self.assertTrue(TestChecker.test(input, expect, 496))
    ############################################################## 
    #                     CHECK LOOPS/CONDITIONS                 #
    ############################################################## 
    def test_497_forstmt_1(self):
        input = """
            main: function void(){
                V, v, R, Htd, OW, Lq, M: integer;
                for ( V = - v, R+Htd, 1000 + i) 
                    main();     
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(V), UnExpr(-, Id(v))), BinExpr(+, Id(R), Id(Htd)), BinExpr(+, IntegerLit(1000), Id(i)), CallStmt(main, ))"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_498_forstmt_2(self):
        input = """
            main: function void(){
                V: float = 100.3;
                for ( V = 10, false, 1000) 
                    main();     
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(V), IntegerLit(10)), BooleanLit(False), IntegerLit(1000), CallStmt(main, ))"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_499_forstmt_3(self):
        input = """
            main: function void(){
                V, x: auto = 100, 11.11;
                for ( V = 10, false, x) 
                    main();     
            }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(V), IntegerLit(10)), BooleanLit(False), Id(x), CallStmt(main, ))"
        self.assertTrue(TestChecker.test(input, expect, 499))
    ############################################################## 
    #                         RETURN BRANCH                      #
    ############################################################## 
    def test_500_retstmt_1(self):
        input = """
            main: function void(){
                return;
                return "di";
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 500))
    def test_501_retstmt_2(self):
        input = """
            main: function void(){
                if(1 < 2)
                    return;
                else
                    return 100;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 501))
    def test_502_retstmt_2(self):
        input = """
            foo: function integer(){}
            main: function void(){
                if(1 < 2)
                    return;
                else
                    foo();
                return 100;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 502))
    ############################################################## 
    #                      CHECK BUILTIN FUNC                    #
    ############################################################## 
    def test_503_read_float(self):
        input = """
            C : function integer   ( ) inherit readFloat { 
                super ( ) ;  
                I  : integer   = jruU9 ( )    == ! lU     :: ZO   - LN    == x   * J       ;  
            }
        """
        expect = "Undeclared Function: jruU9"
        self.assertTrue(TestChecker.test(input, expect, 503))
    def test_504_read_bool(self):
        input = """
            M  : integer   = ! readBoolean ( );  
            V : function array [ 0 , 0 ] of float    ( inherit out IGv : auto    ) { }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(M, IntegerType, UnExpr(!, FuncCall(readBoolean, [])))"
        self.assertTrue(TestChecker.test(input, expect, 504))
    def test_505_super_assign(self):
        input = """
            C : function integer   ( ) inherit readFloat { 
                super = 1000; 
            }
        """
        expect = "Undeclared Identifier: super"
        self.assertTrue(TestChecker.test(input, expect, 505))
    def test_506_super_var_decl(self):
        input = """
            C : function integer   ( ) inherit readFloat { 
                super: auto = 1000; 
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 506))
