Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for "), 
        new StringEndsWith(image)
    );
}
```
This patch replaces the `StringContains` constructor with a combination of `AllOf` and `StringEndsWith` matchers. The `AllOf` matcher takes two matchers as arguments and matches if both of them match. The `StringEndsWith` matcher matches if the string ends with the specified suffix.

The first argument to `AllOf` is a `StringContains` matcher with the text "Status: Downloaded newer image for " and `false` as the second argument to indicate that the match should be case-insensitive. The second argument to `AllOf` is a `StringEndsWith` matcher with the image name.

This should fix the error and allow the code to compile.