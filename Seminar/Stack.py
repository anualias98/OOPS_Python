"""Implementation Using List"""
# initial empty stack
# my_stack = []
#
# # append() function to push
# # element in the my_stack
# my_stack.append('x')
# my_stack.append('y')
# my_stack.append('z')
#
# print(my_stack)
#
# # pop() function to pop
# # element from my_stack in
# # LIFO order
# print('\nElements poped from my_stack:')
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())
#
# print('\nmy_stack after elements are poped:')
# print(my_stack)

""" Implementation using collection.deque"""
# from collections import deque
#
# my_stack = deque()
#
# # append() function is used to push
# # element in the my_stack
# my_stack.append('a')
# my_stack.append('b')
# my_stack.append('c')
#
# print('Initial my_stack:')
# print(my_stack)
#
# # pop() function is used to pop
# # element from my_stack in
# # LIFO order
# print('\nElements poped from my_stack:')
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())
#
# print('\nmy_stack after elements are poped:')
# print(my_stack)

# Implementing stack using the queue module
# # from queue import LifoQueue
# #
# # # Initializing a my_stack stack with maxsize
# # my_stack = LifoQueue(maxsize=5)
# #
# # # qsize() display the number of elements
# # # in the my_stack
# # print(my_stack.qsize())
# #
# # # put() function is used to push
# # # element in the my_stack
# # my_stack.put('x')
# # my_stack.put('y')
# # my_stack.put('z')
# #
# # print("Stack is Full: ", my_stack.full())
# # print("Size of Stack: ", my_stack.qsize())
# #
# # # To pop the element we used get() function
# # # from my_stack in
# # # LIFO order
# # print('\nElements poped from the my_stack')
# # print(my_stack.get())
# print(my_stack.get())
# print(my_stack.get())
#
# print("\nStack is Empty: ", my_stack.empty())
#

# stack=[]
# def push():
#     element=input("Enter the element:")
#     stack.append(element)
#     print(stack)
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         e=stack.pop()
#         print("removed element:",e)
#         print(stack)
# while True:
#     print("Select the operation 1.push 2.pop 3.quit")
#     choice=int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         break
#     else:
#         print("Enter the correct operation")


#
# stack=[]
# def push():
#     if len(stack)==n:
#         print("list is full")
#     else:
#         element=input("Enter the element:")
#         stack.append(element)
#         print(stack)
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         e=stack.pop()
#         print("removed element:",e)
#         print(stack)
# n=int(input("limit of stack"))
# while True:
#     print("Select the operation 1.push 2.pop 3.quit")
#     choice=int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         break
#     else:
#         print("Enter the correct operation")


