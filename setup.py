from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='syllable',
    version='0.0.1',
    description='Tool to split phonetic french into syllables',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Thibo Rosemplatt',
    author_email='thibo.rosemplatt@gmail.com',
    url = 'https://github.com/psawa/syllable_splitter',
    packages=find_packages('syllable_splitter'),
    install_requires=[],
)