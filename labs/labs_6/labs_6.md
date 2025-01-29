# Лабораторная работа №6: Структуры данных

## Цель: Изучить структуры данных

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Структуры данных

`Структуры данных` — это способы организации и хранения данных так, чтобы их можно было эффективно использовать. Они помогают организовывать данные, обеспечивая удобный доступ и модификацию. Разные структуры данных оптимальны для различных задач, и выбор подходящей структуры может значительно повлиять на производительность программы.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Изменяемые структуры данных
`Изменяемые структуры данных` позволяют изменять их содержимое после создания. Это значит, что можно добавлять, удалять или изменять элементы, не создавая новую структуру.

К изменяемым структурам данных относятся:
- `list`
- `set`
- `dict`

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Неизменяемые структуры данных
`Неизменяемые структуры данных` не могут быть изменены после создания. Это значит, что любые операции, которые кажутся изменяющими данные, на самом деле создают новые объекты.
К неизменяемым структурам данных относятся:
- `tuple`
- `str`

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Списки (list)

Что это такое
---
`Список - list` — это упорядоченная коллекция элементов, которые могут быть изменены. Списки позволяют хранить элементы различных типов, включая другие списки.

Как создать
---
Создаются с помощью квадратных скобок [].
```python
my_list = [1, 2, 3]  # список с данными
empty_list = []  # пустой список
```

Какие типы может содержать
---
- Числа (int, float)
- Строки (str)
- Логические значения (bool)
- Списки (вложенные списки)
- Объекты пользовательских классов

```python
mixed_list = [1, "hello", 3.14, True, [5, 6]]
```

Доступ к элементам
---
Элементы списка можно получить по индексу, который начинается с 0. Также доступен отрицательный индекс для обращения к элементам с конца списка.

```python
my_list = [10, 20, 30, 40, 50]

# Доступ по положительному индексу
first_element = my_list[0]  # 10
third_element = my_list[2]   # 30

# Доступ по отрицательному индексу
last_element = my_list[-1]    # 50
second_last_element = my_list[-2]  # 40
```

Методы
---

Основные методы

list.append()
---

Метод `list.append()`

**Описание**: Добавляет элемент в конец списка.

**Пример**:
```python
my_list = [1, 2, 3]
my_list.append(4)
```
**Результат**: `[1, 2, 3, 4]`

---

list.extend()
---

Метод `list.extend()`

**Описание**: Добавляет элементы из итерации (например, списка) в конец списка.

**Пример**:
```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
```
**Результат**: `[1, 2, 3, 4, 5, 6]`

---

list.insert()
---

Метод `list.insert()`

**Описание**: Вставляет элемент на указанную позицию в списке.

**Пример**:
```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
```
**Результат**: `[1, 4, 2, 3]`

---

list.remove()
---

Метод `list.remove()`

**Описание**: Удаляет первый элемент из списка, равный указанному значению. Если элемент не найден, возникает ошибка.

**Пример**:
```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
```
**Результат**: `[1, 3, 2]`

---

list.pop()
---

Метод `list.pop()`

**Описание**: Удаляет и возвращает элемент по заданному индексу. Если индекс не указан, удаляется последний элемент.

**Пример**:
```python
my_list = [1, 2, 3]
item = my_list.pop()
```
**Результат**: `item = 3`, `my_list = [1, 2]`

---

list.index()
---

Метод `list.index()`

**Описание**: Возвращает индекс первого вхождения указанного элемента. Если элемент не найден, возникает ошибка.

**Пример**:
```python
my_list = [1, 2, 3]
index = my_list.index(2)
```
**Результат**: `index = 1`

---

list.count()
---

Метод `list.count()`

**Описание**: Возвращает количество вхождений указанного элемента в списке.

**Пример**:
```python
my_list = [1, 2, 3, 1]
count = my_list.count(1)
```
**Результат**: `count = 2`

---

list.sort()
---

Метод `list.sort()`

**Описание**: Сортирует элементы списка на месте. По умолчанию сортирует по возрастанию.

**Пример**:
```python
my_list = [3, 1, 2]
my_list.sort()
```
**Результат**: `[1, 2, 3]`

---

list.reverse()
---

Метод `list.reverse()`

**Описание**: Обращает порядок элементов в списке на месте.

**Пример**:
```python
my_list = [1, 2, 3]
my_list.reverse()
```
**Результат**: `[3, 2, 1]`

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Множества (set)

Что это такое
---

`Множество set` — это неупорядоченная коллекция уникальных элементов. Множества используются для операций, связанных с математическими множествами (объединение, пересечение и т.д.).

Как создать
---

Создаются с помощью фигурных скобок {} или функции set().

```python
my_set = {1, 2, 3}
empty_set = set()  # Пустое множество
```

Какие типы может содержать
---

- Числа (int, float)
- Строки (str)
- Кортежи (tuple)

> Важно: Множества не могут содержать изменяемые типы, такие как списки или другие множества.

Пример:
```python
mixed_set = {1, "hello", (2, 3)}
```

Доступ к элементам
---

В множествах нет прямого доступа по индексу, так как они неупорядоченные. Для получения элемента нужно использовать операции, такие как перебор, или преобразовать множество в список.

```python
my_set = {10, 20, 30}

# Перебор элементов
for element in my_set:
    print(element)

# Преобразование в список для доступа по индексу
set_as_list = list(my_set)
first_element = set_as_list[0]  # Доступ к первому элементу
```

Методы
---
Основные методы множества

set.add()
---

Метод `set.add()`

**Описание**: Добавляет элемент в множество. Если элемент уже присутствует, изменений не происходит.

**Пример**:
```python
my_set = {1, 2, 3}
my_set.add(4)
```
**Результат**: `{1, 2, 3, 4}`

---

set.remove()
---

Метод `set.remove()`

**Описание**: Удаляет указанный элемент из множества. Если элемент не найден, возникает ошибка.

**Пример**:
```python
my_set = {1, 2, 3}
my_set.remove(2)
```
**Результат**: `{1, 3}`

---

set.discard()
---

Метод `set.discard()`

**Описание**: Удаляет указанный элемент из множества, если он существует. Если элемент не найден, ничего не происходит.

**Пример**:
```python
my_set = {1, 2, 3}
my_set.discard(2)
```
**Результат**: `{1, 3}`
```python
my_set.discard(4)  # Нет ошибки, так как элемент не найден
```

---

set.pop()
---

Метод `set.pop()`

**Описание**: Удаляет и возвращает произвольный элемент из множества. Если множество пусто, возникает ошибка.

**Пример**:
```python
my_set = {1, 2, 3}
item = my_set.pop()
```
**Результат**: `item` — произвольный элемент из множества, например, `1`, а множество может стать `{2, 3}`.

---

set.union()
---

Метод `set.union()`

**Описание**: Возвращает новое множество, состоящее из всех уникальных элементов, присутствующих в обоих множествах.

**Пример**:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
```
**Результат**: `{1, 2, 3, 4, 5}`

---

set.intersection()
---

Метод `set.intersection()`

**Описание**: Возвращает новое множество, состоящее из общих элементов двух множеств.

**Пример**:
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
```
**Результат**: `{2, 3}`

---

set.difference()
---

Метод `set.difference()`

**Описание**: Возвращает новое множество, состоящее из элементов, присутствующих в первом множестве, но отсутствующих во втором.

**Пример**:
```python
set1 = {1, 2, 3}
set2 = {2, 4}
result = set1.difference(set2)
```
**Результат**: `{1, 3}`

---

set.symmetric_difference()
---

Метод `set.symmetric_difference()`

**Описание**: Возвращает новое множество, состоящее из элементов, присутствующих в одном из множеств, но не в обоих.

**Пример**:
```python
set1 = {1, 2, 3}
set2 = {2, 4}
result = set1.symmetric_difference(set2)
```
**Результат**: `{1, 3, 4}`

---

set.clear()
---

Метод `set.clear()`

**Описание**: Удаляет все элементы из множества, оставляя его пустым.

**Пример**:
```python
my_set = {1, 2, 3}
my_set.clear()
```
**Результат**: `set()` (пустое множество)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Словари (dict)

Что это такое
---

Словарь — это коллекция пар "ключ-значение". Он позволяет быстро получать значение по ключу. Словари неупорядочены и могут содержать элементы различных типов.

Как создать
---

Создаются с помощью фигурных скобок {}.

```python
my_dict = {'a': 1, 'b': 2}
empty_dict = {}  # Пустой словарь
```

Какие типы может содержать
---

Ключи: Должны быть хэшируемыми (например, числа, строки, кортежи).
Значения: Могут быть любого типа (включая списки, множества и другие словари).

```python
mixed_dict = {
    'integer': 1,
    'string': "hello",
    'list': [1, 2, 3],
    'set': {4, 5},
    'tuple': (6, 7)
}
```

Доступ к элементам
---

Доступ к значениям словаря осуществляется по ключам. Если ключ отсутствует, можно использовать метод get(), чтобы избежать ошибки.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Доступ по ключу
value_a = my_dict['a']  # 1
value_b = my_dict.get('b')  # 2

# Доступ к несуществующему ключу с использованием get()
value_d = my_dict.get('d', 'Not Found')  # 'Not Found'
```

Методы
---

Основные методы словаря

dict.get()
---

Метод `dict.get()`

**Описание**: Возвращает значение по указанному ключу. Если ключ не найден, возвращает значение по умолчанию (если указано) или `None`.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
value = my_dict.get('a')
```
**Результат**: `value = 1`

---

dict.keys()
---

Метод `dict.keys()`

**Описание**: Возвращает представление всех ключей словаря.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
keys = my_dict.keys()
```
**Результат**: `keys = dict_keys(['a', 'b'])`

---

dict.values()
---

Метод `dict.values()`

**Описание**: Возвращает представление всех значений словаря.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
values = my_dict.values()
```
**Результат**: `values = dict_values([1, 2])`

---

dict.items()
---

Метод `dict.items()`

**Описание**: Возвращает представление всех пар "ключ-значение" в словаре.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
items = my_dict.items()
```
**Результат**: `items = dict_items([('a', 1), ('b', 2)])`

---

dict.update()
---

Метод `dict.update()`

**Описание**: Обновляет словарь, добавляя пары "ключ-значение" из другого словаря или итерируемого объекта.

**Пример**:
```python
my_dict = {'a': 1}
my_dict.update({'b': 2})
```
**Результат**: `my_dict = {'a': 1, 'b': 2}`

---

dict.pop()
---

Метод `dict.pop()`

**Описание**: Удаляет указанный ключ и возвращает соответствующее значение. Если ключ не найден, возникает ошибка.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
```
**Результат**: `value = 1`, `my_dict = {'b': 2}`

---

dict.popitem()
---

Метод `dict.popitem()`

**Описание**: Удаляет и возвращает последнюю добавленную пару "ключ-значение" в виде кортежа. Если словарь пуст, возникает ошибка.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
```
**Результат**: `item = ('b', 2)`, `my_dict = {'a': 1}`

---

dict.clear()
---

Метод `dict.clear()`

**Описание**: Удаляет все элементы из словаря, оставляя его пустым.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
```
**Результат**: `{}` (пустой словарь)

---

dict.copy()
---

Метод `dict.copy()`

**Описание**: Возвращает поверхностную копию словаря.

**Пример**:
```python
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
```
**Результат**: `new_dict = {'a': 1, 'b': 2}`

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Кортежи (tuple)

Что это такое
---

Кортеж — это упорядоченная коллекция элементов, которая является неизменяемой. Кортежи могут содержать элементы различных типов.

Как создать
---

Создаются с помощью круглых скобок ().

```python
my_tuple = (1, 2, 3)
empty_tuple = ()  # Пустой кортеж
```

Какие типы может содержать
---

Кортежи могут содержать элементы различных типов:
- Числа (int, float)
- Строки (str)
-Логические значения (bool)
- Другие кортежи

```python
mixed_tuple = (1, "hello", 3.14, True, (5, 6))
```

Доступ к элементам
---

Как и в списках, элементы кортежа доступны по индексу, который начинается с 0.

```python
my_tuple = (10, 20, 30)

# Доступ по положительному индексу
first_element = my_tuple[0]  # 10
third_element = my_tuple[2]   # 30

# Доступ по отрицательному индексу
last_element = my_tuple[-1]    # 30
```

Методы
---

Основные методы кортежа

tuple.count()
---

Метод `tuple.count()`

**Описание**: Возвращает количество вхождений указанного элемента в кортеже.

**Пример**:
```python
my_tuple = (1, 2, 3, 1)
count = my_tuple.count(1)
```
**Результат**: `count = 2`

---

tuple.index()
---

Метод `tuple.index()`

**Описание**: Возвращает индекс первого вхождения указанного элемента в кортеже. Если элемент не найден, возникает ошибка.

**Пример**:
```python
my_tuple = (1, 2, 3)
index = my_tuple.index(2)
```
**Результат**: `index = 1`
```python
# Если элемента нет, возникнет ошибка
# index = my_tuple.index(4)  # ValueError
```

---

> Так как кортежи неизменяемы, у них нет методов для изменения или удаления элементов, а также методов, которые бы возвращали новые кортежи. 

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Grapes.png" alt="Grapes" width="30" height="30" style="vertical-align: middle"/> Строки (str)

Что это такое
---

Строка — это последовательность символов, представляющая текст. Строки являются неизменяемыми.

Как создать
---

Создаются с помощью одинарных '' или двойных "" кавычек.

```python
my_string = "Hello, World!"
empty_string = ""  # Пустая строка
```

Какие типы может содержать
---

- Строки могут содержать:
- Буквы (латиница, кириллица и другие алфавиты)
- Цифры
- Специальные символы

```python
mixed_string = "123, Hello, @#$%"
```

Методы
---

Основные методы строк

str.lower()
---

Метод `str.lower()`

**Описание**: Возвращает копию строки, в которой все символы приведены к нижнему регистру.

**Пример**:
```python
my_string = "Hello, World!"
result = my_string.lower()
```
**Результат**: `result = "hello, world!"`

---

str.upper()
---

Метод `str.upper()`

**Описание**: Возвращает копию строки, в которой все символы приведены к верхнему регистру.

**Пример**:
```python
my_string = "Hello, World!"
result = my_string.upper()
```
**Результат**: `result = "HELLO, WORLD!"`

---

str.strip()
---

Метод `str.strip()`

**Описание**: Возвращает копию строки с удалёнными начальными и конечными пробелами (или указанными символами).

**Пример**:
```python
my_string = "   Hello, World!   "
result = my_string.strip()
```
**Результат**: `result = "Hello, World!"`

---

str.replace()
---

Метод `str.replace()`

**Описание**: Возвращает копию строки, в которой все вхождения подстроки `old` заменены на `new`.

**Пример**:
```python
my_string = "Hello, World!"
result = my_string.replace("World", "Python")
```
**Результат**: `result = "Hello, Python!"`

---

str.split()
---

Метод `str.split()`

**Описание**: Разделяет строку на список подстрок по указанному разделителю. По умолчанию используется пробел.

**Пример**:
```python
my_string = "Hello, World!"
result = my_string.split()
```
**Результат**: `result = ["Hello,", "World!"]`

---

str.join()
---

Метод `str.join()`

**Описание**: Объединяет элементы итерируемого объекта (например, списка) в строку, используя строку как разделитель.

**Пример**:
```python
my_list = ["Hello", "World"]
result = " ".join(my_list)
```
**Результат**: `result = "Hello World"`

---

str.find()
---

Метод `str.find()`

**Описание**: Возвращает индекс первого вхождения подстроки в строке. Если подстрока не найдена, возвращает -1.

**Пример**:
```python
my_string = "Hello, World!"
index = my_string.find("World")
```
**Результат**: `index = 7`
```python
# Если подстрока не найдена
# index = my_string.find("Python")  # -1
```

---

str.isdigit()
---

Метод `str.isdigit()`

**Описание**: Возвращает True, если все символы строки являются цифрами и в строке есть хотя бы один символ. Иначе возвращает False.

**Пример**:
```python
my_string = "123"
result = my_string.isdigit()
```
**Результат**: `result = True`
```python
my_string = "123a"  # result = False
```

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Hourglass%20Not%20Done.png" alt="Hourglass Not Done" width="35" height="35" /> Лабораторная работа 


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 1: Анализ доходов

**Описание задания**: Напишите программу для анализа доходов группы людей. Для этого:
- Попросите пользователя ввести доходы людей (разделяя их пробелами).
- Сохраните данные в списке.
- Вычислите и выведите:
  - Средний доход.
  - Максимальный и минимальный доход.
  - Медиану доходов (для вычисления медианы отсортируйте список).
  - Моду
  - Дисперсию
  - СКО

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 2: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 3: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 4: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 5: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 6: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 7: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 8: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 9: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 10: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 11: ???

**Описание задания**: 

---

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 12: ???

**Описание задания**: 

___

[Вернуться на главную страницу](https://valeogamer.github.io/Python_2024_MarSU/)