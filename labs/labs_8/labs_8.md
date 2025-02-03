# Лабораторная работа №8: Библиотеки

## Цель научиться использовать библиотеки

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="30" height="30" style="vertical-align: middle"/> Что такое библиотеки в Python?

Библиотеки в Python — это наборы готовых функций, классов и модулей, которые можно использовать для решения различных задач. Использование библиотек позволяет не писать код с нуля, а применять уже готовые решения, что ускоряет разработку программ и упрощает код.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="30" height="30" style="vertical-align: middle"/> Подключение библиотеки

Для использования библиотеки в Python необходимо её сначала импортировать. Для этого используется ключевое слово `import`.

**Пример:**
```python
import math  # Подключаем стандартную библиотеку math
print(math.sqrt(16))  # Выведет: 4.0 (квадратный корень из 16)
```
`import` — ключевое слово для подключения библиотеки.
После подключения библиотеки её функции можно использовать через точку, как `math.sqrt()`.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="30" height="30" style="vertical-align: middle"/> Стандартные библиотеки

Python имеет множество встроенных (стандартных) библиотек, которые не нужно устанавливать дополнительно. Рассмотрим несколько полезных:

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> Математические операции с библиотекой math

Библиотека `math` предоставляет функции для работы с математическими операциями, такими как вычисление квадратных корней, синусов, косинусов и другие.

### Основные математические операции

```python
import math

# Число Pi
print("Pi:", math.pi)  # Выведет значение числа Pi (примерно 3.141592653589793)

# Квадратный корень
print("Квадратный корень из 25:", math.sqrt(25))  # 5.0

# Факториал числа
print("Факториал 5:", math.factorial(5))  # 120

# Округление числа
print("Округление числа 4.7:", math.ceil(4.7))  # 5 (округление вверх)
print("Округление числа 4.3:", math.floor(4.3))  # 4 (округление вниз)
```

### Тригонометрические функции 
```python
import math
# Синус угла в радианах
angle = math.radians(30)  # Переводим градусы в радианы
print("Синус 30 градусов:", math.sin(angle))  # Синус 30 градусов = 0.5

# Косинус угла в радианах
print("Косинус 30 градусов:", math.cos(angle))  # Косинус 30 градусов = 0.8660254037844387

# Тангенс угла в радианах
print("Тангенс 30 градусов:", math.tan(angle))  # Тангенс 30 градусов = 0.5773502691896257

# Обратные тригонометрические функции
print("Арксинус 0.5:", math.degrees(math.asin(0.5)))  # 30.0 (переводим радианы обратно в градусы)
```
### Степени и логарифмы
```python
import math

# Возведение в степень
print("2 в степени 3:", math.pow(2, 3))  # 8.0

# Натуральный логарифм
print("Натуральный логарифм числа 10:", math.log(10))  # 2.302585092994046

# Логарифм по основанию 10
print("Логарифм по основанию 10 числа 1000:", math.log10(1000))  # 3.0

# Логарифм с произвольным основанием
print("Логарифм числа 16 по основанию 2:", math.log(16, 2))  # 4.0
```

### Прочие полезные функции
```python
import math

# Абсолютное значение
print("Абсолютное значение -7:", math.fabs(-7))  # 7.0

# Максимум и минимум из списка
print("Максимум из [1, 5, 3, 9]:", math.fmax(1, 5, 3, 9))  # 9
print("Минимум из [1, 5, 3, 9]:", math.fmin(1, 5, 3, 9))  # 1

# Преобразование углов из градусов в радианы
degrees = 45
radians = math.radians(degrees)
print(f"{degrees} градусов = {radians} радиан")

# Проверка, является ли число конечным
print("Is 2.5 finite?", math.isfinite(2.5))  # True
print("Is inf finite?", math.isfinite(float('inf')))  # False
```

___


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> Работа с датой и временем с библиотекой datetime
Библиотека `datetime` позволяет работать с датами и временем.

```python

import datetime
# Текущая дата и время
now = datetime.datetime.now()
print(now)  # Выведет текущую дату и время
# Форматирование даты
today = datetime.date.today()
print(today.strftime("%d-%m-%Y"))  # Выведет текущую дату в формате ДД-ММ-ГГГГ
```

___


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> Генерация случайных чисел с библиотекой random
Библиотека `random` используется для генерации случайных чисел, выборки из списков и других случайных операций.

```python

import random
# Генерация случайного числа от 1 до 10
print(random.randint(1, 10))  # Выведет случайное число от 1 до 10
# Перемешивание списка
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)  # Список будет перемешан
```

### Генерация случайного числа с плавающей запятой
```python
import random

# Генерация случайного числа с плавающей запятой от 0 до 1
print(random.random())  # Выведет случайное число от 0 до 1

# Генерация случайного числа с плавающей запятой в заданном диапазоне
print(random.uniform(1.5, 10.5))  # Выведет случайное число в диапазоне от 1.5 до 10.5
```

### Выбор случайного элемента из списка
```python
import random

# Список элементов
colors = ['red', 'blue', 'green', 'yellow', 'black']

# Выбор случайного элемента из списка
print(random.choice(colors))  # Выведет случайный цвет из списка
```

### Генерация случайной выборки (несколько случайных элементов) из списка
```python
import random

# Список элементов
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Выбор 3 случайных элементов из списка
print(random.sample(numbers, 3))  # Выведет 3 случайных числа из списка без повторений
```

### Подбрасывание монеты (случайное булево значение)
```python
import random

# Подбрасывание монеты
flip = random.choice(['Орёл', 'Решка'])
print(flip)  # Выведет либо 'Орёл', либо 'Решка'
```

### Генерация случайного числа с учетом вероятностей
```python
import random

# Список с элементами и их вероятностями
elements = ['apple', 'banana', 'cherry']
weights = [0.5, 0.3, 0.2]  # вероятности для каждого элемента

# Случайный выбор с учетом вероятностей
print(random.choices(elements, weights=weights))  # Может выбрать 'apple' с вероятностью 0.5 и т.д.
```

### Генерация случайного целого числа в диапазоне с шагом
```python
import random

# Генерация случайного числа от 0 до 100 с шагом 5
print(random.randrange(0, 101, 5))  # Выведет случайное число из множества: 0, 5, 10, 15, ...
```

### Генерация случайной последовательности чисел
```python
import random

# Генерация списка из 5 случайных чисел от 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(random_numbers)  # Список из 5 случайных чисел
```

### Генерация случайной строки
```python
import random
import string

# Генерация случайной строки длиной 8 символов
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(random_string)  # Сгенерирует строку из букв и цифр длиной 8 символов
```

### Подбрасывание игральной кости
```python
import random

# Подбрасывание игральной кости (1-6)
print(random.randint(1, 6))  # Выведет число от 1 до 6
```

### Генерация случайного пароля
```python
import random
import string

# Генерация случайного пароля длиной 12 символов (состоящего из букв и цифр)
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print(password)  # Сгенерирует случайный пароль
```


## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="30" height="30" style="vertical-align: middle"/> Установка внешних библиотек

Для использования сторонних `(не стандартных)` библиотек, нужно сначала их установить с помощью пакета `pip`.

**Пример установки библиотеки:**

1. Откройте командную строку или терминал. Если работаете в среде jupyter или colab, то пишем команду в ячейке для кода, но перед командой не забываем ставить `!`, как это показано ниже.
2. Выполните команду `!pip install numpy`
3. После установки можно использовать библиотеку в коде:
```python

import numpy as np
# Создание массива с использованием библиотеки numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Выведет: [1 2 3 4 5]
```

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="30" height="30" style="vertical-align: middle"/> Популярные внешние библиотеки
### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> NUMPY
`numpy` — работа с массивами и матрицами
Библиотека numpy предоставляет эффективные инструменты для работы с массивами и матрицами. Она поддерживает многомерные массивы и позволяет выполнять математические операции над ними.

```python
import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# Операции с массивами
arr2 = np.array([5, 4, 3, 2, 1])
print(arr + arr2)  # Выведет: [6 6 6 6 6]
```

### Создание многомерных массивов (матриц)
```python
import numpy as np

# Создание двумерного массива (матрицы)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Двумерная матрица:")
print(matrix)
```

### Индексация и срезы
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Доступ к элементам массива по индексу
print(arr[0])  # Первый элемент: 1
print(arr[-1])  # Последний элемент: 5

# Срезы
print(arr[1:4])  # Элементы с индексами 1, 2 и 3: [2 3 4]
print(arr[:3])  # Первые три элемента: [1 2 3]
```

### Операции с массивами
```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Сложение массивов
print(arr1 + arr2)  # [5 7 9]

# Умножение массива на скаляр
print(arr1 * 2)  # [2 4 6]

# Скалярное произведение
print(np.dot(arr1, arr2))  # 32 (1*4 + 2*5 + 3*6)
```

### Математические операции над массивами
```python
import numpy as np

arr = np.array([1, 4, 9, 16])

# Квадратный корень от каждого элемента массива
print(np.sqrt(arr))  # [1. 2. 3. 4.]

# Синус углов в радианах
print(np.sin(np.pi / 2))  # 1.0

# Экспонента для каждого элемента массива
print(np.exp(arr))  # [2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06]
```

### Создание массивов с использованием встроенных функций
```python
import numpy as np

# Массив из нулей
zeros = np.zeros((2, 3))  # 2x3 массив, заполненный нулями
print(zeros)

# Массив из единиц
ones = np.ones((3, 2))  # 3x2 массив, заполненный единицами
print(ones)

# Единичная матрица (диагональная матрица)
eye_matrix = np.eye(4)  # 4x4 единичная матрица
print(eye_matrix)

# Массив равномерно распределённых значений
linspace_arr = np.linspace(0, 10, 5)  # 5 элементов от 0 до 10
print(linspace_arr)

# Массив случайных чисел (равномерное распределение)
random_arr = np.random.rand(3, 3)  # 3x3 массив случайных чисел от 0 до 1
print(random_arr)
```

### Операции над матрицами
```python
import numpy as np

# Создание двумерных массивов (матриц)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Сложение матриц
C = A + B
print("Сложение матриц A и B:")
print(C)

# Умножение матриц
D = np.dot(A, B)
print("Умножение матриц A и B:")
print(D)

# Транспонирование матрицы
print("Транспонированная матрица A:")
print(A.T)

# Определитель матрицы
det_A = np.linalg.det(A)
print("Определитель матрицы A:", det_A)

# Обратная матрица
inv_A = np.linalg.inv(A)
print("Обратная матрица A:")
print(inv_A)
```

### Использование условных выражений с массивами
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Условие: элементы, больше 2
print(arr[arr > 2])  # [3 4 5]

# Применение функции (например, квадрат) к элементам массива, удовлетворяющим условию
arr[arr > 2] = arr[arr > 2] ** 2
print(arr)  # [ 1  2  9 16 25]
```

### Сложные операции с массивами
```python
import numpy as np

# Массивы случайных чисел
arr1 = np.random.randn(3, 3)  # Массив с 3x3 элементами, случайные числа с нормальным распределением
arr2 = np.random.randn(3, 3)

# Вычисление суммы элементов по строкам
row_sum = np.sum(arr1, axis=1)
print("Сумма по строкам:")
print(row_sum)

# Нахождение максимального значения в каждой строке
row_max = np.max(arr1, axis=1)
print("Максимальное значение по строкам:")
print(row_max)

# Транспонирование матрицы
arr1_T = arr1.T
print("Транспонированная матрица arr1:")
print(arr1_T)

# Поэлементное умножение двух матриц
elementwise_product = arr1 * arr2
print("Поэлементное умножение двух матриц:")
print(elementwise_product)
```

### Умножение матриц
```python
import numpy as np

# Умножение матриц
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Умножение матриц с использованием dot
result = np.dot(A, B)
print("Результат умножения матриц A и B:")
print(result)
```

### Работа с пропущенными значениями
```python
import numpy as np

# Создание массива с пропущенными значениями (NaN)
arr = np.array([1, 2, np.nan, 4, 5])

# Проверка на NaN
print(np.isnan(arr))  # [False False  True False False]

# Заменить NaN на 0
arr_no_nan = np.nan_to_num(arr, nan=0)
print(arr_no_nan)  # [1. 2. 0. 4. 5.]
```

### Расчет статистических показателей
```python
# Генерация случайных данных (нормальное распределение)
np.random.seed(42)  # Для воспроизводимости результатов
data = np.random.randn(100)  # 100 случайных чисел с нормальным распределением (среднее = 0, std = 1)
# Расчет статистических показателей
mean_value = np.mean(data)  # Среднее значение
median_value = np.median(data)  # Медиана
std_deviation = np.std(data)  # Стандартное отклонение
min_value = np.min(data)  # Минимальное значение
max_value = np.max(data)  # Максимальное значение
```

___


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> PANDAS

`pandas` — анализ и обработка данных
Библиотека pandas используется для работы с табличными данными, такими как CSV-файлы. С помощью pandas можно удобно манипулировать и анализировать данные.

```python
import pandas as pd
# Создание DataFrame
data = {'Имя': ['Аня', 'Борис', 'Вика'], 'Возраст': [20, 25, 22]}
df = pd.DataFrame(data)
print(df)
```

___


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Accordion.png" alt="Accordion" width="25" height="25" /> MATPLOTLIB

`matplotlib` — построение графиков
Библиотека matplotlib используется для визуализации данных, например, для построения графиков.


```python
import matplotlib.pyplot as plt
# Данные для графика
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# Построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График y = x^2')
plt.show()
```

### Линейный график с несколькими линиями
```python
import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

# Построение графиков
plt.plot(x, y1, label="y = x^2")
plt.plot(x, y2, label="y = 30 - x^2")

# Подписи и легенда
plt.xlabel('x')
plt.ylabel('y')
plt.title('Сравнение двух графиков')
plt.legend()

plt.show()
```

### Гистограмма
Гистограмма помогает визуализировать распределение данных.
```python
import matplotlib.pyplot as plt
import numpy as np

# Генерация случайных данных
data = np.random.randn(1000)

# Построение гистограммы
plt.hist(data, bins=30, color='blue', alpha=0.7)

# Подписи
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма случайных данных')
plt.show()
```

### График рассеяния (scatter plot)
График рассеяния используется для отображения точек, которые представляют собой пары значений.

```python
import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построение графика рассеяния
plt.scatter(x, y, color='red')

# Подписи
plt.xlabel('x')
plt.ylabel('y')
plt.title('График рассеяния')

plt.show()
```

### График с субплотами (subplots)
С помощью субплотов можно отображать несколько графиков в одном окне.
```python
import matplotlib.pyplot as plt

# Данные для графиков
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

# Создание фигуры с субплотами
fig, axs = plt.subplots(2)

# Первый график
axs[0].plot(x, y1)
axs[0].set_title('График y = x^2')

# Второй график
axs[1].plot(x, y2, color='green')
axs[1].set_title('График y = 30 - x^2')

# Подписи для осей
for ax in axs:
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.tight_layout()
plt.show()
```

### Точечный график с настройками размера точек
Можно изменить размер точек на графике, чтобы подчеркнуть важные элементы.
```python
import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sizes = [50, 100, 200, 300, 400]  # Размеры точек

# Построение графика рассеяния с размером точек
plt.scatter(x, y, s=sizes, color='purple', alpha=0.5)

# Подписи
plt.xlabel('x')
plt.ylabel('y')
plt.title('График рассеяния с разными размерами точек')

plt.show()
```

### График с несколькими осями (secondary axis)
Иногда необходимо добавить вторичную ось для отображения других данных.
```python
import matplotlib.pyplot as plt
import numpy as np

# Данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax1 = plt.subplots()

# Первый график (основная ось)
ax1.plot(x, y1, 'g-')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color='g')

# Вторичная ось
ax2 = ax1.twinx()  
ax2.plot(x, y2, 'b-')
ax2.set_ylabel('cos(x)', color='b')

plt.title('График с двумя осями')

plt.show()
```

### Круговая диаграмма (Pie Chart)
Круговая диаграмма может быть использована для отображения долей в общей сумме.
```python
import matplotlib.pyplot as plt

# Данные для круговой диаграммы
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Построение круговой диаграммы
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Подпись
plt.title('Круговая диаграмма')

plt.show()
```

### График функции с использованием NumPy
Когда функция имеет сложный вид, можно воспользоваться библиотекой NumPy для генерации данных.
```python
import matplotlib.pyplot as plt
import numpy as np

# Генерация данных
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# Построение графика
plt.plot(x, y, label='sin(x)', color='blue')

# Подписи
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции sin(x)')
plt.legend()

plt.show()
```


## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Hourglass%20Not%20Done.png" alt="Hourglass Not Done" width="35" height="35" /> Лабораторная работа

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 1: Основы работы с функциями библиотеки math

Напишите программу, которая выводит:
- Значение числа Pi (до 3 знаков после запятой).
- Квадратный корень из числа 144.
- Факториал числа 6.
- Число e (основание натуральных логарифмов).

Напишите программу, которая округляет число:
- 3.7 до ближайшего целого числа.
- -5.6 до ближайшего целого числа (округление вниз).

```yaml
**Пример вывода:**
Pi: 3.142
Квадратный корень из 144: 12.0
Факториал 6: 720
Число e: 2.718
Округление 3.7: 4
Округление -5.6: -6
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 2: Тригонометрия с помощью библиотеки math

Напишите программу, которая запрашивает у пользователя угол в градусах, переводит его в радианы, а затем выводит:
- Синус, косинус, тангенс, арксинус, арккосинус, арктангенс этого угла.

```yaml
**Пример вывода:**
Введите угол в градусах: 45
Синус: 0.7071067811865475
Косинус: 0.7071067811865476
Тангенс: 1.0
Арксинус: 0.7853981633974483
Арккосинус: 0.7853981633974483
Арктангенс: 0.7853981633974483
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 3: Логарифмические и степенные функции 

Напишите программу с помощью библиотеки math, которая вычисляет:
- Логарифм числа 1000 по основанию 10.
- Логарифм числа 16 по основанию 2.
- Натуральный логарифм числа 20.
Напишите программу, которая возводит число в степень:
- 2 в степени 10.
- 5 в степени 3.

```yaml
**Пример вывода:**
Логарифм 1000 по основанию 10: 3.0
Логарифм 16 по основанию 2: 4.0
Натуральный логарифм 20: 2.995732273553991
2 в степени 10: 1024.0
5 в степени 3: 125.0
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 4: Симуляция подбрасывания монеты

Напишите программу, которая симулирует подбрасывание монеты 100 раз. Программа должна подсчитать, сколько раз выпал `орёл` и сколько раз `решка`.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 5: Выбор случайного участника
Предположим, у вас есть список участников конкурса. Напишите программу, которая случайным образом выбирает одного победителя из списка и выводит его имя.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 6: Симуляция броска двух игральных костей
Напишите программу, которая симулирует бросок двух игральных костей. Повторите 1000 раз. Выведите наиболее часто выпадающеся число на костях.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 7: Статистические вычисления с массивом случайных чисел
Сгенерируйте массив из 100 случайных чисел с нормальным распределением (среднее 0, стандартное отклонение 1).

Вычислите:
- Среднее значение,
- Медиану,
- Стандартное отклонение,
- Минимальное и максимальное значение.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 8: Матричные операции
Создайте две матрицы размером 3x3, содержащие случайные числа в диапазоне от 1 до 10.

Выполните следующие операции:
- Поэлементное умножение этих матриц.
- Умножение матриц (матричное произведение) с использованием np.dot().
- Транспонирование первой матрицы.
- Вычисление определителя первой матрицы с помощью np.linalg.det().
- Для полученной матрицы после транспонирования найдите её обратную матрицу с помощью np.linalg.inv() (если она существует).

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 9: Фильтрация и изменение массива
- Создайте одномерный массив из 50 случайных целых чисел от -10 до 10.
- Выведите все положительные числа, которые больше 5.
- Все отрицательные числа в массиве замените на ноль.
- Измените все числа, которые делятся на 3, на их квадрат.
- После выполнения всех операций выведите обновленный массив.

**Подсказки:**

- Для генерации случайных целых чисел используйте np.random.randint().
- Для фильтрации массива можно использовать условия, как в примере arr[arr > 5].
- Чтобы заменить все элементы, которые делятся на 3, на их квадрат, используйте условие с arr % 3 == 0, и присваивайте квадрат элементов с помощью arr[arr % 3 == 0] = arr[arr % 3 == 0] ** 2.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 10: Построение графиков для нескольких функций
Построить на одном графике несколько функций: y=x^2, y=x^3, y=sin(x) в интервале от -10 до 10.

Использовать различные стили линий и цветов для каждой функции. Добавить легенду и соответствующие подписи для осей.

Требования:
- Легенда для каждой функции
- Подписи осей (x и y)
- Заголовок для графика


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 11:  График с субплотами для разных функций
Построить 2 графика на одном холсте. На первом из них отобразить функцию y=exp^x, а на втором функцию y=ln(x)

**Требования:**

- Разделить холст на два подграфика
- На первом графике отобразить y=exp^x
- На втором графике отобразить y=ln(x)
  
У каждого графика должен быть свой заголовок и подписи осей


___

[Вернуться на главную страницу](https://valeogamer.github.io/Python_2024_MarSU/)