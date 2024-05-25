Here's the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    String formatted = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(formatted);
}
```

This patch creates a new variable `formatted` to store the formatted string, which can be used directly in the `containsString` method, avoiding the need for the `<identifier>` in the original code.