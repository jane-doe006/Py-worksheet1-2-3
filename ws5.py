import numpy as np
from scipy import fftpack, linalg, interpolate, signal, optimize, stats, integrate
import matplotlib.pyplot as plt

# 1
arr1 = np.random.rand(10)
print(arr1)
print('mean:', np.mean(arr1))
print('median:', np.median(arr1))
print('variance:', np.var(arr1))

# 2
arr2 = np.random.rand(5, 5)
print(arr2)
print(fftpack.fft2(arr2))


# 3
A = np.array([[4, 2], [3, 1]])
print(A)
print('determinant:', linalg.det(A))
print('inverse:', linalg.inv(A))
print('eigenvalues:', linalg.eigvals(A))

# 4
x = np.linspace(0, 10, 10)
y = np.sin(x)
print(x)
print(y)
f = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, 100)
ynew = f(xnew)
print(ynew)

# 5
t = np.linspace(0, 1, 100)
data = np.sin(2 * np.pi * 7 * t) + np.random.randn(100) * 0.5
print(data)
b, a = signal.butter(3, 0.05)
filtered = signal.filtfilt(b, a, data)
print(filtered)

# 6
sales = np.random.randint(100, 500, (12, 4))
print(sales)
print('total sales:', np.sum(sales))
print('average sales:', np.mean(sales))
print('max sales:', np.max(sales))
print('best month:', np.argmax(np.sum(sales, axis=1)) + 1)
print('worst month:', np.argmin(np.sum(sales, axis=1)) + 1)

# 7
marks = np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
print(marks)
print('total marks:', np.sum(marks, axis=1))
print('average marks:', np.mean(marks, axis=1))
print('subjectwise avg:', np.mean(marks, axis=0))
print('top performer:', np.argmax(np.sum(marks, axis=1)))
print('bottom performer:', np.argmin(np.sum(marks, axis=1)))
passing = np.sum(np.mean(marks, axis=1)>=40)/len(marks)*100
print('passing:', passing)

# 8
t_data = np.array([0,1,2,3,4,5])
v_data = np.array([2,3.1,7.9,18.2,34.3,56.2])
def quad_func(t, a, b, c):
    return a*t**2 + b*t + c
params, _ = optimize.curve_fit(quad_func, t_data, v_data)
print(params)

# 9
print(marks)
plt.figure()
plt.bar(['Arin','Aditya','Chirag','Gurleen','Kunal'], np.sum(marks, axis=1))
plt.xlabel('student')
plt.ylabel('total Marks')
plt.show()

# 10
print(params)
plt.figure()
plt.scatter(t_data, v_data, label='data')
plt.plot(t_data, quad_func(t_data, *params), label='fitted Curve')
plt.legend()
plt.title('velocity curve fitting')
plt.show()

# 11
years = np.array([2000,2005,2010,2015,2020])
pop = np.array([50,55,70,80,90])
corr = np.corrcoef(years, pop)[0,1]
print('Pearson corr:', corr)
f = interpolate.interp1d(years, pop)
pop_2008 = f(2008)
print('Pop in 2008:', pop_2008)
plt.plot(years, pop, 'o')
plt.plot(2008, pop_2008, 'rx')
plt.show()

# 12
p = np.poly1d([1, -5, 2, -8])
roots = p.roots
print('roots:', roots)
x_poly = np.linspace(-3, 3, 100)
plt.plot(x_poly, p(x_poly))
plt.scatter(roots, p(roots), color='red')
plt.show()

# 13
import time
sizes = [200, 400, 600, 800, 1000]
times = []
for s in sizes:
    txt = ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), s*1024*1024))
    start = time.time()
    res = txt.upper()
    end = time.time()
    duration = end-start
    print(f'{s}MB took:', duration)
    times.append(duration)
plt.plot(sizes, times)
plt.xlabel('file Size (MB)')
plt.ylabel('time (sec)')
plt.show()

# 14
def f(x): return x**4 - 3*x**3 + 2
min_x = optimize.minimize_scalar(f, bounds=(2, 3), method='bounded').x
print('local minima at:', min_x)
x_vals = np.linspace(2, 3, 100)
plt.plot(x_vals, f(x_vals))
plt.scatter([min_x], [f(min_x)], color='red')
plt.show()

# 15
def damped_osc(y, t):
    theta, omega = y
    dydt = [omega, -0.2*omega - theta]
    return dydt

time_vec = np.linspace(0, 20, 200)
sol = integrate.odeint(damped_osc, [1, 0], time_vec)
print(sol[:, 0])
plt.plot(time_vec, sol[:, 0])
plt.xlabel('time (s)')
plt.ylabel('joint Angle (radian)')
plt.show()
print('max displacement:', np.max(sol[:,0]))
print('time of max:', time_vec[np.argmax(sol[:,0])])

