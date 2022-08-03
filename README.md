# RESTful API Testing

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Simple automated API testing for swagger [Pet Store API](https://petstore3.swagger.io/) using PyTest.

Following is a list of test cases evaluated:

- **test_add_pet** - check if pet is added successfully
- **test_get_pet_by_id** - check if pet with given id is returned successfully
- **test_get_pet_by_id_not_found** - check if pet with given id is not returned successfully (404 Error)
- **test_get_pet_by_id_invalid_id** - check if pet is not returned successfully (400 Error)
- **test_find_pets_by_status** - check if pets with the given status are returned successfully
- **test_delete_pet** - check if pet with given id is deleted successfully

### Automating proposed scenarios on different levels

**Unit Testing:**

This degree of testing verifies the working of the individual units of our application, which compare to a class in OO dialects. It is very important to note that a unit test should be testing a single unit, isolated from all of its dependencies.

**Pros:**

- Make refactoring easier
- Code quality is assured / improved
- Problems are found before time
- Debugging is easier

**Cons:**

- Amount of code is significantly increased
- They cant catch all errors
- Very hard to test UI

**Integration Testing:**

Integration tests, as the name suggests, are supposed to test integration between different components of software. As opposed to unit testing, integration tests don't mock dependencies.

**Pros:**

- Broader coverage

**Cons:**

- Fragile and easily affected by changes in environment
- Rely on accessibility of other parts of the system
- Tests take more time

**Performance Testing**

Performance testing is a non-functional type of testing and involves the process by which software or an application is tested to know its current system performance.

**Pros:**

- Tests speed of the system
- Tests reliability of the system
- Tests scalability of the system
- Tests stability of the system
- Identifies bottlenecks in the system

**Cons:**

- API is already live
- Testing has to be done at off peak hours
- Users may experience degraded service performance while the test runs

## Getting Started <a name = "getting_started"></a>

These instructions will help you set up and run these tests.

### Prerequisites

You will require a working python installation (including pip), if you don't have one, you can get one here: [Python](https://www.python.org/downloads/)

## Usage <a name = "usage"></a>

### Open a terminal in this folder and run the following commands:

Create a virtual environment

    python -m venv venv

Activate the virtual environment

    source venv/bin/activate

Install required modules (this step is only necessary if you haven't already installed them)

    pip install -r requirements.txt

Running the tests

    pytest -v
