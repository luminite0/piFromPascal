Pi From Pascal's Triangle


This program (made with python 3) derives the number pi (3.14159... etc.) from Pascal's triangle.

                Pascal's Triangle


                ![alt text](https://github.com/falconite400/piFromPascal/blob/main/triangle.jpg?raw=true)
Each number in the triangle is calculated by adding together the two numbers above it. 

Pi is derived from Pascal's triangle by taking the reciprocal of the third number of each row (excluding the first
two rows), changing the sign of each fraction by alternating between two positive and two negative signs, starting
with positive (+ + - - + + - - etc.), adding the fractions together, and them adding two to the sum.

For example, the first few reciprocals would be:
        1   1   1   1   1  1
        -   -   -   -   -  -
        1   3   6   10  15 21

Applying the + + - - part, we have

        1    1    1    1    1
      + -  + -  - -  - -  + -  
        1    3    6    10   15 .

                              34
Adding these together yeilds  --
                              30 

Multiplying adding two 
