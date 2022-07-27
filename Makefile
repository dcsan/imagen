

run: clear
	python3 cli.py

clear:
	clear && printf '\e[3J'

# render output markdown file
gallery:
	python cli.py -t gallery

storyboard:
	python cli.py -t storyboard

renders:
	python cli.py -t renders

git-push:
	git add .
	git commit -m "update"
	git push

shrink:
	mogrify -format jpg output/dalle-2/*png
