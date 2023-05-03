from math import cbrt
from math import sqrt
from math import atan
from math import cos
from math import acos
from math import sin

def norm_of_vector(vector:list):
    res = 0
    for i in range(0, len(vector)):
        res += vector[i]**2

    return sqrt(res)


class SystemOfEquation:
    def __init__(self, coef:list, operations_list:list):
        self.coef = coef.copy()
        self.var = []
        self.op_list = operations_list.copy()
        self.res = []


    def simple_itteration(self, var:list ,e:float):
        j = 1
        self.var = var.copy()
        while(True):
            prev_var = self.var.copy()

            for i in range(0, len(self.var)):
                self.var[i] = self.op_list[i](self.coef, prev_var)

            print(f"Itteration {j}")
            for i in range(0, len(self.var)):
                print(f"x{i + 1} = {self.var[i]}")

            j += 1

            if abs(norm_of_vector(self.var) - norm_of_vector(prev_var)) <= e:
                print("===========================")
                print("Result: ")
                print(f"Amount of itterations: {j}")
                for i in range(0, len(self.var)):
                    print(f"x{i + 1} = {self.var[i]}")
                print("===========================")
                break



    def gauss_seidel(self, var: list, e: float):
        j = 1
        self.var = var.copy()
        while (True):
            prev_var = self.var.copy()

            for i in range(0, len(self.var)):
                self.var[i] = self.op_list[i](self.coef, self.var)

            print(f"Itteration {j}")
            for i in range(0, len(self.var)):
                print(f"x{i + 1} = {self.var[i]}")

            j += 1

            if abs(norm_of_vector(self.var) - norm_of_vector(prev_var)) <= e:
                print("===========================")
                print("Result: ")
                print(f"Amount of itterations: {j}")
                for i in range(0, len(self.var)):
                    print(f"x{i + 1} = {self.var[i]}")
                print("===========================")
                break





def equation_1_x(coef:list, var:list):
    x = var[0]
    y = var[1]
    a = coef[0]
    b = coef[1]
    c = coef[2]
    d = coef[3]
    f = coef[4]
    g = coef[5]
    return cbrt((b * (y ** 3) - c) / a)


def equation_1_y(coef:list, var:list):
    x = var[0]
    y = var[1]
    a = coef[0]
    b = coef[1]
    c = coef[2]
    d = coef[3]
    f = coef[4]
    g = coef[5]
    return sqrt(abs((d*(x**2)+g)/f))



def derivative_1_x(coef:list, var:list):
    x = var[0]
    y = var[1]
    a = coef[0]
    b = coef[1]
    c = coef[2]
    d = coef[3]
    f = coef[4]
    g = coef[5]
    return (b*y)/(sqrt(abs(a*b*(y**2)+a*c)))


def derivative_1_y(coef:list, var:list):
    x = var[0]
    y = var[1]
    a = coef[0]
    b = coef[1]
    c = coef[2]
    d = coef[3]
    f = coef[4]
    g = coef[5]
    return (d*x)/sqrt(abs(d*f*(x**2)+f*g))


def tmp_cond(coef:list, var:list):
    return (-1)*derivative_1_x(coef,var)*derivative_1_y(coef,var)





o_1 = equation_1_x
o_2 = equation_1_y
o_list = [o_1, o_2]
coef = [3, 5, 4, 5, 12, 13]

    #Simple itteration

    #x1 = 1.5333203767713983
    #x2 = 1.4362993438575313

    #Gauss Seidel

    #x1 = 1.5333418922347142
    #x2 = 1.4363056427402465

#coef = [-2, 0.9, 1.2, 0.6, 1.1, 2.4]

   #Simple itteration

   #x1 = -1.189928877531567
   #x2 = 1.7187628275937712

   #Gauss Zeidel

   #x1 = -1.1899305788948324
   #x2 = 1.718762998510423


#coef = [4.9, 10, -1.9, -0.4, 1.5, 3.6]
#coef = [1.8, 1.1, -1, 3.6, 8.1, -0.9]
#coef = [-1.2, 0.6, -1, 2, 10, -0.2]
#coef = [-4.4, -10, -1.7, 0.8, -10, -8.8]
#coef = [-2, -5, 12, -3.7, 2.3, 19]
var = [1, 1]
e = 0.000001


first_eq = SystemOfEquation(coef, o_list)
if tmp_cond(coef, var) < 1:
    first_eq.simple_itteration(var, e)
else:
    print("Метод не збіжний у даному випадку")