```bash
pyinstaller --add-data "settings.json;." --add-data "gui/themes;gui/themes" --add-data "gui/images;gui/images" --onefile --icon=icon.ico --name=TESTUI --noconsole main.py
```