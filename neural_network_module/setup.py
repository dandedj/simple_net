from setuptools import setup, find_packages

setup(
    name='neural_network_module',
    version='0.1',
    packages=find_packages(),
    description='A simple neural network module',
    author='Dave Dandeneau',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='neural network, machine learning, deep learning',
    install_requires=['numpy'],
    extras_require={
        'test': ['pytest'],
    },
)