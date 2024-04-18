Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

This patch removes the unnecessary parentheses around `<String>` in the `containsString` method call, which should resolve the "identifier expected" error.