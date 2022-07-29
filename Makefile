

run: clear
	python3 cli.py

clear:
	clear && printf '\e[3J'

# render output markdown file
gallery:
	python cli.py -t gallery

storyboard:
	python cli.py -t storyboard

render-story:
	python cli.py -t render-story

render-lines:
	python cli.py -t render-lines

git-push:
	git add .
	git commit -m "update"
	git push

shrink:
	mogrify -verbose -format jpg output/dalle-2/*png
