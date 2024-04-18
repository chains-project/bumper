Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatString = String.format("Status: Downloaded newer image for %s";
    return new CoreMatchers.<String>containsString(formatString);
}
```

In this patch, I created a separate variable `formatString` to store the formatted string, and then passed it as an argument to the `containsString` method. This avoids the need to create a new `String` object inside the argument list, which may have caused the "identifier expected" error.