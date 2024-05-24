Here's the fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

The issue was caused by passing `false` as the first argument to the `StringContains` constructor, which was not expected. Since the `StringContains` constructor only takes a single argument (a `String`), we can simply remove the `false` argument to fix the issue.