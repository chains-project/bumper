Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            "pullImage"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pullImage". The `AllOf` matcher returns true only if both of its component matchers return true, which means that the string must contain both the specified strings.


This patch addresses the error by providing a different way to write the matcher that doesn't rely on the `StringContains` constructor that is not available in the version of the Hamcrest library being used.