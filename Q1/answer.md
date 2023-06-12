# Question #1 (maintenance)

While troubleshooting a bug in an old application, you find that the “multiply” method below is the source of the problem.

CODE:

```py
///
/// multiplies x times y
///
def multiply(x, y):
    total = 0
    while x > 0:
        total += y
        x -= 1
    return total

```

QUESTIONS:

- What is wrong with the above code?
- If you find it wrong, please fix the code above without using the “\*” or “/” operator or Absolute call?
- As part of our development process we test all methods at a code level. Which input values would you use to do the testing?
- For later discussion: What else worries you as you fix this problem?

Answers:

- It does not account for zero or negative numbers for x. If x <= 0, then the return value is automatically 0. Also, comments syntax is wrong (if that counts).
- Code:

  ```py
  def multiply(x, y):
      '''multiplies x times y'''
      if x == 0 or y == 0:
          return 0

      total = 0
      if x < 0:
          [x, y] = [-x, -y]

      while x > 0:
          total += y
          x -= 1

      return total
  ```

- testcases:

  | Test# | x   | y   | Output |
  | ----- | --- | --- | ------ |
  | 1     | 0   | 0   | 0      |
  | 2     | 0   | 12  | 0      |
  | 3     | 6   | 0   | 0      |
  | 4     | -6  | 0   | 0      |
  | 5     | 0   | -12 | 0      |
  | 6     | 6   | 12  | 72     |
  | 7     | -6  | 12  | -72    |
  | 8     | 6   | -12 | -72    |
  | 9     | -6  | -12 | 72     |
