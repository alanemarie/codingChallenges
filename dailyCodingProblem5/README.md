## Description

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
def cons(a,b):
    def pair(f):
        return f(a, b)
    return pair
   
Implement car and cdr.

## Solution

This problem is a matter of dealing with functional programming, a programming paradigm.
This paradigm, roughly speaking, treats a program as a composition of functions (different from the imperative paradigm, in which the code is a sequence of instructions).

Look that cons(a,b) returns the function pair, and pair receives another function, f, as parameter. The function f then uses the input parameters a and b.

Function car will receive function cons(a,b) as parameter. But, as we saw, for given parameters a and b, cons(a,b) returns function pair. Therefore, 
the input of function car is pair(f). In this context, we will call g as the input of car:

def car(g):
  ...
 
What do we know about g? Well, g receives a function f as parameter and f is the function
that we need to get the first element of the pair! We will call f as 'first' in the context of car:
 
 def car(g):
  def first(a,b):
    return a
  return g(first)
 
For the second element, we define cdr analogously:
 
 def cdr(g):
  def second(a,b):
    return b
  return g(second)
 
------
For example: consider a=1 and b=3. When we call car(cons(1,3)), we have:

_ car returns pair(first(1,3))
__ pair(first(1,3)) returns first(1,3)
___ first(1,3) returns 1.


When we call cdr(cons(1,3)), we have:

_ cdr returns pair(second(1,3))
__ pair(second(1,3)) returns second(1,3)
___ second(1,3) returns 3.
