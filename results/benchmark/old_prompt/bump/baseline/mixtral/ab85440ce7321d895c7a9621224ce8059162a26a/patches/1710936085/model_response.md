Here's a possible patch to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatString = String.format("Status: Downloaded newer image for %s", image);
    return is(containsString(formatString));
}
```

The issue with the original code is that there is an extra parenthesis at the end of the `containsString` method call. This patch removes the extra parenthesis and saves the formatted string to a variable to make the code clearer.