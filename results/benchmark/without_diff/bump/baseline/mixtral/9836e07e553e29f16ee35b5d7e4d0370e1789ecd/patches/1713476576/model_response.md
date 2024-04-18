Here's the fixed version of the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    String imageDownloadedMessage = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(imageDownloadedMessage);
}
```

The error was caused by using `String.format` directly inside the `containsString` method. I extracted the formatted string into a separate variable, which should resolve the issue.