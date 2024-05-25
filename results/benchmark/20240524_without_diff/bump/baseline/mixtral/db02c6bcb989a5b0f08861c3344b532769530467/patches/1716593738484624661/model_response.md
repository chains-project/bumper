```java
  @Override
    public void describeTo(Description description) {
        String value = "a string containing: " + expected;
        description.appendText(value);
    }
```