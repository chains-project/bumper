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
            "pull"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first one checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second one checks for the presence of the string "pull". The `AllOf` matcher returns true only if both of its component matchers return true, so it will match the input string if both conditions are met.

This should fix the error because the `StringContains` constructor with two parameters is not available in the version of the Hamcrest library being used, but the `AllOf` class is available and can be used to achieve the same result.