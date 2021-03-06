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
            n, _nlinks = tuple(int(i) for i in f.readline()[:-1].split())  # n - amount of titles, _nlinks - amount of links
            self.n, self._nlinks = n, _nlinks

            self._titles = []  # name of titles
            self._sizes = array.array('L', [0] * n)  # size of title
            self._links = array.array('L', [0] * _nlinks)  # a line of links (it includes ALL links)
            self._redirect = array.array('B', [0] * n)  # a line of redirections
            self._offset = array.array('L', [0] * (n + 1))  # a line of keys that shows a connection between links and titles

            number = 0
            Matrix = {}

            for line in range(n):
                self._titles.append(f.readline()[:-1])
                size, flag, links = tuple(int(i) for i in f.readline()[:-1].split())
                self._sizes[line] = size
                self._offset[line] = number

                if flag == 1:
                    self._redirect[line] = True
                else:
                    self._redirect[line] = False

                for one in range(links):
                    Matrix[self._titles[line]].add(one)
                    self._links[number + one] = int(f.readline()[:-1])
                number += links

        print('Граф загружен')
        f.close()

    def get_number_of_links_from(self, _id): #amount of links
        if _id != self.n-1:
            number_of_links_from = self._offset[_id+1] - self._offset[_id]
        else:
            number_of_links_from = 1
        return number_of_links_from

    def get_links_from(self, _id):  #links
        links_from = self._links[self._offset[_id]:self._offset[_id + 1]]
        return links_from

    def get_id(self, title):   #id
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self.n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):    #name of title
        return self._titles[_id]

    def get_page_size(self, _id):   #size (byte)
        return self._sizes[id]

    def get_number_of_all_links(self):
        return self._nlinks


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


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

        # TODO: статистика и гистограммы


    print('Количество статей с перенаправлениями', sum(1 for i in range(wg.get_number_of_pages()) if wg.is_redirect(i)==True))

    M = [0] * wg.get_number_of_pages()     #M-массив количества ссылок из статьи,
    for i in range(wg.get_number_of_pages()):
        M[i] = wg.get_number_of_links_from(i)

    print(M)

    print('Минимальное количество ссылок из статьи', min(M))
    print('Количество статей с минимальным количеством ссылок', sum(1 for i in range(len(M))
                                                                    if wg.get_number_of_links_from(i) == min(M)))
    Max_title = max(wg.get_number_of_links_from(i) for i in range(wg.get_number_of_pages()))

    print('Максимальное количество ссылок из статьи', max(M))
    print('Количество статей с максимальным количеством ссылок', sum(1 for i in range(len(M))
                                                                    if wg.get_number_of_links_from(i) == Max_title))

    Matrix = []  #tuple of names that have the biggest amounts of links
    for i in range(wg.get_number_of_pages()):
        if wg.get_number_of_links_from(i) == Max_title:
            Matrix.append(wg.get_title(i))

    print('Cтатья с наибольшим количеством ссылок', [i for i in Matrix])

    print('Cреднее количество ссылок в статье', statistics.mean(M))

    matrix = [0] * wg.get_number_of_pages()    #tuple of links ON the article
    for i in range(wg.get_number_of_pages()):
        for one in wg.get_links_from(i):
            matrix[one] += 1

    print('Минимальное количество ссылок на статью', min(matrix))
    print('Mаксимальное количество ссылок на статью', max(matrix))

    Min_number, Max_number = 0, 0
    Name = []
    for one in range(len(matrix)):
        if matrix[one] == int(min(matrix)):
            Min_number += 1
        elif matrix[one] == int(max(matrix)):
            Max_number += 1
            Name.append(wg.get_title(one))

    print('Kоличество статей с минимальным количеством внешних ссылок', Min_number)
    print('Количество статей с максимальным количеством внешних ссылок', Max_number)
    print('Cтатья с наибольшим количеством внешних ссылок', Name)
    print('Среднее количество внешних ссылок на статью', statistics.mean(matrix))


    print('Минимальное количество перенаправлений на статью', )

    print(Matrix)








