from setuptools import setup, find_packages

setup(
    name='githubTexView',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts':
            'tex2gitmd = tex2gitmd.main:main'
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)