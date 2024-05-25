Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatted = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(formatted);
}
```

In this patch, I created a new variable `formatted` to store the formatted string, and then passed it to the `containsString` method. This avoids the need for the `String.format` method call inside the argument list of `containsString`, which was causing the "identifier expected" error.