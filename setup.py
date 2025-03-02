from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='image-processing-package',
    version='0.1.0',
    author='Thiago',
    description='Um pacote para processamento de imagens',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Thiago-Rodui/image-processing-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)