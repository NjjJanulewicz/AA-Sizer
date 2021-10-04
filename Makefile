run:
	python ./sizer/__main__.py

setup: requirements.txt
	pip install -r requirements.txt

build:
	cd sizer && pyinstaller --onefile __main__.py --name sizer --distpath ../bin --clean

clean:
	rm -r sizer/build
