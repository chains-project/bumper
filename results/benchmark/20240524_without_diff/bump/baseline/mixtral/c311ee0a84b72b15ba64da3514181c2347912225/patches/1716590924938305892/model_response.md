Here's the fixed version of the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    String imageDownloaded = String.format("Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(imageDownloaded);
}
```

The issue was caused by the use of `String.format` inside the `containsString` method. The provided patch removes the `String.format` and assigns the formatted string to a separate variable.