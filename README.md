
*GeekTrust Problem Set 5*

## How to Run:

#### for Problem one:

```
$ python

>>> from problem_one import GoldenCrown

>>> d = GoldenCrown()

>>> d.allies()
```

#### for Problem two

```
$ python

>>> from problem_two import BreakerOfChains

>>> s = BreakerOfChains()

>>> s.ruler()
```
##  

1) Both the problem sets are done using Python3

2) Each has the given set of question to be asked

  

3) Sample Input/Output data

  

Who is the ruler of Southeros?

  

Output: None

  

Allies of King Shan?

  

Output: None

  

Input Messages to kingdoms from King Shan:

  

Input: Air, "Let’s swing the sword together"

  

Input: Land, "Die or play the tame of thrones"

  

Input: Ice, "Ahoy! Fight for me with men and money"

  

Input: Water, "Summer is coming"

  

Input: Fire, "Drag on Martin!"

  
  
  

Who is the ruler of Southeros?

  

Output: King Shan

  

Allies of King Shan?

  

Output: Air, Land, Ice, Fire

  

4) Each message input needs to be given separately

5) Both the sets have the declared dictionary for key as Kingdom and value as Emblem for the same

6) Following things are majorly used:
	i) dictionary,
	ii) list,
	iii) list comprehension,
	iv) file input for message
	v) declared functions,
	vi) input()
	vii) for loops

  

About the test:

Problem 1 Has to evaluate who are the Allies of King Shah, if the right message is sent the Allies will support the King.

  

Problem 2 Has to evaluate the kingdom with maximum number of allies, where a message chosen randomly if sent to the right allies, they will give the support to the sender kingdom, given that the Allies are not participating and have not already given their support to the other allies.