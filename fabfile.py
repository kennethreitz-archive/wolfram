import os
from fabric.api import *

os.f
def scrub():
	""" Death to the bytecode! """
	local('rm -fr dist build')
	local("find . -name \"*.pyc\" -exec rm '{}' ';'")

#def docs():
#	"""Build docs."""
#	os.system('make html')
#	os.chdir('_build/html')
#	os.system('sphinxtogithub .')
#	os.system('git add -A')
#	os.system('git commit -m \'documentation update\'')
#	os.system('git push origin gh-pages')