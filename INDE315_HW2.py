import math as m
import numpy as np
from homework import *

# problem 1---------------------------------------------------------------------
problem(1)
days = np.array([1.5,3.0,4.5,5.0,7.0])
prob_days = np.array([0.05,0.25,0.35,0.20,0.15])

mhu = mhu_func(days, prob_days)
sigma_squared = sigma_squared_func(days, prob_days, mhu)

print(f'mhu: {round(mhu, 4)}')
print(f'sigma_squared: {round(sigma_squared, 4)}')


# problem 2---------------------------------------------------------------------
problem(2)
a2 = 5
b2 = 9

mhu_DUD = lambda a, b: (b + a) / 2
sigma_squared_DUD = lambda a, b: ((b-a+1) ** 2 - 1)/12

print(f'mhu: {round(mhu_DUD(a2,b2), 4)}')
print(f'sigma: {round(m.sqrt(sigma_squared_DUD(a2,b2)), 4)}')


# problem3---------------------------------------------------------------------
problem(3)
n3 = 10
p3 = sum(prob_days[0:2])
print(f'a): {round(binomial_distribution(7, n3, p3), 4)}')
x3b = [0, 1, 2]

ans3b = 0
for x in x3b:
    ans3b += binomial_distribution(x, n3, p3)
ans3b = round(ans3b, 4)
print(f'b). {ans3b}')

ans3c = 1 - binomial_distribution(0, n3, p3)
ans3c = round(ans3c, 4)
print(f'c). {ans3c}')
print(f'd). {n3 * p3}')


# problem 4---------------------------------------------------------------------
problem(4)
r4 = 2
p4 = 0.1
x4 = [2,3]
sum4a = 0
for x in x4:
    sum4a += negative_binomial_distribution(r4, x, p4)

ans4a = round(1 - sum4a, 4)
print(f'a): {ans4a}')
print(f'b): {r4/p4}')


# problem 5---------------------------------------------------------------------
problem(5)
x5 = range(2, 31)
n5 = 30
p5 = 0.001
ans5a = 0
for x in x5:
    ans5a += binomial_distribution(x, n5, p5)

print(f'a): {round(ans5a, 6)}')
print(f'b): {round(1/ans5a, 4)}')


# problem 6---------------------------------------------------------------------
problem(6)
fOfX6 = lambda x: 2 / x**3 if x > 1 else 0

# scipy.integrate.quad returns a two-value tuple; first is the answer, and
# the second is the estimated upperbound error
ans6a = prob_density_function(fOfX6, -1 * m.inf, 2)[0]

ans6b = prob_density_function(fOfX6, 5, m.inf)[0]

ans6c = prob_density_function(fOfX6, 4, 8)[0]

ans6d = 1 - prob_density_function(fOfX6, 4, 8)[0]

# calculated in the notes
ans6e = m.sqrt(20)

print(f'a): {round(ans6a, 4)}')
print(f'b): {round(ans6b, 4)}')
print(f'c): {round(ans6c, 4)}')
print(f'd): {round(ans6d, 4)}')
print(f'e): {round(ans6e, 4)}')


# problem 7---------------------------------------------------------------------
problem(7)
fOfX7 = lambda x : 1.25 if 74.6 < x < 75.4 else 0
ans7a = prob_density_function(fOfX7, -1 * m.inf, 74.8)[0]

ans7b = 1 - prob_density_function(fOfX7, 74.8, 75.2)[0]

ans7c = prob_density_function(fOfX7, 74.7, 75.3)[0]

print(f'a): {round(ans7a, 4)}')
print(f'b): {round(ans7b, 4)}')
print(f'c): {round(ans7c, 4)}')


# problem8---------------------------------------------------------------------
problem(8)
gOfX8_1 = lambda x : x * 0.125 * x if 0 < x < 4 else 0
gOfX8_2 = lambda x : x**2 * 0.125 * x if 0 < x < 4 else 0

ans8a = mhu_prob_density_function(gOfX8_1)[0]
print(type(ans8a))
ans8b = sigma_squared_prob_density_function(gOfX8_2, ans8a)

print(f'a): {round(ans8a, 4)}')
print(f'b): {round(ans8b, 4)}')

# problem9---------------------------------------------------------------------
problem(9)
a = 1.5
b = 2.2
fOfX9 = lambda x : 1 / 0.7 if 1.5 < x < 2.2 else 0

mhu9 = (b + a) / 2
sigma_squared9 = (b-a)**2 / 12
print(f'a): mhu = {mhu9} and sigma_squared = {sigma_squared9}')

ans9b = prob_density_function(fOfX9, -1*m.inf, 2)[0]
print(f'b): {round(ans9b, 4)}')

print('c): Done on paper...')


# problem10--------------------------------------------------------------------
problem(10)
print('Done on paper....')

# problem11--------------------------------------------------------------------
problem(11)

# problem12--------------------------------------------------------------------
end()
