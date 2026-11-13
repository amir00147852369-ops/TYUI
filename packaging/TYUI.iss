; Inno Setup 6 installer script. Build dist\TYUI first with PyInstaller.
#define MyAppName "TYUI"
#define MyAppVersion "1.0.0"
#define MyAppExeName "TYUI.exe"
[Setup]
AppId={{D77A04ED-59DB-4E63-9658-38BFB3341B5F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\TYUI
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
OutputDir=..\dist\installer
OutputBaseFilename=TYUI-Setup-1.0.0
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked
[Files]
Source: "..\dist\TYUI\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Icons]
Name: "{group}\TYUI"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\TYUI"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch TYUI"; Flags: postinstall nowait skipifsilent
