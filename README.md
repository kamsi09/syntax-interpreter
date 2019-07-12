# Concepts of Programming
Interpreter Programming Project
CS 3361 Concepts of Programming Languages
Below is the syntax and semantics for a single Boolean expression followed by
a period. Write a program which prompts the user to input a file name which
contains the Boolean expression or simply to input the string to be checked
(indicate which input method you will use in your comments). Although it
may not matter (depending on your implementation), you may assume that no
input will be longer than 1000 characters in length. Expressions may contain
white spaces and white spaces should be considered to be delimiters (i.e. a
white space between : and = of the assignment operator or between the − and
> of the implication symbol would be a syntax error). The program should
check if the expression in the file is of valid syntax and, if valid and has no
undefined variables, output the value of the expression. If there is an undefined
variable, the program should give a message that the variable was undefined
and continue checking the syntax. If the same undefined variable is used more
than once, only one error should be given for that variable. The output should
either be an error message(s) or a message that gives the value of the expression.
You must use the techniques taught in the class - this is a recursive
descent interpreter.
Syntax: (note: for ∨ use the uppercase letter ”V”, for ∧ use the caret symbol, and
a valid var is a single lower case letters)
Selection Sets
hBi ::= hVAihITi . {#, ∼, T, F, var,(}
hVAi ::= #var := hITi ;hVAi {#}
::= ε {∼, T, F, var,(}
hITi ::= hCTi hIT T aili {∼, T, F, var,(}
hIT T aili ::= −> hCTi hIT T aili {−>}
::= ε {., ; ,)}
hCTi ::= hLi hCT T aili {∼, T, F, var,(}
hCT T aili ::= ∨ hLi hCT T aili {∨}
::= ∧ hLi hCT T aili {∧}
::= ε {−>, ., ; ,)}
hLi ::= hAi {T, F, var,(}
::= ∼ hLi {∼}
hAi ::= T {T}
::= F {F}
::= var {var}
::= ( hITi ) {(}
1
Syntactic Domains:
hBi : Bool def
hVAi : Var def
hITi : Imply term
hIT T aili : Imply tail
hCTi : Connect term
hCT T aili : Connect tail
hLi : Literal
hAi : Atom
Semantic Domain:
η : b = {true, f alse}
◦
σ : st = var → b
Semantic Function Domains:
α : Bool def → b
γ : Var def × st → st
β : Imply term × st→ b
δ : Connect term × st→ b
λ : b × Imply tail × st→ b
µ : b × Connect tail × st→ b
φ : Literal × st→ b
ψ : Atom × st→ b
Semantic Equations:
ψ( T , σ) = true
ψ( F , σ) = f alse
ψ( var , σ) = if σ[var] 6= ⊥ then σ[var] else >
ψ( (hITi) , σ) = (β( hITi , σ))
φ(∼ hLi , σ) = if φ( hLi , σ) 6= > then ¬φ( hLi , σ) else >
φ( hAi , σ) = ψ( hAi , σ)
δ( hLihCT T aili , σ) = µ(φ( hLi , σ),  hCT T aili , σ)
µ(η,  ∨hLihCT T aili , σ) = if η 6= > and φ( hLi , σ) 6= > then
µ(η ∨ φ( hLi , σ),  hCT T aili , σ) else >
µ(η,  ∧hLihCT T aili , σ) = if η 6= > and φ( hLi , σ) 6= > then
µ(η ∧ φ( hLi , σ),  hCT T aili , σ) else >
µ(η,  , σ) = η
β( hCTihIT T aili , σ) = λ(δ( hCTi , σ),  hIT T aili , σ)
λ(η,  −> hCTihIT T aili , σ) = if η 6= > and
λ(δ( hCTi , σ),  hIT T aili , σ) 6= > then
η → λ(δ( hCTi , σ),  hIT T aili , σ)
λ(η,  , σ) = η
γ( #var := hITi;hVAi , σ) = γ( hVAi , update(σ, β( hITi , σ)/var))
γ( , σ) = σ
α( hVAihITi. ) = β( hITi , γ( hVAi , σ[ ])