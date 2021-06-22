# Übung 3 – Software-Qualitätssicherung (25 Punkte)

## Lernziel

1. Sie können die Grundlagen von Qualitätsmanagement in IT-Projekten nennen und beschreiben.
2. Sie können Programmcode systematisch erstellen und dokumentieren.
3. Sie können Verfahren zur Qualitätssicherung anwenden.

## Aufgabe 1: Qualitätssicherungsverfahren Zusicherung (10 Punkte)

### Aufgabenstellung

1. Bitte lesen Sie sich in das Thema ein und machen sich damit vertraut.
2. Bitte folgenden Sie den Hinweisen im Dokument `E3_2021ss_Gruppe.docx`.
3. Bitte laden Sie sich aus dem Verzeichnis `e3/lecturer` die Dateien `E3_2021ss_lecturer.py` und `E3_2021ss_lecturer_test.py` in ihr lokales Projekt-Verzeichnis herunter. Letztere Datei ist nach dem TDD-Prinzip erstellt worden. Sie dient ihnen als Basis für die Verwendung von Qualitätssicherungsverfahren. Es sind bereits einige Softwaretests vorhanden. Diese überprüfen Methoden, um Informationen aus einem Dataset zu erhalten.
4. Bitte erstellen Sie benötigte Dokumente in Ihrem GitHub Repo im entsprechendem Gruppenverzeichnis in `e3`.

## Aufgabe 2: Qualitätssicherungsverfahren Try and Except sowie Unit Tests (15 Punkte)

### Wiederholung

Mit `Try and Except` wird in Python eine Ausnahmebehandlung (engl. _exception handling_) durchgeführt. Eine Ausnahme ist ein Zustand, meist ein Fehler, der sich während der Ausführung eines Programmes ergibt. Die Ausnahmebehandlung, ist ein Verfahren, um diese Zustände an andere Programmebenen gezielt weiterzuleiten. Es ist somit möglich, per Programm einen Fehlerzustand gegebenenfalls zu korrigieren bzw. gezielt umzulenken, damit das Programm weiter ausgeführt werden kann. Ansonsten könnten solche Fehlerzustände zu einem Abbruch des Programmes führen.

`Unit Tests` sind Komponententest die – wie der Name bereits erahnen lässt – Komponenten bzw. isolierte Bereiche in einem Programm überprüfen, um Fehler schneller finden zu können. Hierzu werden jeweils passende Testfälle erstellt, mit denen die Spezifikation überprüft wird.

Test-Driven Development (dt. _testgesteuerte Programmierung_) kurz TDD ist ein Programmierprinzip aus der agilen Softwareentwicklung. Programmierer erstellen konsequent Softwaretests vor den zu testenden Komponenten. Die Implementierung erfolgt danach. Diese wird durch die Softwaretests überprüft. Es entsteht somit ein Entwickluszyklus.

### Aufgabenstellung

1. Bitte lesen Sie sich in das Thema ein und machen sich damit vertraut.
2. Bitte folgenden Sie den Hinweisen im Dokument `E3_2021ss_Gruppe.docx`.
3. Machen Sie sich mit dem Code vertraut und führen Sie pytest aus.

## Quellen

- Vorlesung `DSCB230_MMV_3_Software-Qualitaetssicherung.pdf`
- Tutorium `T_20210521.pdf`
- Literatur `Hoffmann_2008_Software-Qualität.pdf`
- Online Referenz [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/framehtml)
