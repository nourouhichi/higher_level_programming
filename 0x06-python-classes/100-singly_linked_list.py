#!/usr/bin/python3
"""module Node"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


    @property
    def data(self):
        return self.__data


    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        return self.__next_node


    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

class SinglyLinkedList(Node):
    """singly linked list class"""
    def __init__(self):
        self.__head = None

    def __repr__(self):
        runner = self.__head
        data_string = ""

        
        while runner:
            data_string += str(runner.data)
            runner = runner.next_node
            if runner.next_node is None:
                break
            data_string += '\n'
        return data_string


    def sorted_insert(self, value):
        new = Node(value, None)
        roadrunner = self.__head
        run = self.__head
        i = 0


        if self.__head is None:
            self. __head = new
            return
        while roadrunner:
            while roadrunner.data < value and roadrunner.next_node:
                roadrunner = roadrunner.next_node
                i += 1
            for j in range(i - 1):
                    run = run.next_node
            bowl = run.next_node
            run.next_node = new
            new.next_node = bowl
            return
        roadrunner.next_node = new
        return
