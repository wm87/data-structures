# AVL Tree Visualizer (Python)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Focus](https://img.shields.io/badge/Focus-Data%20Structures-important)
![GUI](https://img.shields.io/badge/GUI-Tkinter-informational)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib-orange)
![Algorithms](https://img.shields.io/badge/Algorithms-AVL%20Tree%20%7C%20Linked%20List-blueviolet)
![Complexity](https://img.shields.io/badge/Complexity-O\(log%20n\)%20%7C%20O\(n\)-yellow)
![Education](https://img.shields.io/badge/Use%20Case-Education%20%26%20Interviews-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Computer%20Science-critical)
![Code Quality](https://img.shields.io/badge/Code%20Quality-Clean%20%26%20Readable-success)

Ein interaktiver **AVL-Baum-Visualizer** mit grafischer Benutzeroberfläche, entwickelt in **Python**, der die Funktionsweise selbstbalancierender binärer Suchbäume verständlich, transparent und visuell nachvollziehbar macht.
Dieses Projekt richtet sich sowohl an **Studierende der Informatik** als auch an **technische Recruiter**, die Wert auf saubere Algorithmen, gute Softwarearchitektur und Benutzerfreundlichkeit legen.


---

## 🚀 Projektüberblick

AVL-Bäume gehören zu den zentralen Datenstrukturen der Informatik. Dieses Projekt kombiniert:

* **algorithmische Korrektheit** (Insertion, Deletion, Suche mit Balancierung)
* **visuelle Darstellung** der Baumstruktur inkl. Höhen- und Balancefaktoren
* **interaktive GUI**, um Operationen intuitiv auszuführen

Das Ziel ist es, nicht nur *funktionierenden Code*, sondern auch **verständliche Software** zu liefern.

---

## ✨ Features

* ✅ Einfügen, Suchen und Löschen von Knoten in einem AVL-Baum
* 🌳 Automatische Balancierung mittels Links- und Rechtsrotationen
* 🔍 Visuelle Hervorhebung des Suchpfades
* 📊 Anzeige von Höhe (`h`) und Balancefaktor (`b`) an jedem Knoten
* 🖥️ Grafische Benutzeroberfläche mit **Tkinter**
* 📈 Dynamische Baumvisualisierung mit **Matplotlib**

---

## 🧠 Technischer Hintergrund

### AVL-Baum

Ein AVL-Baum ist ein selbstbalancierender binärer Suchbaum mit folgenden Eigenschaften:

* Die Höhen der Teilbäume unterscheiden sich um maximal 1
* Such-, Einfüge- und Löschoperationen laufen in **O(log n)**
* Balancierung erfolgt über gezielte Rotationen

Dieses Projekt implementiert die AVL-Logik **vollständig manuell**, ohne externe Datenstruktur-Bibliotheken.

---

## 🏗️ Architektur & Code-Struktur

```text
.
├── Node            # Repräsentiert einen einzelnen AVL-Knoten
├── AVLTree         # Enthält die komplette Baumlogik
│   ├── insert()
│   ├── delete()
│   ├── search()
│   ├── Rotationen (left / right)
│   └── Visualisierungsmethoden
└── AVLTreeGUI      # GUI-Schicht (Tkinter + Matplotlib)
```

### Trennung der Verantwortlichkeiten

* **Datenstruktur & Algorithmik** sind strikt von der **GUI** getrennt
* Gute Grundlage für Erweiterungen (z. B. andere Bäume oder Exportfunktionen)

---

## 🖼️ Visualisierung

* Jeder Knoten zeigt:

  * Schlüsselwert
  * Höhe (`h`)
  * Balancefaktor (`b`)
* Suchpfade werden **farblich hervorgehoben**
* Kanten und Knoten passen sich dynamisch der Baumhöhe an

Diese Visualisierung eignet sich ideal zur **Lehre**, **Selbstkontrolle** und **Demonstration im Bewerbungsgespräch**.

---

## ⚙️ Installation & Ausführung

### Voraussetzungen

* Python **3.9+**
* Installierte Pakete:

```bash
pip install matplotlib
```

(Tkinter ist in den meisten Python-Installationen bereits enthalten)

### Starten der Anwendung

```bash
python avl_tree_gui.py
```

---

## 🧪 Beispielanwendungen

* Verständnis von Rotationen (LL, RR, LR, RL)
* Visualisierung der AVL-Eigenschaften in Echtzeit
* Lehrmaterial für Datenstrukturen-Vorlesungen
* Demonstration algorithmischer Kompetenz im Portfolio

---

## 🔮 Mögliche Erweiterungen

* Animationen der Rotationen
* Schritt-für-Schritt-Modus
* Unterstützung weiterer Baumtypen (RB-Tree, B-Tree)
* Export als Bild oder PDF

---

## 📦 Doubly Linked List

Neben dem AVL-Baum enthält dieses Repository eine **vollständige Implementierung einer doppelt verketteten Liste** (Doubly Linked List) in Python. Auch dieses Skript wurde bewusst **ohne Nutzung fertiger Datenstruktur-Bibliotheken** umgesetzt, um das zugrunde liegende Konzept transparent darzustellen.

### ✨ Features der Doubly Linked List

* 🔁 Vorwärts- **und** Rückwärtsnavigation durch `prev`- und `next`-Referenzen
* ➕ Einfügen

  * am Anfang
  * am Ende
  * an beliebiger Position
* ❌ Löschen

  * nach Wert
  * nach Index
* 🔍 Lineare Suche mit Index-Rückgabe
* 📏 Berechnung der Listenlänge
* 🧪 Integriertes Test-/Demo-Szenario im `__main__`-Block

### 🧠 Technischer Fokus

* Saubere Pointer-Verwaltung (`prev` / `next`)
* Korrekte Behandlung von Randfällen (Kopf löschen, leere Liste, ungültige Indizes)
* Klar strukturierter, gut lesbarer Code

---

⭐ *Wenn Ihnen dieses Projekt gefällt oder Sie es hilfreich finden, freue ich mich über einen Star auf GitHub!*
