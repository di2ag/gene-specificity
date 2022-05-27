============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the 
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.repo_name }}` for local development.

1. Fork the `{{ cookiecutter.repo_name }}` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/{{ cookiecutter.repo_name }}.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv {{ cookiecutter.repo_name }}
    $ cd {{ cookiecutter.repo_name }}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

        $ flake8 {{ cookiecutter.app_name }} tests
        $ python setup.py test
        $ tox

   To get flake8 and tox, just pip install them into your virtualenv. 

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, 
to 

<p>============ Contributing ============</p>
<p>Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.</p>
<p>You can contribute in many ways:</p>
<h2 id="types-of-contributions">Types of Contributions</h2>
<p>Report Bugs ~~~~~~~~~~~</p>
<p>Report bugs at https://github.com/{{ cookiecutter.github_username
}}/{{ cookiecutter.repo_name }}/issues.</p>
<p>If you are reporting a bug, please include:</p>
<ul>
<li>Your operating system name and version.</li>
<li>Any details about your local setup that might be helpful in
troubleshooting.</li>
<li>Detailed steps to reproduce the bug.</li>
</ul>
<p>Fix Bugs ~~~~~~~~</p>
<p>Look through the GitHub issues for bugs. Anything tagged with “bug”
is open to whoever wants to implement it.</p>
<p>Implement Features ~~~~~~~~~~~~~~~~~~</p>
<p>Look through the GitHub issues for features. Anything tagged with
“feature” is open to whoever wants to implement it.</p>
<p>Write Documentation ~~~~~~~~~~~~~~~~~~~</p>
<p>{{ cookiecutter.project_name }} could always use more documentation,
whether as part of the official {{ cookiecutter.project_name }} docs, in
docstrings, or even on the web in blog posts, articles, and such.</p>
<p>Submit Feedback ~~~~~~~~~~~~~~~</p>
<p>The best way to send feedback is to file an issue at
https://github.com/{{ cookiecutter.github_username }}/{{
cookiecutter.repo_name }}/issues.</p>
<p>If you are proposing a feature:</p>
<ul>
<li>Explain in detail how it would work.</li>
<li>Keep the scope as narrow as possible, to make it easier to
implement.</li>
<li>Remember that this is a volunteer-driven project, and that
contributions are welcome :)</li>
</ul>
<h2 id="get-started">Get Started!</h2>
<p>Ready to contribute? Here’s how to set up
<code>{{ cookiecutter.repo_name }}</code> for local development.</p>
<ol type="1">
<li><p>Fork the <code>{{ cookiecutter.repo_name }}</code> repo on
GitHub.</p></li>
<li><p>Clone your fork locally::</p>
<p>$ git clone git@github.com:your_name_here/{{ cookiecutter.repo_name
}}.git</p></li>
<li><p>Install your local copy into a virtualenv. Assuming you have
virtualenvwrapper installed, this is how you set up your fork for local
development::</p>
<p>$ mkvirtualenv {{ cookiecutter.repo_name }} $ cd {{
cookiecutter.repo_name }}/ $ python setup.py develop</p></li>
<li><p>Create a branch for local development::</p>
<p>$ git checkout -b name-of-your-bugfix-or-feature</p>
<p>Now you can make your changes locally.</p></li>
<li><p>When you’re done making changes, check that your changes pass
flake8 and the tests, including testing other Python versions with
tox::</p>
<pre><code> $ flake8 {{ cookiecutter.app_name }} tests
 $ python setup.py test
 $ tox</code></pre>
<p>To get flake8 and tox, just pip install them into your
virtualenv.</p></li>
<li><p>Commit your changes and push your branch to GitHub::</p>
<p>$ git add . $ git commit -m “Your detailed description of your
changes.” $ git push origin name-of-your-bugfix-or-feature</p></li>
<li><p>Submit a pull request through the GitHub website.</p></li>
</ol>
<h2 id="pull-request-guidelines">Pull Request Guidelines</h2>
<p>Before you submit a pull request, check that it meets these
guidelines:</p>
<ol type="1">
<li>The pull request should include tests.</li>
<li>If the pull request adds functionality,</li>
</ol>