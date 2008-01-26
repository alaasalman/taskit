outdirectory = .
parentdirectory = ..

all: TaskInputDialog.py CategoryInputDialog.py AboutDialog.py MainWindow.py DBDir

DBDir:
	mkdir $(parentdirectory)/db

TaskInputDialog.py: TaskInputDialog.ui
	pyuic4 TaskInputDialog.ui -o $(outdirectory)/TaskInputDialog.py

CategoryInputDialog.py: CategoryInputDialog.ui
	pyuic4 CategoryInputDialog.ui -o $(outdirectory)/CategoryInputDialog.py

AboutDialog.py: AboutDialog.ui
	pyuic4 AboutDialog.ui -o $(outdirectory)/AboutDialog.py

MainWindow.py: MainWindow.ui
	pyuic4 MainWindow.ui -o $(outdirectory)/MainWindow.py

clean:
	rm *.pyc
	rm TaskInputDialog.py
	rm CategoryInputDialog.py
	rm AboutDialog.py
	rm MainWindow.py
