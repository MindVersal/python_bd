..\..\Python36\Scripts\pyuic5.exe qt_bd_ui_main.ui -o qt_bd_ui_main.py

pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip --upgrade

pyinstaller --onefile --noconsole python_qt_bd_ui_main.py

pyinstaller --paths c:\Python36\Lib\site-packages\PyQt5\Qt\bin\ ^
    --onefile --noconsole ^
    --add-data="img\icon_1.png;img" ^
    --add-data="img\123456.png;img" ^
    --icon=img\icon.ico ^
    python_qt_bd_ui_main.pyw