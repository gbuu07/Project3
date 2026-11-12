# Gia Buu Luong
# ECE 241 - Project 3: App1 and App4

from Movie import Movie
import random

class MovieList:
    def __init__(self, filename=None):
        self.__movies = []

        # No filename gives an empty list (used by MovieBST.extractListInOrder)
        if filename is None:
            return

        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    movie_id, year, title = line.strip().split(";", 2)
                    movie = Movie(int(movie_id), int(year), title.strip())
                    self.__movies.append(movie)

    def append(self, movie):
        self.__movies.append(movie)

    def getSize(self):
        return len(self.__movies)

    def binarySearch(self, movie_id):
        # The list must be sorted by ID before calling this method.
        low = 0
        high = self.getSize() - 1

        while low <= high:
            mid = (low + high) // 2
            movie = self.__movies[mid]

            if movie.getID() == movie_id:
                return movie
            elif movie.getID() < movie_id:
                low = mid + 1
            else:
                high = mid - 1

        return None

    def shuffle(self):
        random.shuffle(self.__movies)

    def save(self, filename):
        with open(filename, "w") as file:
            for movie in self.__movies:
                file.write(str(movie) + "\n")

    def display(self):
        for movie in self.__movies:
            print(movie)
