from setuptools import setup, find_packages

setup(
    name='timecraft',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytz',
    ],
    description='A flexible, timezone-aware event scheduler',
    author='Sathish Jindam',
    author_email='sathishjindam98@gmail.com',
    url='https://github.com/yourusername/timecraft',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
