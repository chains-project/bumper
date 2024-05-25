Sure, here's a possible patch for the code you provided:
```java
private static Matcher<String> imagePulled(final String image) {
    String imagePulledMessage = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(imagePulledMessage);
}
```
The issue with the original code is that the `containsString` method expects a string argument, but it was getting a formatted string instead. To fix this, I created a separate variable `imagePulledMessage` to store the formatted string, and then passed it as an argument to `containsString`. This should resolve the "identifier expected" error you were seeing.