Sure, here's a possible patch for the code:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
In this patch, I've created a new variable `message` to store the string that we want to check for in the log message. This makes the code easier to read and understand. I've then used this variable to create the `Matcher` object.

The issue with the original code was that the `containsString` method expects a string argument, but it was receiving a format string with an argument. This caused the compiler to throw an error. By creating a separate variable for the formatted string, we avoid this issue.

I hope this helps! Let me know if you have any questions.