# TYUI V1.0

TYUI is a Windows desktop application. This repository includes a Windows CI pipeline that builds a **real Inno Setup installer** (`TYUI-Setup-1.0.0.exe`) from the app source.

## Get the Windows installer

After the `Build Windows installer` GitHub Actions workflow completes successfully:

1. Open the repository's **Actions** tab.
2. Select the latest successful **Build Windows installer** run.
3. Download the `TYUI-Windows-Installer` artifact.
4. Extract it and run `TYUI-Setup-1.0.0.exe`.

The setup wizard installs TYUI under Program Files, creates Start Menu shortcuts, and offers an optional desktop shortcut. The installer is generated on a Windows runner; it cannot be compiled on Linux/macOS.

## Build locally on Windows

Requirements: 64-bit Windows 10/11, Python 3.12+, and Inno Setup 6.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --noconfirm --clean --windowed --onedir --name TYUI main.py
& "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe" packaging\TYUI.iss
```

Installer output: `dist\installer\TYUI-Setup-1.0.0.exe`.

## Scope of this initial installable build

This baseline includes real live CPU and RAM monitoring and a Windows installation pipeline. It is not yet the complete optimization suite described in the original specification; no DNS changes or process termination are included in this baseline.

## Uninstall

Use **Settings → Apps → Installed apps → TYUI → Uninstall**, or the TYUI Start Menu uninstall shortcut.
