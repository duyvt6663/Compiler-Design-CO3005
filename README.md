# Compiler-Design-CO3005
Assignment from course CO3005 - Principle of Programming Languages.

* Lexer + Parser: implemented using Antlr.
* AST: implemented using visitor pattern on the tokens/grammar produced by Lexer+Parser.
* Static Checker: implemented using visitor pattern on AST and performed Type Inference using Hindley Milner Type System (Stronger than what's required in the course which is just a replication of Type Deduction from C++).
* Code Generation: in progress ...  
* Test Generator: randomly generating testcases that suit each phase. Implemented by unrolling Parser and Lexer generated by Antlr and had depth-control mechanism.
---
# How to run  
Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite
