Pi From Pascal's Triangle


This program (made with python 3) derives the number pi (3.14159... etc.) from Pascal's triangle.


![alt text](https://github.com/falconite400/piFromPascal/blob/main/images/triangle.jpg?raw=true)
Each number in the triangle is calculated by adding together the two numbers above it. 

Pi is derived from Pascal's triangle by taking the reciprocal of the third number of each row (excluding the first
two rows), changing the sign of each fraction by alternating between two positive and two negative signs, starting
with positive (+ + - - + + - - etc.), adding the fractions together, and them adding two to the sum.

For example, the first few reciprocals would be:
![alt text](https://github.com/falconite400/piFromPascal/blob/main/images/fractions.jpg?raw=true)

Applying the + + - - part, we have
![alt text](https://github.com/falconite400/piFromPascal/blob/main/images/fractions_alternating.jpg?raw=true)

Adding these together yeilds approximately 1.14207181707.

Adding 2 to this yeilds 3.14207181707, which is close to pi.

The more numbers are used, the more accurate the result is. For example, when 10,000 numbers are used in the program,
the result is 3.141592633593785, which is much more accurate than the previous example.
