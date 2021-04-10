# Клавиатурный тренажер

## Описание временного состояния и заметки

### Изменения внесенные с последней версии
* Логика отделена от GUI
* Добавлено отображение средней скорости за все время
* Добавлена сохранение статистики и возможность ее сброса
* Добавлено отображение клавиш на которых пользователь чаще всего ошибается
* Добавлена документация ко всем функциям и классам
* Размер окна меняется стандартным образом

### Описание текущего состояние
Имеется рабочее GUI с возможностью ввода текста и дальнейшего его ввода с отображением только правильно набранных букв.
Отображется скорость печати и количестве ошибок отображается после завершения печати
Отображаются клавиши с наибольшим количеством ошибок на них.
Статистика ошибок и скорости сохраняется в файл и есть возможность ее очистки.
Имеется докуменатция ко всем функциям и классам.
Код приведен к pep8.
Графическое состояние будет доработано в дальнейшем.
Возможность выйти в момент ввода кнопкой будет добавлена в дальнейшем.
Компиляция в .exe вероятна в дальнейшем.

## Информация по запуску
Для запуска необходима только библиотека kivy.
Информация по ее установке и запуску приложения:

#### Windows CMD:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv_keyboard_train
kivy_venv_keyboard_train\Scripts\activate
python -m pip install kivy
python ./main.py
```

#### Windows bash:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv_keyboard_train
source kivy_venv_keyboard_train/Scripts/activate
python -m pip install kivy
python ./main.py
```

#### Linux:

```
python3 -m pip install --upgrade pip setuptools virtualenv
python3 -m virtualenv kivy_venv_keyboard_train
source kivy_venv_keyboard_train/bin/activate
python3 -m pip install kivy
python3 ./main.py
```
