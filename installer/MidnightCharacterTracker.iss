[Setup]
AppName=Midnight Character Tracker
AppVersion=0.1.0
AppPublisher=Malte Maehlmann

DefaultDirName={autopf}\Midnight Character Tracker
DefaultGroupName=Midnight Character Tracker

OutputDir=output
OutputBaseFilename=MidnightCharacterTrackerSetup

Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "MidnightCharacterTracker.exe"; DestDir: "{app}"
Source: "_internal\*"; DestDir: "{app}\_internal"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Midnight Character Tracker"; Filename: "{app}\MidnightCharacterTracker.exe"

Name: "{autodesktop}\Midnight Character Tracker"; Filename: "{app}\MidnightCharacterTracker.exe"

[Run]
Filename: "{app}\MidnightCharacterTracker.exe"; Description: "Launch Midnight Character Tracker"; Flags: nowait postinstall skipifsilent