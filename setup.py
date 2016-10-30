from distutils.core import setup

setup(name='vutwifi',
      author='Thomas Levine, Max K. Luminar',
      author_email='kovykmax@gmail.com',
      description='Connect to the WIFI at FIT VUT in Brno.',
      url='https://github.com/luminaar/vutwifi',
      py_modules=['vutwifi'],
      install_requires=[
          'requests>=2.11.1',
          'horetu>=0.2.7',
      ],
      classifiers=[
          'Programming Language :: Python :: 3.5',
      ],
      entry_points = {
          'console_scripts': ['vutwifi = vutwifi:main']
      },
      version='0.1',
      license='AGPL',
      )
