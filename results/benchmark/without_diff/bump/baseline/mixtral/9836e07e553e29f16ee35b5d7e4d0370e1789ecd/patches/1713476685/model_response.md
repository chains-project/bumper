Here is a potential patch for the code:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatted = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(formatted);
}
```

This patch creates a separate variable `formatted` to hold the result of `String.format()`, which is then passed to `CoreMatchers.<String>.containsString()`. This should fix the error message, which indicates that the parser is expecting an identifier at the location of the error.