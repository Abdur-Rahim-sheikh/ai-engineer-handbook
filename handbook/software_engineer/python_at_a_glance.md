## Some important python command

1. Counter -> to count all occurances in list/str
2. isdigit -> it's a method of str to check if the char/str is string
3. islower/isupper -> these method helps to check letter case.

## Some interesting python behaviour

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
