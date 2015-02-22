from setuptools import setup

setup(name='repeat',
      version='0.2',
      description='retry library',
      url='http://github.com/andrewguy9/retry',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['repeat'],
      entry_points = {
        'console_scripts': [
          'repeat = repeat.ui:main',
          ],
      },
      zip_safe=False)
