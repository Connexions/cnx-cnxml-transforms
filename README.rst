Cnxml transforms
================

.. image:: https://travis-ci.org/Connexions/cnx-cnxml-transforms.svg?branch=master
   :target: https://travis-ci.org/Connexions/cnx-cnxml-transforms

.. image:: https://coveralls.io/repos/github/Connexions/cnx-cnxml-transforms/badge.svg?branch=master
   :target: https://coveralls.io/github/Connexions/cnx-cnxml-transforms?branch=master

This package is used for transforming documents in `Connexions archive
<https://github.com/Connexions/cnx-archive>`_ between cnxml and html formats.

Installation
------------

To install::

    python setup.py install

Running tests
-------------

The tests depend on `cnx-archive <https://github.com/Connexions/cnx-archive>`_,
so first complete the steps required for running the cnx-archive tests.

To run the tests::

    python setup.py test

Moving commits from cnx-archive
-------------------------------

As this package is not in use yet, changes need to be ported from cnx-archive
to cnx-cnxml-transforms.  It is possible to cherry-pick commits from
cnx-archive to cnx-cnxml-transforms by using ``git filter-branch``::

    git clone https://github.com/Connexions/cnx-archive.git
    cd cnx-archive
    git filter-branch --tree-filter '
        mkdir -p cnxmltransforms/tests || echo;
        mv cnxarchive/tests/transforms/*.py cnxmltransforms/tests/ || echo;
        mv cnxarchive/transforms/*.py cnxmltransforms || echo;
        rm -rf cnxarchive/;
        rm -f *.* .* || echo' -f --prune-empty

The above command allows us to keep only the commits relevant to
cnx-cnxml-transforms and move all the files so they are in the same structure
as cnx-cnxml-transforms.  (The extra ``|| echo`` just allows us to continue if
the command fails)

We can have a look at the commits and cherry-pick some of them to
cnx-cnxml-transforms::

    cd ..  # go back to cnx-cnxml-transforms
    git remote add archive ./cnx-archive
    git remote update
    git log -p archive/master  # look at the adjusted commits in our local cnx-archive
    git cherry-pick 9060fb32^..archive/master
