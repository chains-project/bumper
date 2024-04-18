Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String imageDownloaded = String.format("Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(imageDownloaded);
}
```

This patch removes the `Status:` prefix from the expected message, which may have been introduced in a dependency update. It also creates a separate variable for the expected message, which makes the code easier to read and understand.