import sys
import getopt

from data.prompts import storylines, various
from utils.RenderLoop import render_many
from utils.DocMaker import create_output


def do_renders():
    render_many(lines=various)


def make_gallery(taskname='gallery'):
    if taskname == 'gallery':
        lines = various
    elif taskname == 'storyboard':
        lines = storylines
    create_output(taskname, lines, max_pix=3)
    create_output(taskname, lines, max_pix=6)
    create_output(taskname, lines, max_pix=9)


def show_help():
    print('usage:\n\tcli.py --task renders|gallery')
    sys.exit()


def get_task(argv):
    try:
        opts, args = getopt.getopt(argv, "t:0:", ["task="])
    except getopt.GetoptError:
        show_help()

    for opt, arg in opts:
        if opt == '-h':
            show_help()
        elif opt in ("-t", "--task"):
            taskname = arg
            return taskname


def main(argv):
    taskname = get_task(argv)
    if taskname == 'renders':
        do_renders()
    elif taskname == 'gallery':
        make_gallery('gallery')
    elif taskname == 'storyboard':
        make_gallery('storyboard')
    else:
        print('task not found:', taskname)
        show_help()


main(sys.argv[1:])
