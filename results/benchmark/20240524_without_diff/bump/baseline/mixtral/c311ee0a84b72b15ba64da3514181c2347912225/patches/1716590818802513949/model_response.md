Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

This patch removes the unnecessary `new` keyword before `CoreMatchers.<String>containsString()` and assigns the formatted string to a separate variable `message`, which is then passed to `CoreMatchers.<String>containsString()`.