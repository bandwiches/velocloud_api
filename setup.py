from setuptools import setup, find_packages


REQUIRED = [
    'aiohttp',
    'dataclasses',
    'enum'
]

REQUIRED_TEST = [
    'pytest'
]

with open('README.md', 'r', encoding='utf8') as file:
    long_desc = file.read()

setup(
    name='velocloud',
    author='Brett Hoshaw',
    author_email='brett.hoshaw@gmail.com',
    # url='http://pypi.python.org/pypi/velocloud/',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>= 3.9.2',
    description='(Unofficial) Velocloud API',
    license='LICENSE',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires=REQUIRED,
    extras_require={
        'testing': REQUIRED_TEST,
    },
    keywords=['velocloud', 'vco', 'api', 'orchestrator', 'vm', 'vmware']
)
