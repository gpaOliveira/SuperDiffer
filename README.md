![Build Status](https://circleci.com/gh/gpaOliveira/SuperDiffer.svg?style=shield&circle-token=:circle-token)

# Super Differ

Super Differ is an application that returns the difference between two base64 encoded strings.

> Requirements:

* Python 2.7.6 (download & install: https://www.python.org/downloads/)
* Vagrant (**optional** download & install: https://www.vagrantup.com/downloads.html)

# Setup:

Normal virtualenv + setup.py install. 

Details can be found on [bootstrap.sh](https://github.com/gpaOliveira/SuperDiffer/blob/master/bootstrap.sh), as the same file is also used for building up vagrant machines.

The server is started with [run_server.sh](https://github.com/gpaOliveira/SuperDiffer/blob/master/run_server.sh), but don't forget to enter dev mode first using [start_dev_mode.sh](https://github.com/gpaOliveira/SuperDiffer/blob/master/start_dev_mode.sh).

# API Behavior

The normal basic flow is to add your data to an ID left descriptor, add your data to the right ID descriptor and asks for the diff of it. Your data will be removed after each succesfull (that returns a 200) diff, even if the diff is not possible to be made. After you've added to left, succesfull adds will fail with a 400 status. The same constraint holds with right. We have no feature to cleanup the database except after a succesfull diff, so take good care of your values. A good approach to delete an unwanted value on left (or right) is to add the same value you've used on one descriptor to another and asks for a diff - that will remove your unwanted data.

We only do diffs on same size strings. If no diff is made, the returned JSON will say that "size" is "not equal". The mechanism we use to diff is described on the [Controllers Wiki](https://github.com/gpaOliveira/SuperDiffer/wiki/ID-Controller), on the find_diff_indexes_and_lenght_on_same_size_values method. 

# Routes

Routes to allow clients to add left and right base64 encoded on JSON values and fetch their diff are described below:

> [**GET /v1/diff/<int:id>**] diff_right_left method

Calculates the diff between left and right descriptors of a given ID and remove those descriptors if they're found (even if the data lenght is not the same and no diff is made)

> [**POST /v1/diff/<int:id>/left**] add_left_to_id method

Add a JSON base64 value (in the format: {"data":"base64value"}) to the left descriptor of a given ID

> [**POST /v1/diff/<int:id>/right**] add_right_to_id method

Add a JSON base64 value (in the format: {"data":"base64value"}) to the right descriptor of a given ID

# Tests

To run all our tests, execute [run_all_tests.sh]( https://github.com/gpaOliveira/SuperDiffer/blob/master/run_all_tests.sh) - this is the same script used by CircleCI. 

* A Junit output will be generated, named nose2-junit.xml
* A coverage report will be generated on the htmlcov folder

We have three types of tests:

* **Unit tests:** the ones that tests the application trough the controller directly. Run with [run_unit_tests.sh](https://github.com/gpaOliveira/SuperDiffer/blob/master/run_unit_tests.sh).

* **Integration tests:** the ones that tests the application mainly trough the endpoints. Run with [run_integration_tests.sh]( https://github.com/gpaOliveira/SuperDiffer/blob/master/run_integration_tests.sh).

* **End-to-End tests:** the ones that handles the tests the application only by the endpoints

Finally, our tests documentation taken directly from the source and their details can be found on the [wiki](https://github.com/gpaOliveira/SuperDiffer/wiki).

# Docs

The bulk of markdown documentation was generated using [build_markdown_doc_from_file.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/docs/build_markdown_doc_from_file.py), a script file created by us to crawl the code and extract comments (lines beggining with a single '#' or '"""') or class names method names or file names and output them in a markdown way to be just copied-and-pasted in to the wikis.

To execute it and renew docs/DOCS.md, do the following:

> python docs/build_markdown_doc_from_file.py > docs/DOCS.md