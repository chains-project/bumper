Here's a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new PatternMatcher(
        Pattern.compile(
            String.format("Status: Downloaded newer image for %s", Pattern.quote(image))
        ),
        Pattern.LITERAL
    );
}
```

This patch uses a `PatternMatcher` instead of a `StringContains` matcher. The `PatternMatcher` takes a regular expression as its first argument, which we construct by quoting the `image` parameter using `Pattern.quote()` to avoid any issues with special characters. We also specify `Pattern.LITERAL` as the second argument to ensure that the regular expression is interpreted literally. This should allow the test to pass even if the `hamcrest-core` library has been updated.