import math
import numpy as np
import matplotlib.pyplot as plt
import keyboard
def org_function(points):
    y = []
    for i in range(len(points)):
        flag = 10*math.sin(points[i] * 5) + 7 * math.fabs(points[i] - 5) + 10
        y.append(flag)
    return y

def decimal_to_binary(decimal_num , length):
    binary_str = []
    binary_str.append(bin(decimal_num)[2:])  # 使用内置的 bin() 函数将十进制转换为二进制字符串
    binary_list = [int(flag) for flag in str(binary_str[0])]
    while len(binary_list) < length:
        binary_list.insert(0,0)
    return binary_list

def make_picture():
    max_x = 15
    min_x = 0
    x_1 = np.linspace(min_x , max_x , 1000)
    y_1 = org_function(x_1)
    plt.plot(x_1 , y_1)
    plt.show()


def copy_def(list):
    list_copy = []
    for i , value in enumerate(list):
        list_copy.append(value)
    return list_copy


def exchange_num(pop):
    result = []
    for i in range(len(pop)):
        r = 0
        for j in range(len(pop[0])):
            if pop[i][j] == 1:
                r += 2 ** (len(pop[0]) - j - 1)
        result.append(r)
    return result

def draw_picture(pop , adaptation_values , generation):
    x = np.linspace(0,10 , 1000)
    y = org_function(x)
    plt.figure()
    plt.plot(x , y)
    max_func_value = max(adaptation_values)
    x_1 = exchange_num(pop)
    for i in range(len(pop)):
        x_1[i] = 10 * x_1[i] / 1023
    y_1 = org_function(x_1)
    true_y = max(y_1)
    plt.scatter(x_1,y_1 , color = 'r')
    print(x_1[0])
    plt.text(0 , 0 , f'generation:{generation} max_fuc_value:{true_y}' , family = 'Arial' , fontsize = 12 , style = 'italic' , color = 'mediumvioletred')
    plt.pause(0.2)






