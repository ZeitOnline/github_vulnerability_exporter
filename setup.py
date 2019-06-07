from setuptools import setup, find_packages


setup(
    name='github_vulnerability_exporter',
    version='1.4.0',
    author='Wolfgang Schnerring',
    author_email='wolfgang.schnerring@zeit.de',
    url='https://github.com/ZeitOnline/github_vulnerability_exporter',
    description='',
    long_description=(
        open('README.rst').read() +
        '\n\n' +
        open('CHANGES.txt').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    install_requires=[
        'prometheus_client',
        'requests',
        'setuptools',
    ],
    entry_points={'console_scripts': [
        'github_vulnerability_exporter = github_vulnerability_exporter:main',
    ]}
)
