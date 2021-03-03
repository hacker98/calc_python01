import random
import operator
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
from time import sleep
from multiprocessing import Pool, current_process
from multiprocessing import Process
import time
import os


operators = [("+", operator.add), ("-", operator.sub), ("*", operator.mul), ('/', operator.truediv)]


data_size = 200


def data_generator(data_size):
    data_list = []
    for i in range(1, data_size):
        number1 = random.randint(1, 2000)
        number2 = random.randint(1, 2000)
        op, fn = random.choice(operators)
        data = {"num1": number1, "num2": number2, "operator": op}
        # print(data)
        data_list.append(data)
    return data_list


def sequential_execution(dataset):
    # """
    #
    # :param dataset:
    # :return:
    # """
    result_list = []
    for data in dataset:
        num1 = data["num1"]
        num2 = data["num2"]
        oper = data["operator"]
        if oper == "+":
            res = operator.add(num1, num2)
        elif oper == "-":
            res = operator.sub(num1, num2)
        elif oper == "*":
            res = operator.mul(num1, num2)
        elif oper == "/":
            res = operator.truediv(num1, num2)
        else:
            res = 0
        res_dict = {"num1": num1, "num2": num2, "operator": oper, "result": res}
        result_list.append(res_dict)
    return result_list


def task(in_data):
    """

    :param in_data:
    :return:
    """
    print( in_data)
    num1 = in_data["num1"]
    num2 = in_data["num2"]
    oper = in_data["operator"]
    if oper == "+":
        res = operator.add(num1, num2)
    elif oper == "-":
        res = operator.sub(num1, num2)
    elif oper == "*":
        res = operator.mul(num1, num2)
    elif oper == "/":
        res = operator.truediv(num1, num2)
    else:
        res = 0
    res_dict = {"num1": num1, "num2": num2, "operator": oper, "result": res}
    print( res_dict)
    return res_dict


def parallel_threading(data_list):
    # """
    #
    # :param data_list:
    # :return:
    # """
    pool = ThreadPool(10)
    results = pool.map(task, data_list)
    pool.close()
    pool.join()
    return results
    print(result)
    print(out_data)





 def processing(data_list):
   # print('hello', name)
   for i in range(1,data_size)
       pool.apply_async(processing, data_list)
  pool = multiprocessing.pool(process=5)
    p = Process(task,data_list)
    p.start()
    p.join()
    return results
    print(result)
    print(out_data)


# print("Select operation:")
# print("1.sequential")
# print("2.multithreading")
# print("3.Multiprocessing")

