Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    String msg = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```

This patch creates a temporary variable `msg` to store the formatted string, which avoids the need for parentheses around the argument to `containsString()`. This should resolve the "identifier expected" error.