from data.prompts import storylines, various

from utils.RenderLoop import render_many
from utils.DocMaker import create_output


def do_renders():
    render_many(lines=various)


def make_output():
    taskname = 'gallery'
    create_output(taskname, lines=various, max_pix=3)
    create_output(taskname, lines=various, max_pix=6)
    create_output(taskname, lines=various, max_pix=9)


do_renders()
make_output()
