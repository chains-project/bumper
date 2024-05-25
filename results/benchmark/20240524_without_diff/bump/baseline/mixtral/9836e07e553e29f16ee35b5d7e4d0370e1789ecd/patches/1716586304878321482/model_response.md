Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

This patch removes the unnecessary parentheses around `<String>` and assigns the formatted string to a separate variable `message` to avoid any potential issues with the Java compiler.