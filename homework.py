import math as m
import numpy as np
import scipy.integrate as integrate

def combination(r, n):
    """
    Combination rule: n! / (r! * (n-r)!)
    r, n are integers
    """
    return m.factorial(n)/(m.factorial(r)*m.factorial(n-r))

def permutation(r, n):
    """
    Permutation rule: n! / (n-r)!
    r, n are integers
    """
    answer = 1
    for i in range(n - r + 1, n + 1):
        answer *= i
    return answer

def mhu_func(x, fOfX):
    """
    General mean calculation: mhu = E(X) = sum(x * f(x))
    x, fOfX are numpy.array
    """
    return np.sum(x * fOfX)

def sigma_squared_func(x, fOfX, mhu):
    """
    General variance calculation: sigma_squared = sum(x^2 * f(x)) - mhu^2
    x, fOfX are numpy.array; mhu is a float
    """
    return np.sum(x ** 2 * fOfX) - mhu ** 2

def binomial_distribution(x, n, p):
    """
    Must be independent trials
    f(x) = combination(x , n) * p^x * (1-p)^(n-x)
    x, n, p are floats
    """
    return combination(x, n) * p**x * (1-p)**(n-x)

def negative_binomial_distribution(r, x, p):
    """
    Negative Binomial Distribution: last trial always end with a success
    f(x) = Combination(r-1, x-1) * p&r * (1-p)^(x-r)
    r, x are integers; p is float
    """
    return combination(r-1,x-1) * p**r * (1-p)**(x-r)

def prob_density_function(fOfX, low, high):
    """
    P(a < X < b) = integral(fOfX) from low to high
    fOfX is a function; low and high are floats
    """
    return integrate.quad(fOfX, low, high)

def mhu_prob_density_function(gOfX):
    """
    mhu = integral(x * fOfX) from -inf to inf
    gOfX = x * fOfX
    lower-bound is -inf and upper-bound is inf always
    """
    return integrate.quad(gOfX, -1*m.inf, m.inf)

def sigma_squared_prob_density_function(gOfX, mhu):
    """
    sigma_squared = integral(x^2 * fOfX) from -inf to inf - mhu**2
    gOfX = x^2 * fOfX
    """
    return integrate.quad(gOfX, -1*m.inf, m.inf)[0] - mhu**2


def problem(number):
    """
    Draw a line ----------------------------------------------
    """
    print('-' * 40)
    print(f'Problem {number}:')

def end():
    """
    Draw the end line
    """
    print()
    print(('*' * 18).ljust(18), end='')
    print('END', end='')
    print(('*' * 19))
