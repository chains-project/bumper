Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String pattern = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(pattern);
}
```

This patch creates a separate variable `pattern` for the formatted string, which should resolve the syntax error.