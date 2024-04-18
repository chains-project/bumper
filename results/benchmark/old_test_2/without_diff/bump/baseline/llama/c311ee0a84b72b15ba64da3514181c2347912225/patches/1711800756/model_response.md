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
            "pulling image"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pulling image". The `AllOf` matcher returns true only if both of its component matchers return true, which means that the patched `imagePulled` method will return a matcher that matches if both conditions are met.

This patch addresses the error by providing a different way to check for the presence of the image name in the output string, without using the `StringContains` constructor that is not applicable due to the external dependency issue.