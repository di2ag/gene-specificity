import os
import webbrowser

from invoke import task #noqa


def open_browser(path): # type: ignore
    try:
        from urllib import pathname2url # type: ignore
    except:
        from urllib.request import pathname2url
    webbrowser.open("file://" + pathname2url(os.path.abspath(path))) # type: ignore


@task
def clean_build(c): # type: ignore
    """
    Remove build artifacts
    """
    c.run("rm -fr build/") # type: ignore
    c.run("rm -fr dist/") # type: ignore
    c.run("rm -fr *.egg-info") # type: ignore


@task
def clean_pyc(c): # type: ignore
    """
    Remove python file artifacts
    """
    c.run("find . -name '*.pyc' -exec rm -f {} +") # type: ignore
    c.run("find . -name '*.pyo' -exec rm -f {} +") # type: ignore
    c.run("find . -name '*~' -exec rm -f {} +") # type: ignore


@task
def coverage(c): # type: ignore
    """
    check code coverage quickly with the default Python
    """
    c.run("coverage run --source {{ cookiecutter.repo_name }} runtests.py tests") # type: ignore
    c.run("coverage report -m") # type: ignore
    c.run("coverage html") # type: ignore
    c.run("open htmlcov/index.html") # type: ignore


@task
def docs(c): # type: ignore
    """
    Build the documentation and open it in the browser
    """
    c.run("rm -f docs/{{ cookiecutter.repo_name }}.rst") # type: ignore
    c.run("rm -f docs/modules.rst") # type: ignore
    c.run("sphinx-apidoc -o docs/ {{ cookiecutter.app_name }}") # type: ignore

    c.run("sphinx-build -E -b html docs docs/_build") # type: ignore
    open_browser(path='docs/_build/html/index.html')


@task
def test_all(c): # type: ignore
    """
    Run tests on every python version with tox
    """
    c.run("tox") # type: ignore


@task
def clean(c): # type: ignore
    """
    Remove python file and build artifacts
    """
    clean_build(c) # type: ignore
    clean_pyc(c) # type: ignore


@task
def unittest(c): # type: ignore
    """
    Run unittests
    """
    c.run("python manage.py test") # type: ignore


@task
def lint(c): # type: ignore
    """
    Check style with flake8
    """
    c.run("flake8 {{ cookiecutter.repo_name }} tests") # type: ignore


@task(help={'bumpsize': 'Bump either for a "feature" or "breaking" change'})
def release(c, bumpsize=''): # type: ignore
    """
    Package and upload a release
    """ 
    clean(c) # type: ignore
    if bumpsize:
        bumpsize = '--' + bumpsize

    c.run("bumpversion {bump} --no-input".format(bump=bumpsize)) # type: ignore

    import {{ cookiecutter.repo_name|replace('-', '_') }} # type: ignore #noqa
    c.run("python setup.py sdist bdist_wheel") # type: ignore
    c.run("twine upload dist/*") # type: ignore

    def read_curies_file(): # type: ignore #noqa
    c.run('git tag -a {version} -m "New version: {version}"'.format(version={{ cookiecutter.repo_name|replace('-', '_') }}.__version__)) # type: ignore #noqa
    c.run("git push --tags") # type: ignore
    c.run("git push origin master") # type: ignore
