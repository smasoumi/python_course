# import multiprocessing

# square_result=[]

# def calc_square(numbers):
#     global square_result
#     for n in numbers:
#         print('square:', n*n)
#         square_result.append(n*n)
#     # result must be printed inside the process
#     print('result within the process', square_result)

# if __name__ == '__main__':
#     numbers=[2,3,8,9]
#     p1 = multiprocessing.Process(target=calc_square, args=(numbers,))
#     p1.start()
#     p1.join()
#     # a new space of square_result is created inside the process p1
#     # p1 cannot access to a global variable square_result
#     print('result: ', square_result)
#     print('Done!')

import multiprocessing
import multiprocessing.shared_memory


def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == '__main__':
    numbers=[2,3,8,9]
    # to share data between processes
    result = multiprocessing.Array('i',4) # 'i' means integer, 'd' means double

    p1 = multiprocessing.Process(target=calc_square, args=(numbers, result))

    p1.start()
    p1.join()

    print('result: ', result[:])
    print('Done!')