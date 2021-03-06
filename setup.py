from setuptools import setup

setup(name='repeat',
      version='0.3',
      description='retry library',
      url='http://github.com/andrewguy9/retry',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['repeat'],
      install_requires=['docopt'],
      entry_points = {
        'console_scripts': [
          'repeat = repeat.ui:main',
          ],
      },
      zip_safe=False)
