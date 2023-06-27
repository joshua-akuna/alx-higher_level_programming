#!/usr/bin/python3
"""A definition for the Node class"""


class Node:
    """A constructor for the Node class which initializes the
        data and next_node values of the current instance"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """A setter for the data property"""
    @property
    def data(self):
        return (self.__data)

    """A getter for the data property"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    """A getter for the next_node property"""
    @property
    def next_node(self):
        return (self.__next_node)

    """A setter for the next_node property"""
    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""A definition for the Node class"""


class SinglyLinkedList:
    """A constructor for the SinglyLinkedList class which initializes
        the head property"""
    def __init__(self):
        self.head = None

    """This function inserts a node into the linked list at the sorted
        position in an increasing order"""
    def sorted_insert(self, value):
        if not self.head:
            self.head = Node(value)
        elif value < self.head.data:
            self.head = Node(value, self.head)
        else:
            node = self.head
            while node.next_node and node.next_node.data < value:
                node = node.next_node
            if node.next_node is None:
                node.next_node = Node(value)
            else:
                node.next_node = Node(value, node.next_node)

    """this function return a string representation of the
        current class instance"""
    def __repr__(self):
        res = ''
        node = self.head
        while node:
            res += str(node.data)
            if node.next_node:
                res += '\n'
            node = node.next_node
        return (res)
