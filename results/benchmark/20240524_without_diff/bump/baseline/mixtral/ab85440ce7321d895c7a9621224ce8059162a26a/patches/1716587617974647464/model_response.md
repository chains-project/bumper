Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

The changes made are:

* A new variable `message` is created to store the formatted string, which makes the code easier to read.
* The `message` variable is used as the argument for `CoreMatchers.containsString()`, which avoids the syntax error caused by the use of `String.format()` directly as an argument.