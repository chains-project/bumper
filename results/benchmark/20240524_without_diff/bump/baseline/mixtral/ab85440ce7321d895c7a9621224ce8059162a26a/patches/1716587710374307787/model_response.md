Sure, I can help you with that. Here's a patch that should fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    String formatString = String.format("Status: Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(formatString);
}
```
In this patch, I created a new variable `formatString` to store the formatted string, and then passed it as an argument to the `containsString` method. This should fix the error and make the code more readable.