# Клавиатурный тренажер

## Описание временного состояния и заметки
Имеется рабочее GUI с возможностью ввода текста и дальнейшего его ввода с отображением только правильно набранных букв.
Графическое состояние будет доработано в дальнейшем.
Возможность изменения размера окна будет добавлена в дальнейшем.
Отображение скорость печати будет добавлено в дальнейшем.
Возможность выйти в момент ввода кнопкой будет добавлена в дальнейшем.
Компиляция в .exe вероятна в дальнейшем.

## Информация по запуску
Для запуска необходима только библиотека kivy.
Информация по ее установке и запуску приложения:

#### Windows CMD:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
python ./main.py
```

#### Windows bash:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv
source kivy_venv/Scripts/activate
python ./main.py
```

#### Linux:

```
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv
source kivy_venv/bin/activate
python ./main.py
```
