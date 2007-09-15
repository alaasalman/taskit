srcdirectory = ..

all: TaskInputDialog.py CategoryInputDialog.py AboutDialog.py MainForm.py

TaskInputDialog.py: TaskInputDialog.ui
	pyuic4 TaskInputDialog.ui -o $(srcdirectory)/TaskInputDialog.py

CategoryInputDialog.py: CategoryInputDialog.ui
	pyuic4 CategoryInputDialog.ui -o $(srcdirectory)/CategoryInputDialog.py

AboutDialog.py: AboutDialog.ui
	pyuic4 AboutDialog.ui -o $(srcdirectory)/AboutDialog.py

MainForm.py: MainForm.ui
	pyuic4 MainForm.ui -o $(srcdirectory)/MainForm.py
