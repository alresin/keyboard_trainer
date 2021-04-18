# Клавиатурный тренажер

## Описание временного состояния и заметки

### Изменения внесенные с последней версии
* Добавлен файл `requirements.txt` (с новыми необходимыми библиотками)
* Добавлен минимальный размер окна
* Добавлена возможность выхода в процессе ввода текста
* Добавлена возможность просмотра клавиш с ошибками в виде heatmap
* Добавлена возможность загрузки текста из файла

### Описание текущего состояние
Имеется рабочее GUI с возможностью ввода текста и дальнейшего его ввода с отображением только правильно набранных букв.
Отображется скорость печати и количестве ошибок отображается после завершения печати
Отображаются клавиши с наибольшим количеством ошибок на них.
Статистика ошибок и скорости сохраняется в файл и есть возможность ее очистки.
Отображение клавиш на вводе которых пользователь ошибается чаще всего с помощью matplotlib.
Имеется докуменатция ко всем функциям и классам.
Код приведен к pep8.

## Информация по запуску
Для запуска необходимы библиотеки kivy, matplotlib, numpy и easygui.
Информация по их установке и запуску приложения:

#### Windows CMD:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv_keyboard_train
kivy_venv_keyboard_train\Scripts\activate
python -m pip install -r requirements.txt
python ./main.py
```

#### Windows bash:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv_keyboard_train
source kivy_venv_keyboard_train/Scripts/activate
python -m pip install -r requirements.txt
python ./main.py
```

#### Linux:

```
python3 -m pip install --upgrade pip setuptools virtualenv
python3 -m virtualenv kivy_venv_keyboard_train
source kivy_venv_keyboard_train/bin/activate
python3 -m pip install -r requirements.txt
python3 ./main.py
```
