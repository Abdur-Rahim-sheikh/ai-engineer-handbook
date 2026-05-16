## Content

1. [Some important python command](#some-important-python-command)
2. [Some interesting python behaviour](#some-interesting-python-behaviour)
3. [What is pytest fixture scope?](#what-is-pytest-fixture-scope)
4. [Some common alembic commands](#some-common-alembic-commands)
5. [When really is the primary key generated in sqlalchemy or sqlmodel](#when-really-is-the-primary-key-generated-in-sqlalchemy-or-sqlmodel)

### Some important python command

1. Counter -> to count all occurances in list/str
2. isdigit -> it's a method of str to check if the char/str is string
3. islower/isupper -> these method helps to check letter case.

### Some interesting python behaviour

1. What this below code will return?

```python
def func():
    try:
        return 1
    finally:
        return 2
print(func())
```

This code will return `2`. In Python, if there is a `finally` block, it will execute after the `try` block, and if there is a return statement in the `finally` block, it will override any previous return statements in the `try` block. Therefore, even though the `try` block returns `1`, the `finally` block returns `2`, which is what gets returned when you call `func()`.

### What is pytest fixture scope?

In pytest, a fixture is a function that is used to set up some state or provide some data for your tests. The scope of a fixture determines how long the fixture will be active and when it will be executed.

The available scopes for pytest fixtures are:

1. `function`: The fixture is executed once per test function. This is the default scope.
2. `class`: The fixture is executed once per test class. All test methods in the class will share the same fixture instance.
3. `module`: The fixture is executed once per module. All test functions in the module will share the same fixture instance.
4. `session`: The fixture is executed once per test session. All test functions across all modules will share the same fixture instance.

The scope of a fixture can be specified using the `scope` parameter in the `@pytest.fixture` decorator. For example:

```python
import pytest
@pytest.fixture(scope="session")
def init_db():
    # Code to initialize the database
    yield db_connection
    # Code to clean up the database connection
```

And yes, there are some built-in fixtures in pytest, such as `tmpdir`, `tmp_path`, `capfd`, `caplog`, etc., which provide common functionality for testing. You can also create your own custom fixtures to suit your specific testing needs.

### Some common alembic commands

**Generate new migration**: - `alembic revision --autogenerate -m "message"` - This scans our models, compares them to the database, and writes a new python script in `versions`
**Apply migrations to the database**: - `alembic upgrade head` - This runs all pending scripts to bring my dabase schema to the latest version

**Undo the last migration** - `alembic downgrade -1` - Useful when we want to revert back by `n` version here `n=1`

**More**

- `alembic current` -> Current database version
- `alembic history --verbose` -> listing all migration scripts
- `alembic check` a quick way to see if the models and database are of of sync

### When really is the primary key generated in sqlalchemy or sqlmodel

Let's say we have a model

```python
from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from typing import Annotated

class User(SQLModel, table=True):
    id: Annotated[UUID|None, Field(default_factory=uuid4, primary_key=True)]
    name: str
```

We are particularly interested in the `id` generation process.
First thing, if every user need to have an `id` as a primary key why are we allowing None as an input.

Well to help pydantic validation. As during creation we will not provide the id, but we don't want to raise validation error by pydantic as well that's why.

Here, we have exactly 3 ways to create an user instance,

1. `user1 = User(id=uuid4(), name="abir")`
2. `user2 = User(name="abir")`
3. `user3 = User(id=None, name="abir")`

You can be assured that all of these will work and create a valid user.
But the real question comes what really happens when a `session` sees these cases.

1. For case 1, it get's the user id, so no fuss it tries insert operation on it and the left handled by db
2. For case 2, `During instanciation` of the sqlmodel class, calls the default factory and generates a uuid. So for the session it's same as case 1.
3. Case 3, is somewhat interesting. Session get's a `None` for primary key. after everything is done, when `session.flush()` method is called just before the commit. It looks for if any way to generate. The session finds a python side default caller, it calls that function and assigns the value to id of the instance inplace. Thus the commit generate a insert query and then rest handled by the db.

So to remeber that, if we explicitly pass None for `id`, it's not generate untill `flush` method is called either manually inside code or by the session handler before commit call. And this is how `flush` comes handy to know where it call it, on basis of business requirement.
