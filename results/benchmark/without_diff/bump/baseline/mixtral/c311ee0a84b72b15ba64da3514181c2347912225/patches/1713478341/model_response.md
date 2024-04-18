Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String format = String.format("Status: Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(format);
}
```

In this patch, I have assigned the formatted string to a separate variable `format`, before passing it to the `containsString` method. This avoids the need for nested method calls, and resolves the "identifier expected" error.