pyinstaller --paths c:\Python36\Lib\site-packages\PyQt5\Qt\bin\ ^
    --onefile --noconsole ^
    --add-data="img\icon_1.png;img" ^
    --add-data="img\123456.png;img" ^
    --icon=img\icon.ico ^
    python_qt_bd_ui_main.pyw