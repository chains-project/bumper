Here's a patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatString = String.format("Status: Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(formatString);
}
```

This patch creates a separate variable for the formatted string, which should resolve the "identifier expected" error.