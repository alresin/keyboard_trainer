# Клавиатурный тренажер

## Описание временного состояния и заметки

### Внесенные изменения с последней версии
* Удалено использование `import *`
* При старте с пустым текстом приложение не вылетает
* Показ скорости и количесва ошибок перенесен в GUI
* Код приведен к PEP8

### Описание текущего состояние
Имеется рабочее GUI с возможностью ввода текста и дальнейшего его ввода с отображением только правильно набранных букв.
Отображется скорость печати и количестве ошибок отображается после завершения печати
Графическое состояние будет доработано в дальнейшем.
Возможность изменения размера окна будет добавлена в дальнейшем.
Возможность выйти в момент ввода кнопкой будет добавлена в дальнейшем.
Компиляция в .exe вероятна в дальнейшем.
Также будет написана документация к функциям и файлам.
Размер окна приложения в зависимости от масштаба и разрешения экрана может различаться, 
его можно изменить в первой строке файла `config.py`.

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
