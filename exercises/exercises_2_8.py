import math

F_IVP = lambda x: -x
X_0 = 1

def euler_method(x_0, f, delta_t, n_steps):
    x_i = x_0

    for step in range(n_steps):
        x_i += f(x_i) * delta_t


    return x_i

def improved_euler_method(x_0, f, delta_t, n_steps):
    x_i = x_0

    for step in range(n_steps):
        x_tmp = x_i + f(x_i) * delta_t
        x_i += (f(x_i) + f(x_tmp)) * delta_t / 2

    return x_i

def runge_kutta_method(x_0, f, delta_t, n_steps):
    x_i = x_0

    for step in range(n_steps):
        k_1 = f(x_i) * delta_t
        k_2 = f(x_i + k_1 / 2) * delta_t
        k_3 = f(x_i + k_2 / 2) * delta_t
        k_4 = f(x_i + k_3) * delta_t
        x_i += (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6

    return x_i

DELTA_TS = [1, 0.1, 0.01, 0.001, 0.0001]
N_STEPS = [1, 10, 100, 1000, 10000]

METHODS = [euler_method, improved_euler_method, runge_kutta_method]

print("\nTesting Different Methods of Integration")
print(f'Correct answer is {math.exp(-1)}')

for method in METHODS:
    print(f'\nMethod: {method.__name__}')
    for delta_t, n_steps in zip(DELTA_TS, N_STEPS):
        print(f'Delta t = {delta_t}, prediction is {method(X_0, F_IVP, delta_t, n_steps)}')
