import os, sys

chapter_name = 'chapter{}'.format(sys.argv[1])

os.makedirs(chapter_name)
os.makedirs(f'{chapter_name}/elixir')
file = open(f'{chapter_name}/elixir/exercises.ex', 'a+')
os.makedirs(f'{chapter_name}/python')
file = open(f'{chapter_name}/python/exercises.ex', 'a+')