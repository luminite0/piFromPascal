Pi From Pascal's Triangle


This program (made with python 3) derives the number pi (3.14159... etc.) from Pascal's triangle.


![alt text](https://github.com/falconite400/piFromPascal/tree/main/images/blob/main/triangle.jpg?raw=true)
Each number in the triangle is calculated by adding together the two numbers above it. 

Pi is derived from Pascal's triangle by taking the reciprocal of the third number of each row (excluding the first
two rows), changing the sign of each fraction by alternating between two positive and two negative signs, starting
with positive (+ + - - + + - - etc.), adding the fractions together, and them adding two to the sum.

For example, the first few reciprocals would be:
![alt text](https://github.com/falconite400/piFromPascal/blob/main
Applying the + + - - part, we have

        1    1    1    1    1    1    1    1    1    1
      + -  + -  - -  - -  + -  + -  - -  - -  + -  + -
        1    3    6    10   15   21   28   36   45   55

                              
Adding these together yeilds approximately 1.15786435786.

Adding 2 to this number equals
Multiplying adding two 
