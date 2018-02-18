# encoding=utf8
# pylint: disable=anomalous-backslash-in-string
"""Implementation of Sphere functions.

Date: 2018

Authors: Iztok Fister Jr.

License: MIT

Function: Sphere function

Input domain:
    The function can be defined on any input domain but it is usually
    evaluated on the hypercube x_i ∈ [0, 10], for all i = 1, 2,..., D.

Global minimum:
    f(x*) = 0, at x* = (0,...,0)

LaTeX formats:
    Inline: $f(x) = \sum_{i=1}^D x_i^2$
    Equation: \begin{equation}f(x) = \sum_{i=1}^D x_i^2 \end{equation}
    Domain: $0 \leq x_i \leq 10$

Reference paper:
    Jamil, M., and Yang, X. S. (2013).
    A literature survey of benchmark functions for global optimisation problems.
    International Journal of Mathematical Modelling and Numerical Optimisation,
    4(2), 150-194.
"""

import math

__all__ = ['Sphere']


class Sphere(object):

    def __init__(self, Lower=-5.12, Upper=5.12):
        self.Lower = Lower
        self.Upper = Upper

    @classmethod
    def function(cls):
        def evaluate(D, sol):

            val = 0.0

            for i in range(D):
                val += math.pow(sol[i], 2)

            return val

        return evaluate
