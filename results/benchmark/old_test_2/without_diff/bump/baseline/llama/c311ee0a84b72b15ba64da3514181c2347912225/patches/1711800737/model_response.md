Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            false,
            " pulled"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first one checks for the presence of "Status: Downloaded newer image for" followed by the image name, while the second one checks for the presence of " pulled".

The `AllOf` matcher returns true only if both of its component matchers return true, so it will match if both "Status: Downloaded newer image for" and " pulled" are present in the input string.

This should fix the error because the `StringContains` constructor with two arguments is not available in the version of the hamcrest library being used, but the `AllOf` class is available and can be used to achieve the same result.