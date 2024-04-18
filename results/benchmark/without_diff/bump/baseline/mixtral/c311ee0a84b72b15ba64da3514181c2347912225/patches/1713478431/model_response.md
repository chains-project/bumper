Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String imageDownloadedMsg = String.format("Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(imageDownloadedMsg);
}
```

The patch removes the extraneous `Status:` from the message string, so it matches the expected format.