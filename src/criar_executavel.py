# Cria arquivo executável a partir do "main.py"
# Veja help - https://pyinstaller.readthedocs.io/en/stable/usage.html

import PyInstaller.__main__

PyInstaller.__main__.run(['main.py', '--onefile', '-w', '-c'])
