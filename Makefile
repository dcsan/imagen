

run: clear
	python3 runner.py

clear:
	clear && printf '\e[3J'

# render output markdown file
build-output:
	python make_output.py

git-push:
	git add .
	git commit -m "update"
	git push
