from setuptools import setup

setup(
    name='per_level_logging',
    version="0.1.0",
    author="Akira Tanimura",
    author_email="autopp.inc@gmail.com",
    description="Implementation of logging.Handler to change the output per level.",
    license="Apache Software License 2.0",
    keywords="logging",
    url="https://github.com/autopp/python_per_level_logging",
    packages=[
        'per_level_logging',
    ],
    extras_require={
        'twisted': ['twisted'],
    },
    test_suite="tests",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Logging"
        "License :: OSI Approved :: Apache Software License",
    ],
)
