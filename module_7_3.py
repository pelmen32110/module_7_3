'''
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
'''
import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем переданные названия файлов в атрибут
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        # Обходим все переданные файлы
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем весь текст файла, приводим к нижнему регистру и убираем пунктуацию
                    text = file.read().lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(char, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                # Если файл не найден, записываем пустой список
                all_words[file_name] = []
        return all_words

    def find(self, word):
        # Находим первую позицию слова в каждом файле
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)+1 #начинам с 0, так что делаем +1 для классической нумерации с 1
            else:
                result[name] = 0  # Если слово не найдено
        return result

    def count(self, word):
        # Подсчитываем количество вхождений слова в каждом файле
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
