```java
  @Override
  public void describeTo(Description description) {
      description.appendText("a string containing: ").appendValue(Objects.requireNonNull(expected));
  }
```