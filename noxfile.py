import os
import shutil

import nox

nox.options.reuse_existing_virtualenvs = True

PYTHON_VERSIONS = ['pypy3', '3.6', '3.7', '3.8']


@nox.session(python=PYTHON_VERSIONS[-1])
def lint(session):
    """Performs pep8 and security checks."""
    source_code = 'tutorial'
    session.install('flake8==3.8.2', 'bandit==1.6.2')
    session.run('flake8', source_code)
    session.run('bandit', '-r', source_code)


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Runs the test suite."""
    session.install('poetry>=1.0.0,<2.0.0')
    session.run('poetry', 'install')
    session.run('pytest')

    # we notify codecov when the latest version of python is used
    if session.python == PYTHON_VERSIONS[-1] and 'GITHUB_ACTIONS' in os.environ:
        session.notify('codecov')


@nox.session
def codecov(session):
    """Runs codecov command to share coverage information on codecov.io"""
    session.install('codecov==2.1.3')
    session.run('codecov')


@nox.session(python=PYTHON_VERSIONS[-1])
def deploy(session):
    """Dummy deployment"""
    session.log('This is where I should use "poetry publish --build" :D')


@nox.session(python=False)
def clean(*_):
    """Since nox take a bit of memory, this command helps to clean nox environment."""
    shutil.rmtree('.nox', ignore_errors=True)
