Here's a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new PatternMatching().withPattern(
        String.format("Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced the `StringContains` matcher with a `PatternMatching` matcher that takes a regular expression pattern. The new matcher checks if the given log message matches the pattern, which should work even if the message format changes in a future version of the external dependency.

Note that I had to make some assumptions about the external dependency and the expected behavior of the code. If the code needs to check for the exact message format, then the patch may need to be adjusted accordingly.