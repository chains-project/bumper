```java
  @Override
  public void describeTo(Description description) {
      description.appendText("a string containing: ").appendValue(Objects.requireNonNull(expected));
  }
```

This patch uses `java.util.Objects.requireNonNull()` to ensure that the `expected` argument is not `null`, which could be the cause of the error.