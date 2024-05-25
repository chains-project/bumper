Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Downloaded newer image for %s", image)
    );
}
```

The error message indicates that the constructor for `StringContains` is unable to handle the format string `"Status: Downloaded newer image for %s"`, so I have removed the `"Status: "` prefix to resolve the issue.