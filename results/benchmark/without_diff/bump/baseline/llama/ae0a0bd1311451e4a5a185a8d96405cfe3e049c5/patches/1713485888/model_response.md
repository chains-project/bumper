Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            " pull "
        )
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that specifies the contains pattern, and the second is a `boolean` that indicates whether the pattern should be matched case-insensitively. In this case, the second parameter is not provided, so it defaults to `false`.

The error message indicates that the constructor `StringContains` cannot be applied to the given types, which means that the compiler is trying to pass two arguments to the constructor, but it only takes one.

The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher looks for the pattern "Status: Downloaded newer image for %s" and the second `StringContains` matcher looks for the pattern " pull ". The `AllOf` matcher returns true if both of its component matchers return true, so if the input string contains both patterns, the `imagePulled` method will return a matcher that matches the input string.

This patch should fix the error and allow the code to compile without errors.