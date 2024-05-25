Sure, I understand the requirements. Here's a possible patch for the failing method:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
The patch creates a temporary variable `message` to store the formatted string, and then passes it to the `containsString` method. This avoids the need for concatenation inside the method call, which was causing the syntax error.