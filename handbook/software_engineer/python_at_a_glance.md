## Content

1. [Some important python command](#some-important-python-command)
2. [Some interesting python behaviour](#some-interesting-python-behaviour)
3. [What is pytest fixture scope?](#what-is-pytest-fixture-scope)
4. [Some common alembic commands](#some-common-alembic-commands)

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
