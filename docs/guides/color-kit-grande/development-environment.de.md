# Entwicklungsumgebung

Wir verwenden **PlatformIO** (PIO) als Entwicklungsumgebung in **Visual Studio Code** (VS Code).
Falls du noch nie mit PlatformIO gearbeitet hast, installiere es gemäss der [Installationsanleitung](https://docs.platformio.org/en/latest/integration/ide/vscode.html#installation).

## Installation

0. [Lade](https://code.visualstudio.com/) die offizielle Version von Microsoft Visual Studio Code herunter und installiere sie. PlatformIO IDE baut darauf auf.
1. Öffne die Erweiterungsverwaltung in VS Code.
2. Suche nach der offiziellen Erweiterung PlatformIO IDE.
3. Installiere PlatformIO IDE.

![PlatformIO IDE in der Erweiterungsverwaltung installieren](../../img/how-tos/platformio-install.png)

### Git installieren

Das Wetterstationsprojekt verwendet eine Bibliothek, die PlatformIO aus einem Git-Repository herunterlädt. Deshalb benötigst du einen funktionsfähigen Git-Client, auch wenn du das Projekt selbst als ZIP-Datei heruntergeladen hast.

1. Lade Git von [git-scm.com/install](https://git-scm.com/install/) herunter und installiere es.
2. Starte Visual Studio Code nach der Installation vollständig neu.
3. Öffne ein Terminal und führe `git --version` aus, um zu prüfen, ob Git verfügbar ist.

Wenn PlatformIO `Please install git client from https://git-scm.com/download` anzeigt, ist Git entweder nicht installiert oder nicht über den System-`PATH` erreichbar.

Sieh dir anschliessend die [Kurzanleitung von PlatformIO](https://docs.platformio.org/en/latest/integration/ide/vscode.html#quick-start) an:

[![PlatformIO-Kurzanleitung](../../img/how-tos/platformio-quickstart.png)](https://docs.platformio.org/en/latest/integration/ide/vscode.html#quick-start)

## Videoanleitung

Auf der Seite [Videoanleitungen](video-tutorials.md) findest du ein Video zur Einrichtung der Entwicklungsumgebung.
