import random
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from utilize import org_function , make_picture , exchange_num , draw_picture , decimal_to_binary , copy_def
import tqdm
class EA(object):

    #代码中定义的二进制数以最左边为最高位
    #不要淘汰父辈！！！！
    #建立一个选择函数将优秀的子辈替代不好的父辈！！！！
    def __init__(self , pop_size : int , binary_length : int , pc : float , pm : float , generations : int):
        self.pop_size = pop_size
        self.binary_length = binary_length
        self.pc = pc
        self.pm = pm
        self.pop = [[random.randint(0,1) for i in range(self.binary_length)] for j in range(self.pop_size)]
        self.generations = generations


    def caculate_adaptation(self):
        dec_pop = []
        for i in range(len(self.pop)):
            k = 10*exchange_num(self.pop)[i]/1023
            dec_pop.append(k)
        self.adaptation_values = []
        for i in range(len(self.pop)):
            j = org_function(dec_pop)[i]
            self.adaptation_values.append(j)


    def crossover(self):
        px = len(self.pop)
        py = len(self.pop[0])
        self.new_pop = [[0 for _ in range(py)] for _ in range(px)]
        for i in range(0 , px , 2):
            if random.uniform(0,1) < self.pc :
                cpoint = random.randint(0,self.binary_length-1)
                self.new_pop[i][0:cpoint] = self.pop[i][0:cpoint]
                self.new_pop[i][cpoint:self.binary_length] = self.pop[i+1][cpoint:self.binary_length]
                self.new_pop[i+1][0:cpoint] = self.pop[i+1][0:cpoint]
                self.new_pop[i+1][cpoint:self.binary_length] = self.pop[i][cpoint:self.binary_length]
            else:
                self.new_pop[i][:] = self.pop[i][:]
                self.new_pop[i+1][:] = self.pop[i+1][:]


    def mutation(self):
        for i in range(len(self.pop)):
            if random.uniform(0,1) < self.pm:
                mpoint = random.randint(0,self.binary_length-1)
                self.new_pop[i][:] = self.pop[i][:]
                if self.new_pop[i][mpoint] == 0:
                    self.new_pop[i][mpoint] = 1
                else:
                    self.new_pop[i][mpoint] = 0
            else:
                self.new_pop[i][:] = self.pop[i][:]

    def best_pop(self):
        self.best_individual = self.pop[0]
        self.best_fit = self.adaptation_values[0]
        for i in range(len(self.pop)):
            if self.adaptation_values[i] < self.best_fit:        ##############
                self.best_fit = self.adaptation_values[i]
                self.best_individual = self.pop[i]

    def selection_max(self):
        total_adaptation_value = sum(self.adaptation_values)
        selection_pop = []
        while len(selection_pop) < len(self.pop):
            random_num = random.uniform(0 , total_adaptation_value)
            cumulative_adaptation_value = 0
            for i , value in enumerate(self.adaptation_values):
                cumulative_adaptation_value += value
                if cumulative_adaptation_value >= random_num:        ###########  cumulative_adaptation_value >= random_num:
                    selection_pop.append(self.pop[i])
                    break
        self.pop = selection_pop


    def selection_min(self):
        total_adaptation_value  = sum(self.adaptation_values) - len(self.adaptation_values) * min(self.adaptation_values)
        selection_pop = []
        while len(selection_pop) < len(self.pop):
            random_num = random.uniform(0 , total_adaptation_value)
            cumulative_value = 0
            for i , value in enumerate(self.adaptation_values):
                cumulative_value += value
                if random_num - cumulative_value < 0:
                    selection_pop.append(self.pop[i])
                    break

    def selection_new_max(self):
        selection_pop = []
        flag = 0
        #### total_adaptation_value = sum(self.adaptation_values)
        min_adaptation_value = min(self.adaptation_values)
        #### average_adaptation_value = total_adaptation_value / len(self.pop)
        pop_copy = copy_def(self.pop)
        adaptation_values_copy = copy_def(self.adaptation_values)
        for i , value in enumerate(adaptation_values_copy):
            if adaptation_values_copy[i] <= min_adaptation_value * 1.005:
                pop_copy.pop(i)
                adaptation_values_copy.pop(i)
                flag += 1
            else :
                selection_pop.append(self.pop[i])
        middle = []
        for i in range(flag):
            if pop_copy == None:
                break
            else:
                middle_value = random.randint(int(min(adaptation_values_copy)), int(max(adaptation_values_copy)))
                middle.append(middle_value)
                pop_copy.append(ecimal_to_binary(middle[i], len(self.pop[0])))
                self.pop = pop_copy

    def selection_new_min(self):
        selection_pop = []
        flag = 0
        #### total_adaptation_value = sum(self.adaptation_values)
        max_adaptation_value = max(self.adaptation_values)
        #### average_adaptation_value = total_adaptation_value / len(self.pop)
        pop_copy = copy_def(self.pop)
        adaptation_values_copy = copy_def(self.adaptation_values)
        for i , value in enumerate(adaptation_values_copy):
            if adaptation_values_copy[i] >= max_adaptation_value * 0.95:
                pop_copy.pop(i)
                adaptation_values_copy.pop(i)
                flag += 1
            else :
                selection_pop.append(self.pop[i])
        middle = []
        for i in range(flag):
            if pop_copy == None:
                break
            else:
                middle_value = random.randint(int(min(adaptation_values_copy)), int(max(adaptation_values_copy)))
                middle.append(middle_value)
                pop_copy.append(decimal_to_binary(middle[i], len(self.pop[0])))
                self.pop = pop_copy

    def run(self):
        #make_picture()
        #plt.pause(5)
        #plt.cla()
        self.caculate_adaptation()  # 计算当前种群中每个个体的适应度
        for generation in tqdm.tqdm(range(self.generations) , desc = "Processing"):
            if keyboard.is_pressed('esc'):
                print("Iteration stopped by pressing 'esc' key.")
                break
            self.selection_max()
            self.crossover()
            self.mutation()
            self.pop = self.new_pop
            self.caculate_adaptation()  # 计算当前种群中每个个体的适应度
            plt.cla()
            plt.title("Evolution Algorithm")
            draw_picture(self.pop, self.adaptation_values , generation)






