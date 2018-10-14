import os
import json
import re
import sys
import zipfile
from argparse import ArgumentParser

config_preqs = ['name', 'surname', 'student-id']

parser = ArgumentParser()
parser.add_argument("-c", "--config", dest="config", default="config.json",
                    help="the path to your config json")
parser.add_argument("-d", "--directory", dest="dir", default=".",
                    help="the directory where the exercises are located")
parser.add_argument("exercise_number", nargs='+', type=int,
                    help="the number(s) of the exercise(s) you want to zip")

args = parser.parse_args()

if not os.path.isfile(args.config):
    sys.exit("config file does not exist!")

with open(args.config, 'r') as file:
    config = json.load(file)

if not all([p in config for p in config_preqs]):
    sys.exit("please make sure your config contains all"
             + "nessecary values: 'name', 'surname' and 'student-id'!")

for exn in args.exercise_number:
    filename = config['name'].lower() + "_" + config['surname'].lower() + "_" + \
        str(config['student-id']) + "_info1_exercise_" + str(exn) + ".zip"

    ex_re = '\D+\0*' + str(exn) + '\d*'
    ex_dirs = next(os.walk(args.dir))[1]
    ex_dir = next(filter(lambda l: re.search(ex_re, l), ex_dirs), None)
    if ex_dir is None:
        print("Could not find directory of exercise " + str(exn) + "!")
        continue
    ex_dir = os.path.join(args.dir, ex_dir)

    tasks = []
    for (root, dirs, files) in os.walk(ex_dir):
        tasknames = filter(lambda l: re.match(
            'task_\d+(_[a-z\d])?\.py', l), files)
        for f in tasknames:
            tasks.append((os.path.join(root, f), f))

    if len(tasks) > 0:
        with zipfile.ZipFile(filename, 'w') as zipf:
            for p, t in tasks:
                zipf.write(p, arcname=t)
        print("Saved exercise " + str(exn) + " successfully.")
    else:
        print("Coldn't find any valid source files in exercise " + str(exn) + "!")
