Here's a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringStartsWith(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` matcher with a `StringStartsWith` matcher, which only checks if a string starts with a given substring. This should resolve the error message, which indicates that the `StringContains` constructor cannot be applied to the given arguments. Note that this patch assumes that the expected log message format has not changed, and still starts with "Status: Downloaded newer image for".