## PYTHON – REFERENCE SHEET  
(CHEAT SHEET)

**Valdemar W. Setzer**  
[www.ime.usp.br/~vwsetzer](https://www.ime.usp.br/%7Evwsetzer) (section [Educational resources](https://www.ime.usp.br/%7Evwsetzer/#EER))  
Version 2.13 12/31/2024. Partial automatic translation from the [original in Portuguese](https://www.ime.usp.br/%7Evwsetzer/python-opers-funcoes.html): Eduardo Furlan; revision: V.W. Setzer

### **INDEX**

  1. [Notes](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#OBS)
  2. [Types, Constants, Variables, and Arrays](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#TIP)
  3. [Operators](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#OPE)
  4. [Logical operators (Boolean)](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#OPL)
  5. [Native functions](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#FNA)
  6. [Some mathematical functions and constants](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#FMA)
  7. [Other functions](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#OFU)
  8. [Precedence (execution order)](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#PRE)
  9. [Function declaration and usage](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#DFU)
  10. [Lambda notation](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#LAM)
  11. [Global and local identifiers](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#GLO)
  12. [Classes](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#CLA)  
12.1 [Introduction](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#CLA)  
12.2 [Polymorfism](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#CLP)  
12.3 [Inheritance](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#CLH)
  13. [Compound statements](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#COC)
  14. [Modules](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#MOD)  

14.1 [Introduction](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#MOI)  
14.2 [Some modules](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#MOA)  

  15. [Reserved words](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#PAL)
  16. [References](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#REF)  
15.1 [Tutorials](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#TUT)  
15.2 [Other references](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#ORE)
  17. [Installing Python and using the IDLE interpreter and its editor](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#INS)
  18. [Courses](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#CUR)
  19. [Texts, programming environments, documentation and programming forums](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#AMB)
  20. [Aknoledgments](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#AGR)



### **1.NOTES**

  1. Attention: many of the cells in the tables below contain a single line; if there are many cells with more than one line, increase the size of the browser window or decrease the size of the letters (generally on PC with Ctrl –; to increase it back, Ctrl +); this will provide for a proper justification.
  2. All operators, functions and commands in the examples were tested with the Python 3.6.1 IDLE ("Integrated Development and Learning Environment") interpreter, except for a few items where Azure Jupyter was used (see the [Environments](https://www.ime.usp.br/~vwsetzer/Python-cheat-sheet.html#AMB) item ). Tests with other versions are annotated with the version, e.g. ex. {3.7.2}. Functions are ususally called "methods".
  3. See [ informations on IDLE](https://docs.python.org/3/library/idle.html#command-line-usage). Instead of using IDLE, one may activate a remote Python compiler provided by W3 Schools. Simply jump to [www.w3schools.com/python/trypython.asp?filename=demo_compiler](https://www.w3schools.com/python/trypython.asp?filename=demo_compiler) but it seems that it doesn't use the last Python version.   
Note: Instead of IDLE, prefer using the IDLE Editor, it is much more practical than just IDLE. See section 16.3. After typing the program, it is necessary to activate the Run button. When using the IDLE Editor or the W3 compiler, to display the result of an operation or variable value, the print() function is required. Attention: in IDLE, typing a line and pressing Enter executes the command on the line. To give multiple statements on a single line, they must be separated by ; . For multiple lines before pressing Enter, it is necessary to use a text editor, copy and paste into IDLE. Or execute commands that are in a file. 
  4. In all tables below, the prior execution of the following assignment statements are assumed: A=1; B=2; C=3; D=1.2; E=2.3; F=3.4; G='abc'; H='def'
  5. In expressions using operators and functions, whitespace is ignored. Thus, one can write A = 1; X= 2+ B; etc. Operator symbols, function names, variable names and statement names cannot contain blanks. Thus, A b and + = are not considered as the variable Ab and the operator +=, but rather as A, b, + and = separately (resulting in syntax errors).
  6. Comments: # defines the rest of the line as a comment (that is, ignored by the interpreter); """ ... """ (three quote signs) defines everything between the """ as a comment, including multiple lines of code.
  7. In the examples, reserved words are written in **bold** face.
  8. In the examples, after typing an IDLE command in a single line, it is executed when typing Enter (end of line); the eventual result appears in this text after "->", e.g. A+B -> 3 (after giving the command >>>A+B and Enter, 3 appears on the next line). Attention: when using copy/paste, several lines can be pasted, but they must all form just one statement, for example an **if** or **while** with several lines. However, two or more commands can be given on a single line, separated by ";": X=1; Y=2; X,Y -> (1,2).  

  9. Some functions require adding a special module to the program, which is done with the **import** statement. For details about it, see[ https://docs.python.org/3/library/importlib.html](https://docs.python.org/3/library/importlib.html)
  10. Attention: the examples on this page can be copied and pasted into the IDLE Editor (See section 16 below) and executed, taking care to eliminate the ->.  

  11. See a page with [examples of complete programs](https://www.ime.usp.br/%7Evwsetzer/python-examples.html) tested in Microsoft's Azure environment. See also a [website with many examples](http://exercism.io/languages/python/exercises); the codes are in the "Test Suite" tabs.
  12. See an excellent paper on [programming style in Python](https://peps.python.org/pep-0008/). {EF}
  13. Comments, suggestions and criticisms are very welcome!!!  

  14. Section 12 contains acknowledgments with the contributors' code in curly braces {...}, mentioned in the parts for which they contributed.



### **2\. TYPES, CONSTANTS, VARIABLES AND ARRAYS**

#### 2.1 Types of varibles

Concerning types of variables, Python is considered a _dynamic_ and _strongly typed_ language: 1. _Strongly Typed_ : Python does not allow implicit operations between different types without explicit conversion. For example, adding a string to a number, such as A+G (see values attributed in last section, subsection 4), will generate an error unless the string is explicitly converted to a number. Thus, addding a string of characters (see below) to a number will gerate an error, unless the string is converted into a number through a type conversion function. But numbers of different types are allowed, such as A+D. _Dynamically Typed_ : The type of a variable is determined at runtime and can change as new values are assigned to it, meaning that a variable x adopts the type of the value assigned to it. For example, when executing the assignment satement x = 1, x will be of type integer. If the assignment x = 1.5 is then executed, x will become of type floating point.  
  
Variables function as references (or pointers) to objects. When a value is assigned to a variable, it does not directly store the value, but rather a reference to the object that contains the value.  


  


#### 2.2 Numeric types

**Integer** (int): precisão ilimitada. E.g.: 1234567890123456789012345  
**Constants. Bynary**. Ex.: 0b101 or 0B101 (decimal value 5); **octal** : 0o127 or 0O127 (87); **hexadecimal** : 0xA5B or oXA5B (2651). Hexadecimal constants are commonly used to represent binary numbers in an easier-to-read notation.  
**Floating point** : usually implemented using the double type in the C language. E.g.: .12345678901234567890 -> 0.12345678901234568 (note the rounding off).  
**Complexo** : contém uma parte real, e uma imaginária indicada por um j. Exs.: constante (1+2j) ou (1+2J); variável (A+D*1j)  
**Complex** : contains a real part and an imaginary part indicated by a j. E.g.: constant (1+2j) or (1+2J); variable (A+D*1j)  
To convert any type to integer use the functions int(), to floating point float(), to complex complex(). These functions should be used especially in data input, input() – which always gives a string type (str).  
The NumPy module (see references), which must be installed, allows for the use of a wide variety of numeric types. To define a 32-bit floating point variable, simply give, for example,  
x = numpy.float32(1.0)  


#### 2.3 Thecharacter string type 

**_Example_** : 'tuv5xyz: ' -> 'tuv5xyz: '; "tuv5xyz: " -> 'tuv5xyz: '; 'tuv5x"yz: ' -> 'tuv5x"yz: '; If the command STR = 'This is a string' is executed, then STR -> 'This is a string'  
**_Empty string_** : '' (two apostrophes) or " " or "" "" -> (one blank space).  
**_Indexing_** : the 1st index indicates the initial element, starting at 0; the 2nd the final one, starting at 1. For the STR string above, STR[0] -> 'T'; STR[5:9] -> 'is a']; STR[5:] -> 'is a string'. To address the last elements of the list, use negative numbers: STR[-1] -> g; STR[-3] -> i  
**_Locating a list elemet_** : string elements are separated by spaces x = STR.index('is'); x -> 2  
**_Concatenation_** of strings: 'tuv5xyz: ' + STR -> tuv5xyz: This is a string; 2*STR -> This is a stringThis is a string  


#### 2.4 The ordered tuple type

**_Example_** : Tup = (A, 5, 3.14, 'blah'); Tup -> (1, 5, 3.14, 'blah'). `For the value of A, see section 3 of the notes.)  
_**Empty tuple**_ : ()  
**_Indexing_** : Tup[0] -> 1; Tup[1:3] -> (5, 3.14); Tup[2:] -> (3.14, 'blah'); 2*Tup -> (1, 5, 3.14, 'blah', 1, 5, 3.14, 'blah').   
Assigning a value to an element of a tuple is not valid:: Tup[1] = 10  
**_Locating_** a tuple element and tuple **_concatenation_** : as in 2.3  


#### 2.5 The list type

**_Example_** : L = [A, 5, 1.2, 'blah']  
**_Empty list_** : []  
**_Indexing_** : L[2] -> 1.2; L[1:4] -> [5, 1.2, 'blah']. Note that indices of elements range from 0 to, say, _n_. L[i:j] indicates the elements starting at the element with index i and ending at the element with index j–1. L[5] -> gives an error because there is no element with index 5. L[4] = 9 -> gives the same error. Adding one more element (always at the end of the list): L = L + [9]; L -> [1, 5, 1.2, 'bla', 9]; L = L \+ [] does not change L.  
**_Assignment_** to an element: the following is valid: L[3]=10; L -> [1, 5, 1.2, 10].  
_**Deleting**_ an element from a list: use the statement **del**. E.g. **del** L[2]; L -> [1, 5, 10];  
**_Locating_** a list element and list **_concatenation_** : as in 2.3  


#### 2.6 The diccionary type

**_Example_** : Dic = {5:10, 3:'blah', 'bleh':'A', 'A':'8'}; Dic ->{5: 10, 3: 'blah', 'bleh': 'A', 'A': 8}  
Note that each element of a dictionary is of the form x:y, where x is the _index_ and y is the _value_ associated with that index. Indexes or values that are alphabetic must be enclosed in apostrophes or quotation marks.  
**_Indexing_** : Dic[5] -> 10; Dic[3] -> blah; Dic['bleh'] -> A; Dic[3] -> 'blah'; DIC['A'] -> 8  
Getting **_all indices_** (keys): Dic.keys() -> dict_keys([5, 3, 'bleh', 'A'])  
Getting _**all values**_ : Dic.values() -> dict_values(10, 'blah', 'A', '8'])  
dict_keys and dict_values cannot be indexed. To work with all indices or values, one may transform them into lists and then work with them {MDG}:  
  L = [x **for** x **in** Dic.keys()]; L -> [5, 3, 'bleh', 1]  
  L = [x **for** x **in** Dic.values()]; L -> [10, 'blah', A, 8]  


#### 2.7 The set type

**_Example_** S = {1, 'two', 3, 'four'}; S -> {3 , 1, 'two', 'four'} (it seems that printed order is arbitrary)  
Sets are unordered, cannot be indexed, and the system eliminates duplicates. E.g. print({1, 2, 1, 3} -> {1, 2, 3}  
_**Empty set** : {}_  
**_Usage_**._Number of elements_ (_cardinality_): len(S) -> 4\. _Membership_ : 'two' **in** S -> True. _Union_ : S | {5} -> {1, 3, 5, 'four', 'two'} (apparently in alphabetic order). _Intersection_ : S & {1, 'two'} -> {1, 'two'}. _Complementation_ : S – {1, 'two'} -> {3, 'four'}. Tests for _proper superset_ : S > {1, 'four'} -> True. _Superset_ : >=; _Proper subset_ : <. _Subset_ : <=. _Exclusive unio_ n (eliminates common elements): S ^ {'two', 5} -> {1, 3, 5, 'four'}  
There are two types of sets: _set_ , in which its elements can be changed, and _frozenset_ , which cannot be changed. The construction of a set is automatic. Ex.: x = frozenset(({1, 2}); x.pop() -> error. Declared subsets of sets must be of type _frozenset_. The values True and 1 are considered the same value in sets, and are treated as duplicate.   


#### 2.8 The type range of integers

**_Specification_** : range(_m_ , _n_ , _k_), with optional _n_ and _k_ or optional k only, generating the integers of a list _r_ such that _r_[_i_] = _m_ \+ _k_ *_i_ , where _i_ >= 0 and _i_ < abs(n)  
Examples: list(range(5)) -> [0, 1, 2, 3, 4]; list(range(0, 8, 2)) -> [0, 2, 4, 6]; list(range(-1, -10, -2)) -> [-1, -3, -5, -7, -9]  
Usage in **for** statements: see the statements in section 13 below and in 2.5 above.  


#### 2.9 Vectors and arrays

Unlike almost all other programming languages, Python does not have an array type, since variable values can be of different sizes. Arrays are represented by lists, since they can be indexed as if they were arrays. In other languages, declaring an array produces the initialization of its values, that is, declaring the array causes all its elements to exist. However, this does not happen with Python lists; therefore, each new element must be added in the proper ordering.  
The NumPy module allows the use of vectors and arrays as in traditional languages. Assuming it is installed, to activate it and give it the internal name of np, give   
**import** NumPy as np. See the references for details on how to use it.   
**Examples**  
1\. To define a vector of 5 elements, initializing with 0 values (it could be any other value, such as the value of I or an expression): V=[I for I in range(4)]; V -> [0, 1, 2, 3]; note that V[4] does not exist and cannot receive a value, such as V[4]=5. To define it: V=V+[5]. To scan an entire vector of variable size, use len(V) -> 4\. Note that indeces of a list begin at value 0.  
2\. To define a two-dimensional array (a matrix), construct a list of sublists, each sublist with the same length: M=[[1, 2], [3, 4]]; M -> [[1, 2], [3, 4]]; M[1][1] -> 4; M[0][1] -> 2; len(M[1]) -> 2  
Initialization, with several values, of an array with 3 rows and 4 columns:  
M=[[0,0,0],[0,0,0]]; for I in range(2):; for J in range(3): M[I][J] = I+J+2 -> [[2, 3, 4], [3, 4, 5]]; M[2][1] -> 3  
For larger dimensions, simply extend the recipe.  


**3.** To loop through all elements and display their values:  
M=[[1, 2], [3, 4]]  
**for** I **in** [0,1]:   
  **for** J **in** [0,1]: print (M[I][J]))  
1  
2  
3  
4 **4.** Getting lines:  
**for** I in [0, 1]: print (M[I])  
[1, 2]  
[3, 4] **5.** Getting columns:  
**for** J **in** [0,1]:  
   **for** I **in** M:  
     print(I[J])  
1  
3  
2  
4 |  **6.** Generateing a vector with increasing values:  
M1=[]  
**for** I **in** range(3):  
   M1=M1+[I]  
print (M1)  
[0, 1, 2]  **7.** Generating a two-dimensional array with increasing values**  
** M1=[[],[]]  
J=0  
**for** I **in** range(2):  
   M1[I]=[J,J+1]  
   J=J+2  
print (M1)  
[[0,1], [2,3]]  
{PC} Drew attention to the initializtion of J **8.** Constroying a vector applying a function, e.g. sqrt, to all its elements:  
**import** math #insere o módulo math no programa  
V=[math.sqrt(I) **for** I **in** range(4)]  
print (V)  
[0.0, 1.0, 1.4142135623730951, 1.7320508075688772]   
---|---  
  
#### **2.10 Iterables**

In Python, an _iterable_ is an object capable of returning its members one at a time, allowing it to be looped over in a **for** -loop. Common examples of iterables include lists, tuples, dictionaries, and sets.

### **3\. OPERATORS**

**Op** |  **Meaning and types of operands** |  **Examples**  
---|---|---  
+ |  Binary operator (with two arguments): sum of int, float, or complex; concatenation of strings, lists and tuples |  A+B -> 3, D+E -> 3.5; A+D -> 2.2; (A+D*1j)+(E+C*1j) -> (3.3+4.2j);   
G+H -> 'abcdef'; (123, 'xyz') + ('L', '3.14') -> (123, 'xyz', 'L', 3.14)  
[1, 2] + [3] -> [1, 2, 3]  
+ | Unary operator (with one argument): no effect | +A -> 1  
– |  Binary subtraction operatorfor int, float or complex types; set complementation |  C–B -> 1; F–D -> 2.2; F–A -> 2.4  
print ({1,2,3,4,5}-{1,2}) -> {3,4,5}  
– | OUnary sign change operator | –A -> –1   
* |  Int, float or complex multiplication |  B*C -> 6; D*E -> 2.76; B*D -> 2.4; (A+D*1j)+(E+C*1j) -> (3.3+4.2j)  
/ |  Int, float or complex division |  C/B -> 1.5; F/E -> 1.4782608695652175; C/D -> 2.5;   
(A+D*1j)/(E+C*1j) -> (0.41287613715885235-0.016794961511546552j)  
// |  Division of int results in int; float by int gives integer part of result in float  |  C//B -> 1; F//D -> 2.0; F//B -> 1.0;   
% |  Int remainder from division of ints, integer part if division of floats |  C%B -> 1; F//D -> 2.0; F//B -> 1.0  
** |  **  
Potentiation of int, float or complex |  B**C -> 8; B**D -> 2.2973967099940698; D**B -> 1.44; D**E -> 1.5209567545525315; (1+1j)**2 -> 2j; 27**(1/3) -> 3 (raiz cúbica)  
== |  Tests for equality of int, float, complex or string, resulting **True** (true) or **False** (see the table of logical operators); with several == in a single command gives True only if each one of consecutive pairs is equal |  B==A*2 -> True; A==B -> False; A==D -> False; A==int(D) -> True; (A+B*1j)==(1+2j) -> True; G=='abc’ -> True; G==H -> False; 1==1==1 -> True; 1==1==2 -> False;  
!= |  Different, ditto |  A!=B -> True; A!=D -> True; A!=int(D) -> False; (1+2j)!=(2+2j) -> True;   
G!=H -> True; 1!=2!=3 -> True; 1!=1!= 2 -> False;  
>  |  Greater than, ditto, but without complex; tests for proper superset |  B>A -> True; A>B -> False; D>A -> True; E>D -> True; H>G -> True; 3>2>1 -> True; 3>2>3 -> False;  
<  |  Less than, ditto; proper subset |  A<B -> True; B<A -> False; etc.  
>= |  Greater than or equal, ditto; test for superset |  B>=A -> True; B>=D -> True; H>=G True; etc.  
<= |  Less than or equal, ditto; test for subset |  B<=A -> False; etc.  
& | Bitwise "and" of binary values; intersection of sets | 0b0101 & 0b0001 -> 1; bin(0b1100 & 0b1010) -> '0b1010' (left 0s are not displayed)  
| | Bitwise inclusive "or "; union of sets | bin(0b1100 | 0b1010) -> '0b1110'  
^ | bitwise "and" of binary values, decimal result in IDLE; intersection of sets  |  bin(0b0110 ^ 0b1010) -> '0b1100'  
>> | Bitwise shift to the right, inserting 0s to the left  | J = 10; bin(J) -> '0b1010'; bin(J>>1) -> '0b101' (left 0s are not displayed)  
<< | Bitwise shift to the left, inserting 0s to the right (equivalent to division by pow(2,n) | J = 10; bin(J) -> '0b1010'; bin(J<<2) -> '0b101000'  
**is** | Identity test of obejcts. Determines whether two variables point to the same object in memory. | x = y = 0; x is y -> True  
**is not** | Tests non-identity of objetos. Determines if two variables point to different objects in memory. | x = y = 0; x is not y -> False  
= |  Single or multiple assignment, right side int, float, complex or string; both sides can be an tuple without "(" and ")" |  A=1; A -> 1; A=D; A -> 1.2 (A changed from int to float);   
J=(A+D*1j); J -> (1+1.2j); J, I, K = 10, 20, B*30; I -> 20; J, K -> (10, 60)  
Exchage of variable values: X, Y= 3, 4; X, Y= Y, X; X, Y -> (4, 3)  
+= |  x += y equivalent to x = x + y |  J=1; J=+2; J -> 3; J=(1+2j); J+=(2+3j); J -> (3+5j)  
–= |  x -= y equivalent to x = x – y, inclusive de conjuntos |  J=3; J–=2; J -> 1  
*= |  x *= y equivalent to x = x * y |  J=2; J*=3; J -> 6  
/= |  x /= y equivalent to x = x /y |  J=6; J/=3; J -> 2.0  
//= | x // y equivalent to x = x // y | J=15; J//=4; J -> 3; J=15.5; J//=3.7; J -> 4.0  
%= |  x %= y equivalent to x = x%y |  J=6; J%=4; J -> 2.0; J=6; J%=2; J -> 0  
**= | x **= y equivalent to x = x**y | J=2; J**=3; J-> 8  
>>= | x >>= y equivalent to x = x>>y | J=0b1010; J>>=2; bin(J) -> '0b10' (left zeroes are not displayed)  
<<= | x <<= y equivalent to x = x<<y | J=0b1010; J<<=2; bin(J) -> '0b101000'  
&= | x &= y equivalent to x = x&y, inclusive for sets | J=0b1100; K=0b1010; J&=K; bin(J) -> '0b1000'  
^= | x ^= y equivalent to x = x^y, inclusive for sets | J=0b1100; K=0b0110; J^=K; bin(J) -> '0b1010'  
|= | x |= y equivalent to x = x|y, inclusive for sets | J=0b1100; K=0b1010; J|=K; bin(J) -> '0b1110'  
**if** |  Condition  
x= Value if True **if** logical expression **else** value if False | J = 1 **if** 4>3 **else** 2 -> 1  
J = 5 * (1 **if** B<A **else** 3*A); -> 15  
  
### 4\. LOGICAL OPERATORS (BOOLEANS)

**Op** |  **Meaning** |  **Examples**  
---|---|---  
  | In what follows, the prior execution of L1T =**True** is assumed; L2T = **True** ; L1F = **False** ; L2F = **False**  
**True** | Constant indicating "true" | The identifier "true" is accepted as a variable name, but thereafter it will not be considered tlogical constant anymore: true = False; print(true) -> False  
**False** | Constant indicating "false" | Ditto for false. Considered as False : **None** , 0, 0.0, 0j, ' ', (), [], {}; other values as True   
**not** | Negation: changes True to False and vice versa | **not** L1T -> False; **not** L1F -> True  
x **or** y | "Inclusive or"; gives **False** only if x and y are false, **True** otherwise.  
| L1T **or** L2T -> True; L1T **or** L1F -> True; L1F **or** L1T -> True; L1F **or** L2F -> False  
x **and** y | "and"; gives **True** only if x and y are true, False otherwise | L1T **and** L2T -> True; L1T **and** L1F -> False; L1F **and** L1T -> False; L1F **and** L2F -> False  
x **in** y | if x is in string, tuple, list or set y gives True, else False  |  'a' **in** 'false' -> True; 5 in (2, 5, 3) -> True; 3 **in** [2, 5, 3] -> True; 4 **in** [2, 5, 3] -> False  
x **not in** y | Contrary to **in** | 'a' not in 'false' -> False; 5 not in (2, 5, 3) -> False; 3 not in [2, 5, 3] -> False;   
4 not in [2, 5, 3] -> True   
**is** |  Object identity test. Determines whether two variables point to the same object. | x = y = 0; x is y -> True  
**is not** | Object non-identity test. Determines whether two variables point to different objects.  
| x = y = 0; x is not y -> False; x = 0; y = 1; print(x is not 1) -> True  
  


**5\. NATIVE FUNCTIONS/METHODS** (To be complemented; [source](https://docs.python.org/3/library/functions.html). Examples were tested using IDLE or with IDLE's Editor. In the latter, displaying of results was done with print().)

**Função** |  **Significado** |  **Exemplos**  
---|---|---  
abs() |  Modulus, also of a complex number |  abs(-1) -> 1; abs (2) -> 2; abs((1+2j)) -> 2.23606797749979  
S.add(x) | Inserts x into the S set | S = {1, 2, 'four'}; S.add('three'); S -> {1, 2, 'three', 'four'}  
Apparently, sets are displayed in alphabetic order  
aiter() | Creates an asynchronous iterable. Used in asynchronous programs (permits concurrent execution, without waiting for completion of operations. A normal program is synchronous, one operation executed at each time, sequentially | Requires the import of specific modules, such as asyncio for input/output. [See examples](https://diveintopython.org/functions/built-in/aiter).  
all(x) |  Returns True if all elements of iterable (cf. 2.10) x have value True or x is empty, and False if any element of x has value False |  a = [True, True, True]; b = [True, True, False]; c = []; all(a), all(b), all(c) -> (True, False, True)  
anext() | Used in an asynchrohous program (see aiter()). Permits access to the next item of an ansynchrohous iterable. | Part of asyncio. [See example](https://diveintopython.org/functions/built-in/aiter).  
any(x) |  Returns True if any element of the iterable x is true, and False if no element of x is True, or x is empty. |  a = [True, True, True]; b = [True, True, False]; c = []; any(a), any(b), any(c) ? (True, True, False)  
ascii(x) | Returns x as a string, skipping characters that are not of type ASCII {EF} | numb = 123; list = [1, 2, "Olá"]; tuple = ("a", "b", "c")  
print(ascii(numb), ascii(list), ascii(tuple)) ->  
123 [1, 2, 'Ol\xe1'] ('a', 'b', 'c')   
breakpoint() | Ativa o depurador (_debugger_) pdb, dando os valores das variáveis e expressões naquele ponto  | a = 2; b = 3  
**if** (a+b == 5):  
  breakpoint()  
  print('soma é 5') ->  
print('soma é 5); (Pdb) +a; 2; (Pdb) +b; (Pdb) +b; 3; (Pdb) a+b; (Pdb) +a+b; 5; (Pdb)  
bin() |  Converts an int to bynary |  bin(B) -> '0b10'; bin(20) -> '0b10100'   
x.bit_length() | Significant bit length of binary x (left 0s are ignored) | 0b101010.bit_length() -> 6; 0b001010.bit_length() -> 4   
bool(x) |  Returns True if the argumenthas value True, False if it has value False or it is empty |  bool(B>A) -> True; bool(C>D) -> False; bool() -> False  
bytearray(x) |  Returns a bytearray object which is an array of the bytes in the iterable (cf. 2.10) x |  numbers = [2, 3, 11, 30]; byte = bytearray(numbers); print(byte) -> bytearray(b'\x02\x03\x0b\x1e')  
bytes(x,c,er) | The same as bytearraym but the result is an object that cannot be modified. | x = bytes(5); print(x) -> b'\x00\x00\x00\x00\x00'  
bytearray(x,c,er) |  Returns a bytearray object which is an array of the bytes in the iterable (cf. 2.10) x using code type; the default is utf-8 in hexadecimal; er is a message string issued if a character in x is not encodable |  numbers = [2, 3, 11, 30]; byte = bytearray(numbers); print(byte) -> bytearray(b'\x02\x03\x0b\x1e')  
callable(x) |  Returns True if x is a callable function or method, False otherwise |  x = 10; print(callable(x)) -> False  
def func(x): return (x); y = func; print(callable(y)) -> True  
chr(x) |  Character corresponding to the ASCII code of the argument (between 0 and 255) |  chr(97) -> 'a'; chr(150) &rarr ? [the character was not found]  
  
classmethod() |  Permits directly calling a method of a classe, without having to instantiate the class {EF} |  **class** CM:  
  a = 0  
  **def** shows_a(cls, x):  
     cls.a = x  
     print('"a" value:', cls.a)  
CM.mostra_a = classmethod(CM.shows_a); CM.shows_a(123) ->  
"a" value: 123  
x.clear() | Removes all elements from the iterable (cf. 2.10) x | x = {1, 2, 'três'}; x.clear(); x -> set() [indica conjunto vazio ou [] se for cadeia]  
compile(s,file,mo) |  Permits compiling and executing an object (e.g. a string), returning the result if the mode mo is 'exec', or 'eval' if s is an expression, or 'single" if s is an iterable object; file obtains s form a file {EF} |  string = 'a=8;b=7;soma=a+b\nprint(soma)' # a=8;b=7;print(a+b)  
ref = compile(string, ' ', 'exec'); exec(ref) -> 15  
complex(re,im) |  Converts to a complex with real part re and imag. im |  complex(1) -> (1+0j); complex(2,5) -> (2+5j)  
x.conjugate() | Gives the conjugate of the complex x  | x = (1+2j); x.conjugate() -> (1-2j) [Not working on 3.13.1]  
delattr(cl,attr) |  Deletes atribute attr from class cl {EF} |  **class** A:  
  x = 10; y = 20  
inst = A(); print(inst.x, inst.y); delattr(A, 'x'); print(inst.x) ->  
10 20  
AttributeError: 'A' object has no attribute 'x'  
dict() |  Creates a dictionary {EF} |     
dir() | Lists the names of all session variables {EF} |  n = [10]; print(dir()) -> [..., n]  
x.discard(y) | Removes element y from the set x, if y is in x; does nothing if y is not in x. | x = {1, 2, 'three'}; x.discard('three'); x -> {1, 2}   
divmod(x,y) |  Gives the ordinate duble (x // y, x % y) |  divmod (C,B) -> (1,1) divmod (C,D) -> (2.0, 0.6000000000000001)  
x.encode(c) | Encodes x using the encoding type c, utf-8 is the default |    
enumerate(x) |  Returns iterable x enumerating each of its elements |  lis = ['a', 'b', 'c']; print(list(enumerate(lis))) -> [(0, 'a'), (1, 'b'), (2, 'c')]  
eval(x) |  Runs the string x and returns its value. x maybe te result of input(). x cannot be a compound statement.  |  eval('2*3') -> 6 eval("'abc'[1]") -> 'b'  
exec('c',gl,loc) | Immediately executs code c; gl and loc are dictionaries allowing for the specification of global and local variables to be used, guaranteeing safety |  exec('print("The sum of 5 and 10 is", (5+10))') &rarr The sum of 5 and 10 is 15  
exec('x = 10\ny = 20\nprint("Sum:", x + y)') -> Sum: 30  
Instead of \n (indicates new line of code) one may use ;  
exit() | Ends execution of the program.  | Requires sys module, incorporated with **import** sys. Usage: sys.exit()  
filter(f, L) |  Apply the function f to each element of the iterable L, and results in the elements of L for which f is True |  See example in section "Lambda notation"  
float(x) |  Converts x to float |  float(B) -> 2.0;   
float.as_integer_ratio() | Returns a pair of integers whose ratio is the argument  | float.as_integer_ratio(1.5) -> (3,2)  
float.is_integer() | Returns **True** if the argument is integer, **False** otherwise  | float.is_integer(1.5) -> False; float.is_integer(3.0) -> True  
format(x,f) |  Returns the value of x in the format f. See the large [types of formats](https://www.w3schools.com/python/ref_func_format.asp) {EF} |  a = 123; print(format(a, 'x')); print(format(a, 'b')) -> 7b 1111011  
Obs.: 'x' stands for hexa   
frozenset() |  Builds a set that cannot be changed |  x = frozenset({1, 2}); x -> {1, 2}; x.pop() gives an error message  
getattr(obj,attr,defa) |  Returns the value of an attribute attr of object obj. If the attribut does not exist in obj, returns default defa |  **class** Cla:  
  **def** __init__(self, X, Y):  
     self.X = X  
     self.Y = Y  
cla1 = Cla(13, 'abc') #Creates an instantiation  
cla2 = Cla(15, 'def'); print(getattr(cla1, 'X', getattr(cla2, 'Y')) &rarr  
13 def  
globals() |  Returns a dictionary with names and values of all global variables {EF} |  a = 1; b = 2; print(globals()) &rarr {..., 'a': 1, 'b': 2}  
hasattr(clobj,attr) |  Returns True if the class or object clobj has attribute attr {EF} |  **class** A:  
   a = 123  
print(hasattr(A, "a")); print(hasattr(A, "b")) &rarr True False   
hash(x) |  Retorna a unique integer representing x, which can only be a string, a number or a tuple. The result may vary depending on the session. |  hash('Python') -> 402769285147184097 hash((1,2,3)) -> 529344067295497451  
help() |  In interactive mode (IDLE, W3 compiler, see section 1-3), gives documentation of the argument |  help(int)  
hex() |  Converts an int to a hexadecimal |  hex (8) -> '0x8'; hex (50) -> '0x32'; hex(C) -> '0x3'  
id(x) |  When an object x is created, a unique number (address) is associated to it; id returns this number {EF} |  a = 5; b = 6; c = a + b; print('a', id(a), 'b' id(b), 'c' id(c)) ->  
a 140720283321384 b 140720283321416 c 140720283321576  
__import__() |  Import of modules. Same as the **import** command. |  See <https://docs.python.org/3/library/importlib.html>  
input("mensagem") |  Waits for the user to enter input, followed by Enter. Returns the input data in the form of a string; may display a message when running. Did not work on W3 on-line compiler. |  day=input('Enter the value of the day:'); -> "Enter the value of the day" 20 **Enter** dia -> '20' (as a _string_);  
to use in calculation day_int=int(input('Enter...')) or dayint=int(day); dayint -> 20  
int() |  Converts to int |  int(D) -> 1; int('123') -> 123  
x.isdisjoint(y) | **True** if the set x is disjoint from the set y, **False** otherwise  | {1, 2, 'três'}.isdisjoint({4, 'cinco'}) -> True  
{1, 2, 'três'}.isdisjoint({2, 'cinco'}) -> False  
isinstance(clobj,t) |  Returns True if the class or object of clobj is of the same type as t; if t is a tuple, returns True if obj is of any of the types of t {EF} |  print (isinstance("Hello", (float, int, str, list, dict, tuple))) -> True  
issubclass(c1,c2) |  Returns true if class c1 is a subclass of class c2, False otherwise {EF} |  **class** A:  
  a = 1  
**class** B(A):  
  b = 2; print(A.a, b)  
print(issubclass(B,A)) ->  
1 2  
True   
iter(x) |  Returns an index to the elements of iterable x {EF} |  x = iter(["a", "b", "c"])  
print(next(x),next(x),next(x)) -> a b c  
s.join(x) | Method in class string. Concatenates the parts of the iterable x, separating them with the string s. | S = ','.join(['a', 'b', 'c']); S -> 'a,b,c'  
len(x) |  Returns the number of elements in iterable (cf. 2.10) x  |  len(G) -> 3; len((1,2,3,4)) -> 4; len((A,B,G)) -> 3; len([1,B,5,7]) -> 4  
len({1, 2, 'three'}) -> 3  
list() |  Converts the elements of an iterable into a list; without argument gives the empty list |  list(G) -> ['a', 'b', 'c']; list((1, 2, 3)) -> [1, 2, 3]; list({1,2,3}) -> [1, 2, 3]   
locals() |  Returns a dictionary with names and values of local variables of a function or program |  **def** f(x):  
  x = 10  
  print(locals())  
  **return**(x+3)  
print(f(20)) ->  
{'x': 10}  
13  
lower() | Converts letters in a string to lowercase  | 'BLAH3#'.lower() -> 'blah3#'; name = input('Enter your name:').lower(); print(name)  
map(f,L) |  Applies the function f to each element of one or more iterables (cf. 2.10) L |  list (map (abs, [2,-3,4,-5])) -> [2, 3, 4, 5]   
max(x) |  Returns the largest of the elements of the argumentor iterable x |  max (1,2,3) -> 3; max (['a', 'b', 'c']) -> 'c'; max ('a', 'aa', 'aaa') -> aaa;   
max (G) -> 'c'  
memoryview(x) |  Returns an object with the internal representation of x {EF} |  a = bytearray('ABC', 'utf-8'); m = memoryview(a); print(list(m[1:3])) ->  
[66, 67]   
min() |  As max, but for the least element |  min (1,2,3) -> 1; min (['a', 'b', 'c']) -> 'a'; min ('a', 'aa', 'aaa') -> a;   
min (G) -> 'a'  
next(x) |  Returns the next value of iterable (cf. 2.10) x {EF} |  a = [5, 6, 7]; b = iter(a); print(next(b), next(b)) -> 5 6  
object() |  Returns the class that is the base of all classes; it is not possicle to define attributes to it, but it contains all attributes common to all classes. e.g __init__, __strint__, etc. {EF} |  obj = object(); print(dir(obj)) ->  
['__class__', '__delattr__', '__dir__', '__doc__', ...]  
oct() |  Converts to octal |  oct(15) -> '0o17'  
open(fi,m) |  Opens file with path and name fi in mode m, as an object. m may be r (reading only), w (writing, creates arq if non existent), a (appends a string to arq, creats if non existent, ), x (creates fi, error if it exists), b (binary file, e.g. with image), t (text file, standard). arq becomes a class with attributes. |  f = open('name', 'w'); f.write('Text'); f = open('name', 'r')   
print(f.read()); f.close() ->  
Text  
ord() |  Contrary to chr |  ord ('a') -> 97  
x.pop() | Removes the last element of the iterable (cf. 2.10) x | x = {1, 2, 'três'}; x.pop(); x -> {1, 2}  
pow(x.y) |  Equivalente a x**y |  pow(2,3) -> 8; pow(4,0.5) -> 2.0; pow (4,-2) -> 0.625  
print() |  Data output. x may contain various objects and expressions, separated by commas, as well as strings to be exhibited as constants, and line control parameters (\\...) |  print(A,D) -> 1 1.2; print ('A =',A) -> A = 1; print ('A*3 =',A*3,'\nD =',D) ->   
A*3 = 3  
D = 1.2  
property(cl) |  Used inside a class cl, permits altering the values of attributes of cl {EF} |  See examples [here](https://www.geeksforgeeks.org/python-property-function/)  
random |  A class. Requires importing the random module. Some functions of this class:  
1\. random.randint(a,b) returns pseudo-random integer between a and b inclusive.  
2\. random.random() gives the next random floating point between 0.0 and 1.0  
3\. random.uniform(a, b) ditto between a and b inclusive  
4\. random.choice(x) randomly returns an element from the non-empty list x  
5 . random.shuffle(x) sorts the list x randomly | The results obtained with IDLE may be different, depending on the "seed":  
  
1\. import random; random.randint(10, 100) -> 12; random.randint(10, 100) -> 67  
2\. random.random() -> 0.05462293624556047; random.random() -> 0.36903357168070205  
3\. random.uniform(2,5) -> 3.983840861586745  
4\. random.choice([1,2,3,4,5])) -> 3; random.choice([1,2,3,4,5])) -> 4   
5\. x=[1,2,3,4]; random.shuffle(x); x -> [3, 1, 4, 2]; random.shuffle(x); x -> [4, 1, 2, 3]  
range()  
range(first,end,step)  |  Creates a virtual list, to be used in a **for** statement. first indicates the order of the first element, end the order of the last, and step (if omitted, it is 1) the increments in the order. |  range(C): equivalent to [0, 1, 2]; range(1, 5) to [1, 2, 3, 4, 5];   
range(0, 10, 3) to [0, 3, 6, 9]; range(0, -4, -1) to [0, -1, -2, -3]  
reduce(fu,li) |  This function is part of the module "operator". It applies the funcion fu to all elements of list li. It requires loading the module "functools", allowing operators (sections 3 and 4 above) to be specified as functions. Another possibility is using the lambda notation (section 10) defining a function with an operator. |  **import** functools  
**mport** operator #see operators in <https://docs.python.org/3/library/operator.html>  
lis = [1,3,5]; functools.reduce(operator.add, lis) ->  
9  
  
functools.reduce(lambda x, y: x+y, lis) #extends the + to all list members   
9   
reload() |  Reloads a function x defined in a present module |     
repr(x) |  Returns the value of x in the form of a string. x may be a class object, recriating it. Useful for debuggin. (Look for examples with class objects.) | x = "abc"; y= [1, 2, 3]; print(repr(x, repr(z)) -> ("'abc'", '[1, 2, 3]')  
reversed(x) | Returns iterable (cf. 2.10) x in its reverse order. Not applicable to sets {EF} | print(list((reversed('abc')))); print(list((reversed(('d','e','f'))))) ->   
['c', 'b', 'a'] ['f', 'e', 'd']  
round(x,n) |  x rounded to the nth decimal place; without n rounds to the integer |  round(3.5566,3) -> 3.557; round(4.5555,3) -> 4.555;  
round(3.5555) -> 4; round(3.4555) -> 3  
s.rstrip(c) |  As lstrip, deletes string c to the left of string s |  print("example!!!".rstrip("!"), "example!!! ".rstrip("!")) -> exemple exemple!!! {EF}  
set(x) |  Converts iterable (cf. 2.10) x to a set; if x is empty, creates the empty set |  set([1, 2, 'three']) -> {1, 2, 'three'}; set() -> set()  
setattr(clobj,'attr',val) |  Assigns value val to the string attribute attr of class or object clobj {EF}  |  **class** Person:  
  name = 'Eva'; age = 36  
setattr(Person, 'age', 25); print(Person.age) &rarr  
25   
  
slice(start,end,step) |  Defines indeces of an iterable (cf. 2.10) x to be used later on with the iterable to extract part of itl; start, end step as in funtion range() |  T= ("a", "b", "c", "d", "e", "f"); y = slice(2); T[y] -> ('a', 'b')  
z = slice(3, 5); T[z] -> ('d', 'f')  
str = 'abcdefghi'; t = slice(5, 7); str[t]; -> 'fgh'  
staticmethod(cl,m) |  Converts method m of class cl into a static method, which can be used wothout having to instantiate cl into an object {EF} |  **class** Cl:  
  **def** ad(a,b):  
  **    return** a + b   
Cl.ad = staticmethod(Cl.ad)  
print(Cl.ad(5,7)) #Ativação da função ad sem criar um objeto de Cl &rarr  
12  
str(x) |  Converts int or float x to string |  str(C) -> '3'; str(D) -> '1.2'  
sum() |  Sums the elements of an iterable (cf. 2.10)  |  sum([A,B,C, 4, D]) -> 11.2; sum((1,2,3)) -> 6; sum ({1, 2, 3}) -> 6  
super() |  Permits that a child class C2 which inherits the properties of a parent class C1 uses the attributes of C1 |  **class** C1: #Example taken from W3 Schools  
  **def** __init__(self, txt):  
    self.message = txt  
  **def** printmessage(self):  
    print(self.message)  
**class** C2(Parent):  
  def __init__(self, txt):  
    super().__init__(txt)  
x = C2(Hello!"); x.printmessage() -> Hello!  
time.sleep(n) | Interrupts the execution of a program for _n_ seconds. Requires loading the time module: **import** time  
| **import** time; print(10); time.sleep(5); print(20) -> 10 [pause] 20  
[Does not work on the W3 on-line compiler; works in IDLE]  
tuple() |  Converts an iterable (cf. 2.10) to a tuple |  tuple('abc') -> ('a', 'b', 'c'); tuple([1, 2, 3]) -> (1, 2, 3);   
tuple({1,2,3}) -> (1, 2, 3)  
type() |  If the argument is a variable,returns its type; if it is an object, its type |  type (A) -> <class 'int'>; type (D) -> <class 'float'>; type (G) -> <class 'str'>  
upper() | Converts letters in a string to upper case | 'bla3#'.upper() -> 'BLA3#'  
vars(obj) |  Returns the __dict__ attribute of object obj. Pemits seeing the attributes in a dictionary form. Other atributes used by the system also appear. |  **class** Ex:  
  X = "abc"  
  Y = 12  
atrs = vars(Ex)  
{'X':"abc", 'Y':12}  
zip(x) |  x must be a number of parallel iterables, in principle with the same number of elements in each iterable. The result will be doubles, triples, etc., by joining corresponding elements of the iterables. It is as if transforming rows into columns. |  **for** I **in** zip([1, 2, 3], ['a', 'b', 'c']):  
  print(I) ->  
(1, 'a')  
(2, 'b')  
(3, 'c')  
  
### 6\. SOME MATHEMATICAL FUNCTIONS AND CONSTANTSS

To use these functions, it is necessary to execute the **import** math command in IDLE or the W3 School on-line compiler, or insert it into a program, which activates the math module. Functions must be preceded by math, e.g. math.sqrt(4), math.e etc; results are always of type float, unless otherwise noted. For calculations with complex numbers, **import** cmath .  


**Function** |  **Meaning** |  **Examples**  
---|---|---  
atan(x) | Arctangent, x and result in radians | math.atan(2) -> 1.1071487177940904;   
ceil(x) | The less integer >= x | math.ceil(4.7) -> 5  
cos(x) | Cosine, x and result in radians |  math.cos(math.pi/2) -> 6.123233995736766e-17 [should be zero; due to approximation of pi]; math.cos(math.pi) -> -1.0  
degrees(x) | Convert x in degrees to radians | math.degrees(math.pi) -> 180.0  
e | The constant e | math.e -> 2.718281828459045  
exp(x) | e**x | math.exp(1) -> 2.718281828459045; math.exp(2) -> 7.38905609893065   
factorial(x) | Factorial of x of type int, result in int | math.factorial(5) -> 120  
floor(x) | Bigger int <= x | math.floor(4.7) -> 4  
fsum | Summation | Like sum() of the Native Functions section, but with rounding-off   
inf | The constant infinite (biggest representable float) | math.inf -> inf  
log(x, b) | Logarithm of x to the base b (optional); without base gives the log in base _e_ | math.log(10) -> 2.302585092994046; math.log(100,10) -> 2.0  
log10() | Logarithm in base 10 | math.log10(100) -> 2.0; em geral mais precisa que math.log(x,10)  
log2() | Logarithm in base 2 | math.log2(8) -> 3.0  
modf(x) | Returns in float the decimal and integer parts of x  | math.modf(1.25) -> (0.25, 1.0)  
pi | The number pi | math.pi -> 3.141592653589793 (see examples in, cos and tan)  
radians(x) | Converts x in radians to degrees | math.radians(180) -> 3.141592653589793  
sin(x) | Sin, x and result in radians | math.sin(math.pi/2) -> 1.0; math.sin(math.pi) -> 1.2246467991473532e-16 (devia ser zero; não é devido à aproximação)   
sqrt() | Square root | math.sqrt(4) -> 2.0; math.sqrt(5.6) -> 2.3664319132398464  
tan(x) | Tangent, x in radianos |  math.tan(math.pi) -> 1.2246467991473532e-16 (devia ser zero);  
math.tan(math.pi/2) -> 1.633123935319537e+16 (representação do infinito)  
trunc(x) | Integer part of x | math.trunc(3.5) -> 3  
  
### 7\. LIST FUNCTIONS/METHODS

**Functions** |  **Results** |  **Examples**  
---|---|---  
append() |  Adds an element at the end of the list | L=[1, 2, 3, 4]; L=L+[5] -> [1, 2, 3, 4, 5]; L=L+'#' -> [1, 2, 3, 4, 5, '#']  
clear() | Clears string or set | L = [1, 2, 'three']; L.clear(); print('d',x) -> []  
L= {1, 2, 'three}; L.clear(); print('c',x); -> set();   
copy() |  Returns a copy of the list as a new object | L = [1, 2, 'three']; Lnew= L.copy(); print(Lnew) -> [1, 2, 'three']  
count(v) |  Returns the number of elements with value v |  L=[1, 2, 3, 2, 4, 2]; Conta_L = L.count(2); print(Conta_L) -> 3  
text = "Hello, world! Hello, everyone!"; count_hello = text.count("Hello"); print(count_hello)  
-> 2   
extend(s) | Add the elements s of a list (or any iterable), to the end of the list | L=[1,2,3,4]; L.extend([5,6]); print(L) &rar;r [1, 2, 3, 4, 5, 6]  
index(v,s,e) |  Returns the índex of the first element com o valor v starting at s and endint at e  
| L = [1,2,'three']; i1 = L.index(1); i2 = L.index('three'); print(i1,i2) -> 0 2  
L = [1, 2, 3, 4, 1, 1, 1, 4, 5]; i1 = L.index(1, 4, 8); i2= L.index(1, 2, 8); print(i1,i2) -> 4 4  
L.insert(p,e) |  Adds an element e at position p of list L | L = [1, 2, 3, 4]; L.insert(2, 10); print(L) -> [1, 2, 10, 3, 4]  
lstrip() | Removes blank spaces or specified characters at the begining of a string | Same as strip(), but from the begining  
pop(e,p) | Removes the element e at position p; if p is not given, removes the last element in the list | L = [1, 2, 3, 2, 4]; L.pop(3); print(L) -> [1, 2, 3, 4]; print(L.pop()); -> [1, 2, 3]  
pop() may be used to pop-up the topmost element of a stack  
remove() | Removes the first item with the specified value |  L = [1, 2, 3, 2, 2]; L.remove(2); print(L) -> [1, 3, 2, 2]  
L = ['a', 'b', 'c', 'b', 'b']; L.remove('b'); print(L) -> ['a', 'c', 'b', 'b']  
replace('a','b') | Replace ocurrences of 'a' by 'b' | OLA = 'He?llo, g?oo?d mot?ning!?!'; OLALimpo = OLA.replace('?', '')  
print(OLALimpo) -> Hello, good morning!!  
reverse() | Reverses the order of the list | L = [1, 2, 3, 4]; L.reverse(); print(L) -> [4, 3, 2, 1]  
sort() | Sorts the list | L = [1, 3, 4, 2]; L.sort(); print(L) -> [1, 2, 3, 4]  
s.split(sep) | Method of class string. Generates a list with the elements of string s separated by the string sep; if sep is omitted, it uses blank space as separator | s='a,b,3'; s.split(') -> ['a', 'b', '3']; s='x#y#z'; s.split('#') -> ['x', 'y', 'z']  
strip() | Removes blank spaces os specified characters at the beginning and end of a string | OLA = " Hello, good morning!!"; OLALimpo = OLA.strip(); print(OLALimpo) -> Hello, good morning!!!!  
OLA = ",,##?? Hello, good morning!!,,##?? "; OLALimpo = OLA.strip(',#? '); print(OLALimpo) ->  
Hello, good morning!! [The blank at the end of the string is essential; stops stripping characters from both end once it encounters a character that is not in the specified characters.]  
rstrip() | Removes blank spaces os specified characters at the end of a string | Same as strip(), but from the end  
translate() | Remove a sbustring using None | OLA = 'He?llo, g?o?od mor?ning!?!'; OLALimpo = OLA.translate({ord('?'): None});  
print (OLALimpo) -> Hello, good morning!!  
  


**8\. PRECEDENCE (EXECUTION ORDER)**

**Order** |  **Operator/function** |  **Examples**  
---|---|---  
1 | ( ... ) | (... ignored by the interpreter {EF})  
2 | function() | abs(-5)+2 -> 7  
3 | unary + and - | -5-2 -> -7; -(+5-2) -> -3  
4 | *, /, % and// |    
5 | binary + e - (addition and subtraction) |    
6 | & ("and", bit bybit) |    
7 | | and ^  |    
8 | <=, <, >, >= |    
9 | =, %=, /=, //= e –=  |    
10 | +=, *= e **= |    
11 | **in** , **not in** |    
12 | **not** , **or** , **and** |    
  
### **9\. FUNCTION DECLARATION AND USAGE  
**

The following examples were tested usind IDLE 3.13.1 with its prompt >>>.  
In a program sequence, the declaration of a function must always come before its activation. A fuction is declared with its _parameters_ , and is called (activated) with _arguments_.  
  
**Syntax** |  **Examples on IDLE**  
---|---  
# Declaration (attention to vertical alignment)  
  
**def  **function-name (parameter_1 , ..., parameter_n ):  
   statement_1  
   ...  
  statement_n  
next-command  
# Activation  
function-name (argument- 1 , ..., argument- m ) |  >>> **def**  sum(a,b): # declaration  
        **return** a+b #Hit enter  
... #Hit Enter, producing a blank line  
...   
>>> sum(1,2) # activation  
3  
>>> sum(A*3,D)   
4.2 When typing in IDLE, it is necessary to insert a blank line to end a function declaration (about IDLE, see section 16 below).  
  
In a program sequence, the declaration of a function must always come before its activation.  


### **10\. LAMBDA NOTATION**

This notation allows for the declaration of a function without giving it a name, placing it anywhere a function can be called.  


**Syntax** |  **Examples on IDLE**  
---|---  
**lambda** paramenter_list: functon of these paramenters |  >>> y = lambda x: x**2 #Hit Enter  
>>> y(8)  
64 >>> min = lambda x,y: x if x < y else y  
>>> min (3,2)   
2 >>> items = [1, 2, 3, 4, 5];  
>>> list(map(lambda x: x**2, items)  
[1, 4, 9, 16, 25] >>> number_list = range(-5, 10)  
>>> list(filter(lambda x: x < 0, number_list))  
-> [-5, -4, -3, -2, -1]  
  
### **11\. GLOBAl E LOCAL IDENTIFIERS**

An identifier declared within a function is only local to it (valid within it); declared outside the function, before or ater it in a scope (i.e., validity space) directly encompassing the function, it is global, it can be used both outside and inside the function. Using a local identifier avoids many errors, as only the function where it is declared can modify its value; this identifier has been "encapsulated" into the function. In this sense, the correct thing to do is to pass argument values to the function and obtain them from it through parameters in its declaration (arguments in its activation).

  >>> **def** F():  
        Loc = 1 # local a F  
        print (Loc, Glob)  
>>> Glob = 2 # global to F  
>>> F() ->  
1 2  
>>> Loc  
Loc  
NameError: name 'Loc' is not defined |  Converting a local identifier into a global: >>> **def** F():  
...   **global** Glob  
...   print (Glob)  
...  
...   
>>> Glob=1  
>>> F()  
1  
---|---  
  
An F2 function can be declared inside another F1 function. In this case, F2 becomes local to F1 and cannot be activated outside of F1:  


>>> **def** F1():  
...   **def** F2(): #Local to F1  
...     LocF2 = 13  
...     print (LocF2)  
...   F2() # Activated inside F1  
...  
...  
>>> F1()  
13  | >>> **def** F1():  
...   **def** F2(): #Local to F1!   
...     LocF2 = 13  
...     print (LocF2)  
>>> F2()  
F2()  
NameError: name 'F2' is not defined  
---|---  
  
If function F2 is declared inside F1, the **nonlocal** declaration causes a variable V declared in F2 to become the scope of F1, but is not valid outside of F1. V must have a value assigned to it in F1 before the nonlocal declaration:

>>> **def** F1():  
       LocF1 = 13 # Local a F1 necessária!  
       print ("Na F1:", LocF1)   
       **def** F2():  
          **nonlocal** LocF1 # Global a F2  
          LocF1 = "26"  
          print ("Passou pela F2:", LocF1)  
       F2() # Na F2        
...  
...   
>>> F1()  
Na F1: 13  
Passou pela F2: 26  
>>> F1();  
In F1: 1  
In F2: LocF2 | >>> def F1():  
>>>   def F2():  
>>>     Local =1  
>>>     print(Local)  
...  
...   
>>> F2  
NameError: name 'F2' is not defined  
---|---  
  
### **12\. CLASSES**

**12.1 Introduction**

Classes can be conceptually viewed as an extension of types and functions, and are used to achieve further encapsulation. Unlike functions, classes do not contain parameters in the declaration of their name; to be used with arguments in their activation ("calling"), the latter have to be declared in the class body as a first attribute; one can change the name of the class, but the common use is to call it "self" (see example below). The native function __initi__() declares the initial attributes of the class, and is activated every time an object is created for that class (see below). In its body, a class can contain variable and function declarations, which become local to them. Each element declared in a class is called an "attribute" or, more generally, "property", thus encompassing functions. A property is declared using the class name, a period, and the attribute or property name. Like functions, classes must be defined before they can be used. A functions declared within a class is called _a method_. One can assign values to elements of a class outside of it. A class can be assigned to a variable V; in this case V receives an _instance_ of the class, an _object_ , with all the properties of the class. One may declare any number of objects. A class C2 can be declared as a subclass of a class C1. In this case, C2 "inherits" all properties of C1, but it may have its own, local properties, inacessible by C1. A class can be created dynamically using the function type(N,B,dic), where N will be the name of the class, B a tuple which works as a base class, from which the created class N inherits the attributes (i.e., N will be a subclass of B), and dic is a dictionary containing the names of the attributes and values that N will contain (see example below). To eliminate an object p, use **del** p. Se other functions applied to classes in section 5 above. 

**12.2 Polymorphism  
****  
**_Polymorphism_ is the ability of the same operator, function, or object of a class to operate with arguments of different types. For example, the operator + can indicate the sum of integers, the concatenation of strings or tuples, etc. The function len(x) accepts, as the argument x, strings (giving the number of characters), or a list, tuple or set (giving their number of elements). All of this is predefined. The polymorphism of functions or methods of classes is something defined by the programmer. The same function f can occur in different classes. In this case, f can be applied to several instances (objects) of these classes, as exemplified below. This helps to implement and use a personal "program library" – there are already those of available modules and of many contributors, permitting the reutilization of parts of programs.

class C:  
   """This is a class."""  
   #Implicit attribute for documentation:__doc__  
       X = 13  
       **def** FdeC (Y):  
          **return** Y + 1  
print(C.X)  
13  
print(C.FdeC(2))  
3   
print(C.__doc__) #Docummentation at the header of C  
' This is a class '  
ObjC = C # Instantiation: creating an object  
print(ObjC.X)  
13 |  # Dynamic creation of a new class C2  
  
C2 = type('C2', (object,), {'attr': 100})  
inst = C2()# Creation of an object, an instance of C2  
print(nst.attr)->  
100 If C2 is declared as a subclass of a class C1, use C1 instead of "object"; C2 inherits all attributes of C1  
---|---  
**class** person:  
  **def** __init__(self, name, age) #Parameters name, age  
    self.name = name #self einstead the classe name  
    self.age = age  
p1 = person('Val',84) #Declaration of objeto p1, use of arguments  
print(p1.name, p1.age) &rarr;  
Val 84  | class Person:  
  Age = 84  
p1 = Person # Creation of object p1  
print(p1.Age)   
p1.Age = 48 # Modifying the value of object attribute  
print(p1.Age) &rarr;  
84  
48   
  
**12.3 Inheritance**

The concept of inheritance is quite old in programming languages. It emerged with the Algol language, which had its final definition in 1960, with Agol-60. In this language, a block was declared with commands between begin ... end. It was possible to declare a block B2 inside a block B1. In this case, all variables and procedures (called "functions" in the later C language) declared in B1 were accessible in B2 (called _global_ to B2), but those declared in B2 were not accessible inside B1 (they were _local_ to B2). It was conventional to say that B2 _inherited_ the properties declared in B1. In Algol, a special function was a type of procedure that returned a value, like a function in Python. In the C language, it was not possible to declare a function inside another: all functions had only one lexical level (the outermost), which was imposed by questions of efficency f the machine (PDP-11) for which the language was developed. That is, instead of changing the structure of the machine, programming was distorted. Python allows one to declare a function F2 inside another F1, which is called _nested function_ s; all the variables and functions ("properties") declared in F1 are available inside F2 (global to F2). The term _inheritance_ of F2 in relation to F1 was established, that is, F2 inherits the attributes and functions declared in F1, which are global to F2, and those declared in F2, which are not available in F2 outside F1, that is, are local to F1. The properties of F1 have a _scope_ that encompasses the whole of F2; the scope of the properties of F2 only has the scope of F2 (see diagram below).

The notion of inheritance also applies to classes: it is possible to declare a class C2 as being a _subclass_ of another _superclass_ C1. The C++ language introduced the notion of classes in C, and since in C there was no function declaration within a function, this syntax was passed on to C++ in relation to classes. Python preserved this structure. In order for C2 to inherit all the properties of C1, it is necessary to declare them as in the following schema:

**def** F1():  
  # propriedades próprias de F1; as de F2 não estão disponíveis  
  **def** F2():  
    # propriedades próprias de F2; as de F1 estão disponíveis | **class** C1: # Superclasse de C2  
  # propriedades próprias de C1; as de C2 não estão disponíveis  
**class** C2(C1): # Subclasse de C1  
  # propriedades próprias de C2; as de C1 estão disponíveis  
---|---  
  
The notion of inheritance is very useful, because in the example, the class C2 can be declared without its own attributes being changed outside of it. This facilitates encapsulation, that is, isolation from external influences. [See examples](https://www.geeksforgeeks.org/inheritance-in-python/). 

Finally, a philosophical observation: the notion of inheritance is yet another misnomer in computing, which is full of misleading anthropomorphisms: minerals and plants do not inherit; only animals and human beings inherit. Machines are on a lower level than minerals.

### **13\. SIMPLE AND COMPOUND STATEMENTS**

**Syntax** |  **Examples** (testados no Azure, V. Ambientes abaixo)  
---|---  
**13.1 Block of statements** All in the same line: Statement; Statement;... ; Statement; Multiple lines. Have to be vertically aligned to the left margin or a column, if the block is immersed in some statement: Statement  
Statement  
...  
Statement |    
  
J = 2; K = 3; M = 4; J,K,M -> (2,3,4)  
  
J=2  
K=3  
M=4  
J,K,M -> (2,3,4)  
  
**13.2 if** \- Logical choice statement  # Attention to the vertical alignement  
**if****** Logical expression:  
 Block # Begining in any column except below the i of if.  
**elif** Logical expression**:** # Optional,  
 # aligned at the same column as the **if**  
 Block # Starting at any column to the   # right of the beginning of elif  
**elif** Logical expression # Idem  
 Block # Idem  
   _...  
_**elif** Logical expression: # Idem  
 Block __ # Idem _  
_**else** : """Idem. Optional. In IDLE, the **else** aligned with the 1st column of the if; follows a single Command or a block with several aligned lines starting at least in the 2nd column in relation to the else"""  
Next-Command # Aligned with the **if** column |  J = 2; K = 3; L= 4 # válido para todos os exemplos seguintes  
---|---  
**if** J < K: print(J); print(K)->   
2  
3  **if** K > J : """ O ":" pode estar em   
   qualquer coluna desta linha """  
   N = J+3  
P = K+4  
N, P -> (5,7)  {PC} corrected (5, 7) **if** K < J: N=5  
**else:** N=6  
P=8  
N, P -> (6,8) |  **if** K < J:  N=5  
**elif** L > K: N=6  
P=9  
N, P -> (6,9)   
**if** K < J: N=5  
**elif** L < : N=6;  
**elif** J > K:   
   N=7  
**else** : N=8  
N**** -> 8   
  
**13.3 while** statement for repeating the execution (loop) of a statement or block of statements **while** Logical Expression: # a single statement; or   a block of statements aligned vertically to the   right of the w  
**else** : statement #or a block of statements  
next command #aligned with the first e of **else** The **else** command is executed when the Logical Expression results is False  
The **break** statement interrupts the execution of the repetition loop and jumps to the next command after the **while** with its block. It is convenient to use it when an exception situation occurs during the execution of the loop.  
Within the block of statrements, it may occur an  
**if** Logical Expression:  
  **continue**  
If Logical Expression is true, it skips the remainder of the current iteration of the **while** loop and continues with the next iteration. Apparently, the **continue** statement cannot immediately follow the **while** statement. |  Warning: when using a **while** command in IDLE, it is executed until the end (until Logical Expression results in False) before the next command can be given. Suppose  
L = 4  
---|---  
M = 1  
**while** M<L: M += 1;  
**    print**(M) ->  
4   
M = 1  
**while** M<4:  
  **print**(M)  
  M += 1 ->  
1  
2  
3  
**print**(10) ->  
10  |  M = 1  
**while** M < 4:  
    print(M)  
    M += 2  
**else** : **print**(7)->  
1  
3   
7  
i = 0; L = []  
**while** i < 3:  
  i += 1  
  **if** i == 2:  
    **continue**  
  L = L + [i]   
print(L) -> [1, 3] |  # Example of a loop  
# with infinite # execution and **break** I = 1  
L = []  
**while True** :  
    I = I + 1  
    L.append(I)  
    if I > 4:  
       **break**  
       print(I) ->  
2  
3  
4  
print(L) ->  
[2, 3, 4, 5, 6]  
  
**13.4 for** repetition tatement (loop)  
  
**for** Variable**in** Expression List:  
   Block   [to be repeated]  
**else** : [Optional]  
   Block  
  
Values from the Expression List are consecutively assigned to Variable; for each repetition the for block is executed once.   
When the list is exhausted, the **else** block is executed, if it exists.   
A **break** statement stops the execution of the repeating loop and jumps to the next statement after the **for**. The **continue** statement may be used inside a **for** , as with the **while** statemente  
|  **for** I **in** range(3): #starts with 0!  
  print(I) ->  
0  
1  
2 **for** I **in** range(2,4): #starts with2  
   I # and ends with 3 (4-1)! ->  
2  
3   
Fruits = ['apple','peach','mango']  
**for** fruit**in** Fruits:   
   print ('Fruit of the turn:', fruit) ->  
Fruit of the turn: apple  
Fruta da vez: peach  
Fruta da vez: mango **for** I **in** range(3):  
    if I==2: **break**  
    print(I) ->  
0  
1 |  **for** letter **in** 'xyz':  
   print ('Letra da vez:', letter) ->  
Letra da vez: x  
Letra da vez: y  
Letra da vez: x   
  
Using **else and two chained fors  
****for** I **in** range(3):  
   **for** J **in** [2,'xy']:   
      print ('I =", I, 'J =", J]  
      **else** : print ('Passed here!')   
->  
I = 0 J = 2  
I = 0 J = xy  
'Passed here!  
I = 1 J = 2  
I = 1 J = xy  
'Passed here!'   
I = 2 J = 2  
I = 2 J = xy  
---|---|---  
**for** using iterables (cf. 2.10)   
---  
**for** i **in** [1, 2, 3]: print (i) ->  
1  
2  
3 |  **for** car **in** "123": print (car) ->  
1  
2  
3 | **for** index **in** {'one':1, 'two':2}: print (index) ->  
two  
one  
  
**13.5 match...case** of multiple logical choices  
---  
**match** Expression:  
   **case** Expression1: statement1   
   **case** Expression2: statement1  
   ...  
   **case** ExpressionN: stetmentN  
   **case_** : statem  
  
If Expression1 has the value **True** , then statement1 is executed; statement!it can be a block  
The same for Expression2,..., ExpressionN If Expression1,..., ExpressionN all have values other than Expression, then statemt is executed; this last **case_** is optional  
****   |  Suppose that variiable Color has a value 'blue', green', or 'red', or neither one of these, and one wants to exhibit the value of each one: **match** Color:  
   **case** 'blue'  : Print ('The color is blue')  
   **case** 'green': Print ('The color is green')  
   **case** 'pink'  : Print ('The color is pink'')  
   **case** **_         **: Print ('The color is neiter blue, green or red') The **match** statement replaces with many advantages a chain of **if** 's when testing the value of a single condition **if** <Expressiono> = ... :  
**   elif **<Expression1> = ... :  
**   elif **<Expression2> = ... :  
  ...  
**   elif **<ExpressionN> = ... :  
**   else** ...  
  
  
**13.6 import** statement Includes a module into a program, or just some of its functionalities. E.g., to use a mathematical funcion like sqrt it is necessary to import the math module. But if the program uses only the sqrt function, it may be imported isolatedly using the **from** statement: **from** module **import** function To use another name for a module:  
  
**import** module **as** new name |  **import** math; math.sqrt (4) ->  
2 **from** math **import** pi; pi ->  
3.141592653589793 **import** math; math.e ->  
2.718281828459045     
---|---  
**13.7 try** statement Exception (error) detection   
  
**try** : statement1  
**except** : statement2  
**except** : statement3  
**else** : statement4  
**finally** : statement5  
This statement checks if something in statement1 is undefined or produces an error, so statement1 cannot be executed. Then statement2 and statement3 (there could be just one or more **except** statements) are executed. If statement1 can be executed (no error) the **else** optional statement is executed. The **finally** optional statement executes statement5 regardless of whether there was an error in statement1. As the name **try** says, it is also used to test whether there will be an error in statement1, before the error occurs and execution stops.  
statment2, ..., statement 5 can be blocks of statements. One may embed a **try** inside a **tr** y  
See [many try examples](https://www.w3schools.com/python/python_try_except.asp). |  **try:**  
    print (x)  
**except:**  
    print ("An error will occur, probably x has not been declared)  
  
Suppose the existence of a list named L. This command can be used to check whether the element L[j] is not in the list L , in which case the value of j is greater than the index of the last element of L, or negative, cf. item 2.5 above:  
**try:**  
   A == L[j]  
**except:**  
    print ("Error: L[", j, "] is not in the list")  
**13.8 pass** This command, which is not composed, inserted into another one causes the system to ignore this other one. It is very practical when creating a program. See the example. See [many examples of pass](https://stackoverflow.com/questions/13886168/how-to-use-pass-statement) .   |  **def** OneFuntion(x):  
   **pass** The body of OneFunction has not yet been programmed, but it is already known that it will exist and the function will remain in this part of the program. This ensures that the entire program will be executed; without the pass it wouldn't be, there would be a syntax error.  
  
In the 2nd example of the **try** statement above, if nothing is to be done if L[j] is not in the list, one may use  
**try:** L[j]  
**except:** **pass**  
**13.9 raise** – executes an exception handling class **raise** SystemExit("Message")  
terminates program execution displaying Message This command, which is not composed, forces an error to occur, and terminates execution.  
See [description and examples of **raise**](https://www.geeksforgeeks.org/python-raise-keyword/) . The examples on the right were copied from this page.  
|  a = 5  
**if** a % 2 != 0:  
   **raise** Exception("The number cannot be odd")  
->  
Traceback (most recent call last):  
  File "./prog.py", line 3, in <module>  
Exception: The number cannot be odd In the example below, the program tests whether a type conversion is valid; ValueError is a class that prints its name and argument:  
s = 'apple''  
**try** :  
   num = **int**(s)  
**except** ValueError:  
    **raise** ValueError("Sring", s, "cannot be converted to integer"  
**13.10 yield** x This statement must be used within a function, generating a result for it. It does not interrupt the execution of the function, unlike **return** , which returns a single value (eventually, an iterable) and ends the execution of the function. **Yiel** d can be placed in several places within a function, and will generate the function's value every time it is executed. **return** can also occur in several places, but if executed it ends the execution of the function.  
The example on the side was taken from [here](https://horadecodar.com.br/python-para-que-serve-o-yield-quando-utilizar/) . |  **def** EvenOrOdd(x):  
  **for** i **in** range(x):  
    **if** (i % 2 == 0): **yield** 'even'  
    **else** : **yield** 'odd'  
y=EvenOrOdd (5)  
for j in y: print(j)  
->   
even  
odd  
even  
odd  
even  
  
###  14\. MODULES

#### 14.1 Introduction

  
Module is a name given in Python to a program M that can be inserted into a program P.For this, it is necessary that P "imports" M, using in P the statement **import** M. On import, one can locally rename a module M to MM using **import** M **as** MM. To create a module M, one must create a program for M and then store it with some name, for example M, and the necessary extension .py, i.e., M.py . In this way, one can create and use program libraries, reusing tested programs. A module M can contain its own variables and functions, which are used as if M were a class. If a variable V and f are a variable and a function declared within M, when referring to them in program P one uses M.V and M.f().  
  
  


#### 14.2 Some modules

Below are some very useful modules. To use them, one needs to examine the corresponding documentation, which can be found seraching the internet with Python and the module name. 

  1. Numpy: a module that allows scientific computation, processing of arrays, random numbers, Fourier transform (harmonic analysis) etc. 
  2. random: used for random number generation

  3. Math: See section 6 above.

  4. PyTest: facilitates testing programs. 

  5. Pyperclip: permits inserting text into the clipboard.

  6. Dash: that allows the creation of images of various types, such as a clock, linear and pie charts, etc.

  7. Matplotlib: a basic module for generating graphic charts.

  8. Seaborn: allows drawig statistical graphs.

  9. PyGame allows the use of multimedia routines for audio, keyboard, mouse, etc.

  10. Pillow: a part of the Python Image Library (Image module) allowing the creation of thumbnails, applying filters, displaying images, etc.

  11. Requests: a module that allows access to the internet and use of http, including authentication, use of cookies, working with sessions, proxies, etc. It allows the use of the Jason method avoiding inserting internet links manually.   


  12. Chardet: contains routines for detecting the type of characters used in a text.  


  13. Progress: allows for the generation of a bar graph showing the time progress of a procedure.




### **15\. RESERVED WORDS**

The following words cannot be used as identifier names (variables, functions and classes):  


**assert and as break class continue def del elif else except False finally for from global if import in lambda match None nonlocal not or pass is raise return True try while with yield**  
---  
  
### **16\. REFERENCES**

####  16.1 Tutorials

  * Free tutorial:: [www.educba.com/category/software-development/software-development-tutorials/python-tutorial/](https://www.educba.com/category/software-development/software-development-tutorials/python-tutorial/)
  * Another tutorial: <https://ddi.ifi.lmu.de/probestudium/2012/ws-i-3d-programmierung/tutorials/tutorial-python-schoene-einfuehrung-englisch/at_download/file>
  * "Official" tutorial: <https://docs.python.org/3/tutorial>
  * Tutorial on operators: [www.programiz.com/python-programming/operators](https://www.programiz.com/python-programming/operators);[ https://www.tutorialspoint.com/python/python_basic_operators.htm](https://www.tutorialspoint.com/python/python_basic_operators.htm)
  * Tutorial on variables, constantes e tipos: [www.tutorialspoint.com/python/python_variable_types.htm](https://www.tutorialspoint.com/python/python_variable_types.htm)
  * Tutorial on [usage of listas](https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html) com muitos exemplos e testes de conhecimento
  * Tutorial on using of _arrays_): [www.i-programmer.info/programming/python/3942-arrays-in-python.html](http://www.i-programmer.info/programming/python/3942-arrays-in-python.html)
  * Tutorial on using NumPy module for processing arrays: [ www.i-programmer.info/programming/python/5785-advanced-python-arrays-introducing-numpy.html?start=1](http://www.i-programmer.info/programming/python/5785-advanced-python-arrays-introducing-numpy.html?start=1)
  * Tutorial on classes: [ https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
  * Tutorial on modules: [ https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html)



#### 16.2 Other references

  * List with built-in functions, with links to their explanation: [https://docs.python.org/3/library/functions.html](https://www.ime.usp.br/~vwsetzer/://docs.python.org/3/library/functions.html)
  * Reference (cheat) sheet: <https://ddi.ifi.lmu.de/probestudium/2012/ws-i-3d-programmierung/tutorials/python-referenzkarte>
  * Reference sheet directed network administrators, with lists of libraries, methpds and modules, produced by PCWDSLD: [www.pcwdld.com/python-cheat-sheet](https://www.pcwdld.com/python-cheat-sheet)
  * Compact refernce sheet: <https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf>
  * On types: <https://docs.python.org/3/library/stdtypes.html>
  * Mathematical functions: <https://docs.python.org/2/library/math.html>
  * Functions on complex numbers: <https://docs.python.org/3/library/cmath.html#module-cmath>
  * Operator precedences: [www.tutorialspoint.com/python/operators_precedence_example.htm](http://www.tutorialspoint.com/python/operators_precedence_example.htm)
  * Referência manual: <https://docs.python.org/3/>
  * "Oficial" site: <https://www.python.org/>



### **17\. INSTALLING PYTHON AND USING THE IDLE INTERPRETER AND ITS EDITOR  
**

#### **17.1 Installation**

To install Python and use its IDLE (Integrated Develop and Learning) interpreter: <https://www.python.org/downloads> . IDLE allows programs to be typed; each line with a command typed in IDLE is executed immediately when closed with Enter. Try, for example, with the sequence A = 5 Enter A Enter. The value 5 will be displayed.  
  


#### 17.2 Using IDLE on Windows

**1.** On my W11, on 8/7/24 the Python 3.10.5 executable was automatically installed with Python 3.12.4 in c:\Windows\py.exe file. To find the path to this directory, right-click the Python icon if it is on the desktop, or in the list of preferred programs in the Start menu, then Properties, Shortcut tab; the path is in the Destination field and can be copied. In my case, to activate IDLE just do a Windows search with py., as the path must have been added to the Windows Path. **2**. When activating the Python program, an IDLE window appears, similar to a Windows prompt window, here called "statement window". After loading, the Python prompt appears, >>> and pne can type language statements. Several command windows can be opened by activating Python more than once as described, allowing copying and pasting from one to another. **3.** Editing a command in the Python statement window follows the Windows standard. **4.** It is necessary to type one line at a time, ending with Enter. Note that when one finishes typing a statement, by pressing Enter IDLE executes the statement and opens a new line with >>>. If it is a compound statement or function declaration, ... appears on the next line, where the continuation must be typed. To end a compound statement or function declaration, it is necessary to leave blank lines, which causes the compound statement to be executed, or the function remains declared and can be used later, with the >>> appearing again. Moreover, it is possible to hit Ctrl C to interrupt a statement, withou losing the present status of variables and other objects. Nevertheless, it cancels typing of a compound statement. **5.** To load a Python program (.py extension), use File &raarr; Open. **8.** To close the statement window, type quit() or, at the beginning of the next command line, Ctrl+D. Being in an IDLE window, to eliminate all variables and identifiers created with the last session/program, and continue with a new program, at the menu use Shell &raarr; Restart Shell. A line appears indicating this Restart. **9.** One can activate IDLE directly from a regular Windows prompt window. To do this, in this window, go to the directory where the Python executable is located (with the command > cd directory name) and give the py command. If py was entered in the Windows PATH when downloading Python, simply enter py from any command line in a Prompt window. The disadvantage of using the Windows Prompt is that one has only limited editing possibilities. In an IDLE window one may have more possibilities, for example when typing an **if** statement the next line with will appear with tabs. If the : at the end of the condition is forgotten, a message will point this out. **9.** For a list of active variable names during an execution in IDLE, use dir(). To delete a variable x (it will no longer be available), use del(x).  
  


#### 16.3 Editing a program with the IDLE Editor and running a stored program

**1.** IDLE has an Editor that launches in a separate window. Attention: instead of IDLE, use the Editor to test programs. It's much simpler and practical. To activate it, in the IDLE menu, click File &raarr; NewFile. A blank Editor window opens, where one can type a program, using IDLE and Windows editing facilities. When completing a line, Enter obviously does not produce its execution, unlike IDLE. **2.** Once typing the program is finished, one needs to store it using File &raarr; Save. The file name appears on the first line, between asterisks, indicating that it was stored and giving its path. **3.** If a program is stored in a file, in the Editor one can load it by clicking on the File &raar Open (this can also be done in the IDLE window, which opens one in the Editor), and the file name must have the .py extension. **4.** A program in the Editor can be executed by first storing it using File &raarr Save option, and then Run &raarr Run Module. This clears everything that was in IDLE (variables, that cease to exist, state of the previous program, etc.), displays the message === RESTART: path to the file with the program that was executed ===, and copies the program from the Editor into IDLE and runs it. **5.** Attention: if in the executed program the variable A has a value, e.g. 5, if one enters A in one line of the editor, when executing the program with Run Module the value of A will not appear on the next line, as would happen if the program were typed and executed in the IDLE window. This is obvious, because by inserting a satement in an IDLE line and pressing Enter, the statement is interpreted and executed. When executing a complete program copied from the Editor window, there is no statement-by-statement interpretation, giving its result. To display the value of A when executing a program in the Editor, it is necessary to enter the command print(A) or print("A=", A). **6**. To edit a program outside of IDLE and the Editor, use Windows Notepad (or copy the program that was edited in another editor, to a Notepad window). When storing the text, to be loaded into the Editor, in the Type field choose All files, in (attention!) Encoding choose UTF-8, put the .py extension in the name and save the program. Another possibility is to save as .txt and then change the extension to .py. To do this, use for example the Total Commander program, which I use instead of Windows Explorer, as it is much more practical, displaying two parts in one window, and one can move or copy from one part to the other, one can search for file or directory names, changing name extensions, etc.  
  


#### 16.4 Using the IDLE Debugger

To detect errors in a locally stored program, one can use the IDLE Debugger. See its excellent tutorial at  
[www.cs.uky.edu/~keen/help/debug-tutorial/debug.html  
](https://www.cs.uky.edu/%7Ekeen/help/debug-tutorial/debug.html)**1.** Load a program in the Editor (see item 3 above). **2.** Insert breakpoints in places where you want execution to stop, for example to check the value of variables or the sequence of command execution. To do this, in the Editor, right-click the line where you want to insert a breakpoint, and click Set Breakpoint. A yellow stripe appears on the line. To eliminate a breakpoint, hit Clear Breakpoint. **3.** In the Editor, click Window &raarr; Show Line Numbers; The program line numbers appear, which is important for following the Debugger. **4.** In IDLE, click Debug &raarr; Debugger; the DEBUG ON message appears. Repeating this, when turning off Debugger, DEBUG OFF appears in IDLE. **5.** In the Editor, clicking Run &raarr; Execution Module; a Debug Control window appears. In it, below the buttons the name of the program appears and on the work area a blue-striped line with > and at the end of it the line number with the stop point where the execution stopped was inserted. **6.** By pressing the Step button, the program will be executed line by line, with the current one colored in gray _before_ being executed. If the line contains an assignment of a value to a variable, after executing that line that variable is displayed in the Debugger window and the value it received appears in the Locals area, along with identifiers and values of all variables whose values have already been assigned (so one can check what will happen with the conditions of sgtatement such as **if** and **while**). This Step feature is perhaps the most useful, as it allows yone to follow the entire execution. **7.** By pressing the Go button, the program runs without stopping until the next breakpoint. Thus, if there is some doubt about the execution of a section of the program, one can delimit it with two breakpoints, initially divert to the first with Go, and from then on use Step; When you reach the second point, you can press Go again to go to the starting point of the stop. **8.** If an input() function is executed, the process will stop. It is necessary to go to the IDLE window and enter the requested value and Enter. The given value, with the variable that received the input, appears in the Locals section. **9.** If an error occurs while running the program, the message will appear in the Debugger window. **10**. The Quit button terminates the debugger execution. **11.** I still haven't figured out what the Out button is for, maybe to switch to the Editor window.  
  


### **17\. FREE COURSES**

  * Python course in Portuguese on Coursera (free if without a certificate), by Prof. Fábio Kon (IME-USP): [www.coursera.org/learn/ciencia-computacao-python-conceitos](https://www.coursera.org/learn/ciencia-computacao-python-conceitos)

  
Attention : in this course, Prof. Kon gives examples in which he edits a program in a text editor, then stores it, for example, in a file called program.py . Then he enables the Python interpreter using the statement (or something like i) ...> python35 program.py . It turns out that IDLE uses the UTF-8 character encoding, so the program text must be stored locally in that encoding, which exist in some text editors. On Windows, which normally uses the Latin-1 encoding (not supported by IDLE), Notepad has this option, in the Save As &raarr; Encoding option and selecting UTF-8. The same for programs that the course requires to be sent to Coursera to be executed and evaluated in that system. If this is not done, when running the program an unrecognized character error message appears.  
  

  * Courses in English: [www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners)



### **18\. TEXTS, PROGRAMMING ENVIRONMENTS, DOCUMENTATION, PROGRAMMING FORUMS**

  * [Spyder](https://www.spyder-ide.org/) : programming and debugging environment (IDE), which was strongly recommended by {AL} as being much better than IDLE and its Editor

  * [Jupyter](https://jupyter.org/) : a system available on the internet which, using a browser, provides for a programming and debugging environment with resources for literary programming (source code and docummentation together in a single file). Works both in a local computer as welll as in a remote on the internet. No need to install IDLE.

  * [Azure](https://blogs.technet.microsoft.com/machinelearning/2015/07/24/introducing-jupyter-notebooks-in-azure-ml-studio/) : Microsoft environment; includes Jupyter and provides additional features. Programs are kept in "notebooks". To create one, log into your account, click on Notebooks (in the left menu) and then + New (in the bottom left corner). In each cell of a notebook it is possible to place a program and modify it; To run it, select it and press Shift Enter. A variable or function declared in a cell that has already been executed is valid in other cells. Apparently it does not include the IDL debugger.

  * [PyCharm](https://www.jetbrains.com/pycharm/) , a programming environment with an open source version (free of charge). {LF}

  * [Anaconda](https://www.anaconda.com/distribution/), an open source programming environment including systems for machine learning.

  * [GitHub](https://github.com/) is a forum, a community of developers, where participants post programs. There you can find the entire book Python Data Science Handbook by Jake VanderPlas. {LF}

  * Official Python Community forums: <https://discuss.python.org/>



### **19\. ACKNOWLEDGMENTS  
**

  * Collaborators (search the page with abbreviations): {AL} Alexandre Leite; {LF} Luis Felipe Carvalho; {MDG} Marco Dimas Gubitoso; {PC} Paulo César Zandona Vieira found 2 mistakes. Eduardo Furlan contributed with many additions of functions, texts and typos.




 
