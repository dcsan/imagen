from data.prompts import storylines, various

from utils.RenderLoop import render_many
from utils.DocMaker import create_output


def do_renders():
    render_many(storylines)


def make_output():
    taskname = 'snaps'
    create_output(taskname, lines=various, max_pix=3)
    # create_output(taskname, lines=storylines, max_pix=6)
    # create_output(taskname, lines=storylines, max_pix=9)


make_output()

# do_renders()
