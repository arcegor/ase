//преобразование gui интерфейса в файл .py
pyuic5 path/to/design.ui -o output/path/to/design.py
//создание файла .exe (app.exe будет лежать в папке dist
pyinstaller -F -w -i="atom.ico" --clean --name="app" main.py
