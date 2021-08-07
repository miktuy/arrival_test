# API checklist
* Корректность структуры данных
* [POST requests](./tests/test_post.py)
  * All fields are valid
  * Invalid bear's types
  * Invalid bear's names
  * Invalid bear's ages
* [GET requests](./tests/test_get.py)
  * Get empty bear's list
  * Get bear's list with one bear
  * Get bear's list with several bears
  * Get bear by id
  * Get bear by not existed id
  * Get bear without id
  * Get bear with invalid id
* [PUT requests](./tests/test_put.py)
  
  _positive_
  * Update bear's type
  * Update bear's name
  * Update bear's age
  * Update all fields
  
  _negative_
  * Update bear's type by invalid value
  * Update bear's name by invalid value
  * Update bear's age by invalid value
* [DELETE requests](./tests/test_delete.py)
  * Delete all bears when bears not exist
  * Delete all bears when several bears exist
  * Delete exist bear by id
  * Delete bear by empty id value
  * Delete bear by invalid id
  * Delete exist bear by id twice
    