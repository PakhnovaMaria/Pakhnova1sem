import os
import sys
import math

import array

import statistics

from matplotlib import rc

rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):

        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            n, n_links = tuple(int(i) for i in f.readline()[:-1].split())  # n - amount of titles, _nlinks - amount of links
            self.n, self.n_links = n, n_links

            self._titles = []  # name of titles
            self._sizes = array.array('L', [0] * n)  # size of title
            self._links = array.array('L', [0] * n_links)  # a line of links (it includes ALL links)
            self._offset = array.array('L', [0] * (n + 1))  # a line of keys that shows a connection between links and titles
            self._redirect = array.array('B', [0] * n)  # a line of redirections

            number = 0
            way_links = {}

            for line in range(n):
                self._titles.append(f.readline()[:-1])
                size, flag, links = tuple(int(i) for i in f.readline()[:-1].split())
                self._sizes[line] = size
                self._offset[line] = number

                if flag == 1:
                    self._redirect[line] = True
                else:
                    self._redirect[line] = False

                for One in range(links):
                    self._links[number + One] = int(f.readline()[:-1])
                    if self._titles[line] not in way_links:
                        way_links[self._titles[line]] = {One: self._links[number + One]}
                    else:
                        way_links[self._titles[line]][One] = self._links[number + One]

                number += links
        self.way_links = way_links
        print('Граф загружен')
        f.close()

    def get_number_of_links_from(self, _id):  # amount of links
        if _id != self.n-1:
            number_of_links_from = self._offset[_id+1] - self._offset[_id]
        else:
            number_of_links_from = self.n_links - self._offset[_id]
        return number_of_links_from

    def get_links_from(self, _id):  # links
        links_from = self._links[self._offset[_id]:self._offset[_id + 1]]
        return links_from

    def get_id(self, title):   # id
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self.n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):    # name of title
        return self._titles[_id]

    def get_page_size(self, _id):   # size (byte)
        return self._sizes[_id]

    def get_number_of_all_links(self):
        return self.n_links

    def get_matrix_of_way(self):    # словарь вида: статья - ссылки (названные словами)
        for i in self.way_links:
            number = 0
            for _ in self.way_links[i]:
                number += 1
            for num in range(number):
                name2 = self._titles[self.way_links[i][num]]
                self.way_links[i][num] = name2
        return self.way_links


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.hist(x=data, bins=bins, facecolor=facecolor, alpha=alpha, **kwargs)
    plt.savefig(fname, transparent=transparent)


def bfs_fired(G, start, fired):
    Q = [start]
    fired.add(start)
    while len(Q) != 0:
        current = Q.pop(0)
        neighbour = 0
        while neighbour != wg.get_number_of_links_from(wg.get_id(current)):
            if G[current][neighbour] not in fired:
                fired.add(G[current][neighbour])
                Q.append(G[current][neighbour])
                neighbour += 1
    return fired

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    M = [0] * wg.get_number_of_pages()     # M-массив количества ссылок из статьи,
    for i in range(wg.get_number_of_pages()):
        M[i] = wg.get_number_of_links_from(i)

    Matrix = []  # tuple of names that have the biggest amounts of links
    for i in range(wg.get_number_of_pages()):
        if wg.get_number_of_links_from(i) == max(M):
            Matrix.append(wg.get_title(i))

    matrix = [0] * (wg.get_number_of_pages())    # массив ссылок НА статью
    for i in range(wg.get_number_of_pages()):
        if not wg.is_redirect(i):     # условие проверки перенаправления, перенаправление не является внешней ссылкой
            for one in wg.get_links_from(i):
                matrix[one] += 1

    Min_number, Max_number = 0, 0
    Name_title = []
    for one in range(len(matrix)):
        if matrix[one] == int(min(matrix)):
            Min_number += 1
        elif matrix[one] == int(max(matrix)):
            Max_number += 1
            Name_title.append(wg.get_title(one))

    matrix1 = [0] * (wg.get_number_of_pages())    # массив ссылок НА статью
    for i in range(wg.get_number_of_pages()):
        if wg.is_redirect(i):     # условие проверки перенаправления
            for one in wg.get_links_from(i):
                matrix1[one] += 1

    Min_number1, Max_number1 = 0, 0
    Name_1 = []
    for one in range(len(matrix1)):
        if matrix1[one] == int(min(matrix1)):
            Min_number1 += 1
        elif matrix1[one] == int(max(matrix1)):
            Max_number1 += 1
            Name_1.append(wg.get_title(one))

    print('Количество статей с перенаправлениями', sum(1 for i in range(wg.get_number_of_pages())
                                                       if wg.is_redirect(i) == True))

    print('Минимальное количество ссылок из статьи', min(M))

    print('Количество статей с минимальным количеством ссылок', sum(1 for i in range(len(M))
                                                                  if wg.get_number_of_links_from(i) == min(M)))

    print('Максимальное количество ссылок из статьи', max(M))

    print('Количество статей с максимальным количеством ссылок', sum(1 for i in range(len(M))
                                                                    if wg.get_number_of_links_from(i) == max(M)))

    print('Cтатья с наибольшим количеством ссылок', [i for i in Matrix])

    print('Cреднее количество ссылок в статье', round(statistics.mean(M), 2))

    print('Минимальное количество ссылок на статью', min(matrix))

    print('Mаксимальное количество ссылок на статью', max(matrix))

    print('Kоличество статей с минимальным количеством внешних ссылок', Min_number)

    print('Количество статей с максимальным количеством внешних ссылок', Max_number)

    print('Cтатья с наибольшим количеством внешних ссылок', Name_title)

    print('Среднее количество внешних ссылок на статью', round(statistics.mean(matrix), 2))

    print('Минимальное количество перенаправлений на статью', min(matrix1))

    print('Максимальное количество перенаправлений на статью', max(matrix1))

    print('Количество статей с минимальным количеством внешних перенаправлений', Min_number1)

    print('Количество статей с максимальным количеством внешних перенаправлений', Max_number1)

    print('Статья с наибольшим количеством внешних перенаправлений', Name_1)

    print('Cреднее количество внешних перенаправлений на статью', round(statistics.mean(matrix1), 2))


"""    hist(fname='first.png', data=M, bins=200, xlabel='Количество статей', ylabel="Количество ссылок",
         title="Распределение количества ссылок из статьи")
    hist(fname='second.png', data=matrix, bins=200, xlabel='Количество статей',
         ylabel="Количество ссылок", title="Распределение количества ссылок на статью")
    hist(fname='third.png', data=matrix1, bins=50, xlabel='Количество статей', ylabel="Количество ссылок",
         title="Распределение количества редиректов на статью")
    hist(fname='forth.png', data=[wg._sizes[i] for i in range(wg.n)], bins=50, xlabel='Количество статей',
         ylabel="Количество ссылок", title="Распределение размеров статей")   """

"""     start = 'Python'
    finish = 'Cписок файловых систем'

    Bfs_fired = bfs_fired(wg.get_matrix_of_way(), start, set())

    if finish not in Bfs_fired:
        print('переход невозможен')
    else:
        print('переход возможен')
        way = []
        current = finish
        for i in Bfs_fired:
            if i == start:
                print(way)
            if current in get_matrix_of_way[i]:
                way.append(i)
                current = i   """
