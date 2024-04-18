Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatString = String.format("Status: Downloaded newer image for %s";
    return new CoreMatchers.<String>containsString(formatString);
}
```

In this patch, I've created a separate variable `formatString` for the formatted string. This way, the method call `String.format` is not inside the argument of `CoreMatchers.<String>containsString`, avoiding the "identifier expected" error.