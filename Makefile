

run: clear
	python3 runner.py

clear:
	clear && printf '\e[3J'

# render output markdown file
build-output:
	@rm output/renders/output.md
	python make_output.py
	head output/renders/output.md
