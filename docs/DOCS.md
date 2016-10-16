*Obtained from file:* [SuperDiffer/id/controllers.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/id/controllers.py)


Controller methods file, where the models are used and their information is server to routes or tests.

> count method

Helper testing function to count all IDs


> list method

Helper testing function to list all IDs


> add method

Add a description and a data to our model - rollback and return False if anything goes wrong (PK not respected, for example)


> grab_descriptors_values_to_diff method

Grab all the descriptors values to diff or get out


> grab_pairs_keys_to_compare method

Grab all pair of keys to compare




> find_diff_indexes_and_lenght_on_same_size_values method

Find the diff indexes and lenght of the difference, as follows below, and return on an array of diffs. Some more details follows below:

(a) on the first different char in a sequence, save that index on a buffer along with the sequence lenght (only 1 for now)

(b) on the successive different chars in a sequence, increment the lenght of the sequence on the buffer

(c) on the first equal char after a sequence of differences, add the buffer to our list and reset it if needed


> diff_values method

Compute insights on where the diffs are and their lenght on strings with the same size (without using https://docs.python.org/2/library/difflib.html)

* Initialize returned struct in the format: {"size":"equal", "diffs":[]}
* Doesn't compare different size strings
* Save the diffs obtained go to diffs entry

> diff method

Calculates the difference on values of all the pairs of descriptors to diff from a given ID

* Grab the values to diff - if all the values are not present on that ID, return None
* Grab the key pairs to compare - if no pair is given or found, return None
* For each pair, calculate the diff between their components values

# ID

*Obtained from file:* [SuperDiffer/id/models.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/id/models.py)


# to hold the ID table

*Obtained from file:* [SuperDiffer/id/models.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/id/models.py)

Model class to hold the ID table (Primary Key), along with its descriptors (Primary Keys also, so we don't want to have non-unique descriptors to a ID) and value

Routes to allow clients to add left and right base64 encoded on JSON values and fetch their diff

* References: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

> [**GET /v1/diff/<int:id>**] diff_right_left method

Calculates the diff between left and right descriptors of a given ID


> [**POST /v1/diff/<int:id>/left**] add_left_to_id method

Add a JSON base64 value (in the format: {"data":"base64value"}) to the left descriptor of a given ID


> [**POST /v1/diff/<int:id>/right**] add_right_to_id method

Add a JSON base64 value (in the format: {"data":"base64value"}) to the right descriptor of a given ID


> not_found method


# SupperDifferBaseDescriptorTestCase

*Obtained from file:* [SuperDiffer/tests/test_base_descriptor.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/tests/test_base_descriptor.py)


# DBTestCases

*Obtained from file:* [SuperDiffer/tests/test_db.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/tests/test_db.py)

Test cases to verify and document the DB helpers behavior on the controller


> [**UNIT_TESTS**] db count 1 method

* **Given** no data is on the database
* **When** a data is added to the model
* **Then** the database count is raised properlly by 1

> [**UNIT_TESTS**] db count 2 method

* **Given** no data is on the database
* **When** two new different IDs are added to the model
* **Then** the database count is raised properlly by 2

> [**UNIT_TESTS**] db count non unique id method

* **Given** no data is on the database
* **When** two new different descriptors for the ID are added to the model
* **Then** the database count is raised properlly by 2

> [**UNIT_TESTS**] db count unique description and id method

* **Given** no data is on the database
* **When** the same descriptor is added twice to an ID on the model
* **Then** an IntegrityError is raised and the database count is raised only by 1

> [**UNIT_TESTS**] db list 1 method

* **Given** no data is on the database
* **When** a data is added to the database model
* **Then** a json representation of it is correctly returned

> [**UNIT_TESTS**] db list 2 different ids method

* **Given** no data is on the database
* **When** two IDs are added to the database model
* **Then** a json representation of them both is correctly returned

> [**UNIT_TESTS**] db list 2 different descriptors method

* **Given** no data is on the database
* **When** two descriptors are added to the database model bound to the same ID
* **Then** a json representation of them both is correctly returned

# AddDescriptorTestCase

*Obtained from file:* [SuperDiffer/tests/test_descriptor.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/tests/test_descriptor.py)

Test cases to verify and document the Add behavior on the controller and on the endpoints


> [**UNIT_TESTS**] left add ok method

Add left descriptor and make sure all went fine


> [**UNIT_TESTS**] right add ok method

Add right descriptor and make sure all went fine


> [**UNIT_TESTS**] center add ok method

Add center descriptor and make sure all went fine


> [**UNIT_TESTS**] left add not ok method

Add left descriptor twice and make sure the second one doesn't work


> [**UNIT_TESTS**] right add not ok method

Add right descriptor twice and make sure the second one doesn't work


> [**UNIT_TESTS**] center add not ok method

Add center descriptor twice and make sure the second one doesn't work


> [**UNIT_TESTS**] mixed add method

Mix add descriptors to make sure the twice add of each doesn't work


> [**INTEGRATON_TESTS**] integration left 201 method

Post to left endpoint and make sure all went well


> [**INTEGRATON_TESTS**] integration right 201 method

Post to right endpoint and make sure all went well


> [**INTEGRATON_TESTS**] integration left 400 due to repeated left value method

Post to left endpoint twice and make sure the second one doesn't work (right endpoint works the same so we don't need to cover it with another test)


> [**INTEGRATON_TESTS**] integration left 400 due to bad base64 method

Post to left endpoint with bad base64 data and make sure it doesn't work


> [**INTEGRATON_TESTS**] integration center 404 no endpoint method

Post to center endpoint to make sure it doesn't exists


> [**INTEGRATON_TESTS**] integration mixed method

Mix posting to left and right endpoints twice and make sure the second one of each doesn't work


> [**INTEGRATON_TESTS**] integration id nan 404 method

Post to right or left with a not-a-number ID to make sure it doesn't exists


# DiffTestCases

*Obtained from file:* [SuperDiffer/tests/test_diff.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/tests/test_diff.py)

Test cases to verify and document the Diff behavior on the controller and on the endpoint


> [**UNIT_TESTS**] diff without any descriptors method

* **Given** some value is saved
* **When** the diff is requested without any descriptors to compare
* **Then** None is returned

> [**UNIT_TESTS**] diff with a single descriptors method

* **Given** some value is saved
* **When** the diff is requested with a single descriptors to compare
* **Then** None is returned, as there are no pairs to compare

> [**UNIT_TESTS**] diff without all descriptors method

* **Given** some value is saved
* **When** the diff between two descriptors is requested
* **Then** None is returned, as not all the descriptors are found

> [**UNIT_TESTS**] diff without id method

* **Given** some values are saved
* **When** the diff between two descriptors is requested with a different ID
* **Then** None is returned

> [**UNIT_TESTS**] diff not equal response method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 1 char method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 2 chars method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 3 chars middle diff method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 2 sequences begin middle method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 2 sequences middle end method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff 3 sequences begin middle end method

* **Given** some values are saved with different lenght of values
* **When** the diff between those two descriptors is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff sequences on many ids request 1 method

* **Given** some values are saved with different lenght of values on different IDs
* **When** the diff between two descriptors on ID 1 is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**UNIT_TESTS**] diff sequences on many ids request 2 method

* **Given** some values are saved with different lenght of values on different IDs
* **When** the diff between two descriptors on ID 2 is requested
* **Then** a not equal response is returned, as the lenght of the values is different

> [**INTEGRATON_TESTS**] diff integration only left value present method

* **Given** Left description of ID = 1 is added but not the right one
* **When** a diff is made asking for left and right of ID = 1
* **Then** a 400 Bad Request is retrieved
* **And** nothing changed on the databse

> [**INTEGRATON_TESTS**] diff integration only right value present method

* **Given** right descriptors of ID = 1 is added but not the left one
* **When** a diff is made asking for left and right of ID = 1
* **Then** a 400 Bad Request is retrieved
* **And** nothing changed on the databse

> [**INTEGRATON_TESTS**] diff integration left right different lenghts method

* **Given** left and right descriptors of ID = 1 are added, but with different value lenghts
* **When** a diff is made asking for left and right of ID = 1
* **Then** a 200 is retrieved
* **And** the response json states that the size is different
* **And** nothing changed on the databse

> [**INTEGRATON_TESTS**] diff integration left right equal lenghts values method

* **Given** left and right descriptors of ID = 1 are added, with equal values
* **When** a diff is made asking for left and right of ID = 1
* **Then** a 200 is retrieved
* **And** the response json states that the size is different
* **And** nothing changed on the databse

> [**INTEGRATON_TESTS**] diff integration left right 1 diff on values method

* **Given** left and right descriptors of ID = 1 are added, with different values
* **When** a diff is made asking for left and right of ID = 1
* **Then** a 200 is retrieved
* **And** the response json states that the size is different
* **And** nothing changed on the databse

> [**INTEGRATON_TESTS**] diff integration left right 1 diff on other values method

* **Given** left and right descriptors of ID = 1 are added, with different values
* **When** a diff is made asking for left and right of ID = 2
* **Then** a 200 is retrieved
* **And** the response json states that the size is different
* **And** nothing changed on the databse

# DiffE2ETestCases

*Obtained from file:* [SuperDiffer/tests/test_diff_e2e.py](https://github.com/gpaOliveira/SuperDiffer/blob/master/SuperDiffer/tests/test_diff_e2e.py)

Test cases to verify if the endpoints can be used together safelly to load images as base64 values


> [**END_TO_END_TESTS**] diff e2e lenna1 left right method

* **Given** Lenna1 is loaded on left and right
* **When** the diff is returned
* **Then** no difference is found

> [**END_TO_END_TESTS**] diff e2e lenna1 left lenna2 right method

* **Given** Lenna1 is loaded on left and right
* **When** the diff is returned
* **Then** no difference is found
