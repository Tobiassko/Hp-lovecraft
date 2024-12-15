# H.P. Lovecraft Presentation Compiler

## Prerequisites
- Python 3.6 or higher
- PyInstaller (`pip install pyinstaller`)
- AutoIt (`pip install autoit`)
- PyAutoGUI (`pip install pyautogui`)

## Compilation Steps

1. Open command prompt in the project directory
2. Run the following command:
```bash
pyinstaller H.p.Lovecraft.spec
```

The compiled executable will be created in the `dist` folder.

## Running the Application
- Navigate to `dist/H.p.Lovecraft`
- Run `H.p.Lovecraft.exe`

## Troubleshooting
If you encounter missing dependencies, install them using:
```bash
pip install -r requirements.txt
```
