# Gia Buu Luong, Aymaan Mohammed
# ECE 241 - Project 3: App2, App3 and App4

from Movie import Movie
from MovieList import MovieList
import random


class Node:
    def __init__(self, movie, index=0):
        self.movie = movie
        self.left = None
        self.right = None
        self.index = index  # level-order position: left=2*i+1, right=2*i+2


class MovieBST:
    def __init__(self, filename):
        self.__root = None
        self.__size = 0

        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    movie_id, year, title = line.strip().split(";", 2)
                    self.insert(Movie(int(movie_id), int(year), title.strip()))

    def insert(self, movie):
        if self.__root is None:
            self.__root = Node(movie, 0)
            self.__size += 1
        else:
            self.__insert(self.__root, movie)

    def __insert(self, node, movie):
        # Tree is sorted by ID number
        if movie.getID() < node.movie.getID():
            if node.left is None:
                node.left = Node(movie, 2 * node.index + 1)
                self.__size += 1
            else:
                self.__insert(node.left, movie)
        elif movie.getID() > node.movie.getID():
            if node.right is None:
                node.right = Node(movie, 2 * node.index + 2)
                self.__size += 1
            else:
                self.__insert(node.right, movie)

    def getSize(self):
        return self.__size

    def search(self, movie_id):
        current = self.__root

        while current is not None:
            if movie_id == current.movie.getID():
                return current.movie
            elif movie_id < current.movie.getID():
                current = current.left
            else:
                current = current.right

        return None

    def displayInOrder(self):
        print("Display in order " + str(self.__size) + " items by ID")
        self.__displayInOrder(self.__root)

    def __displayInOrder(self, node):
        if node is not None:
            self.__displayInOrder(node.left)
            print(node.movie)
            self.__displayInOrder(node.right)

    def show(self):
        print("The BSTree looks like:")
        self.__show(self.__root, 0)

    def __show(self, node, level):
        if node is not None:
            # Right subtree appears above the root in the sideways tree.
            self.__show(node.right, level + 1)
            print("      " * level + str(node.movie.getID())
                  + "(" + str(node.index) + ")")
            self.__show(node.left, level + 1)

    def extractListInOrder(self, word):
        print("Begin sublist extraction for word:" + word
              + " using in-order traversal")
        userList = MovieList()
        self.__extractListInOrder(self.__root, word.lower(), userList)
        return userList

    def __extractListInOrder(self, node, word, userList):
        if node is not None:
            self.__extractListInOrder(node.left, word, userList)
            # Case-insensitive match on whole words of the title
            if word in node.movie.getTitle().lower().split():
                userList.append(node.movie)
            self.__extractListInOrder(node.right, word, userList)
