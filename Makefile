all: TaskInputDialog.py CategoryInputDialog.py AboutDialog.py MainForm.py

TaskInputDialog.py: TaskInputDialog.ui
	pyuic4 TaskInputDialog.ui -o TaskInputDialog.py

CategoryInputDialog.py: CategoryInputDialog.ui
	pyuic4 CategoryInputDialog.ui -o CategoryInputDialog.py

AboutDialog.py: AboutDialog.ui
	pyuic4 AboutDialog.ui -o AboutDialog.py

MainForm.py: MainForm.ui
	pyuic4 MainForm.ui -o MainForm.py
