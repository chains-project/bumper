Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            false,
            "pullImage"
        )
    );
}
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pullImage".

The `AllOf` matcher returns true if both of its component matchers return true, so if the image name is found in the output and the string "pullImage" is also present, the matcher will return true.

This patch should fix the error because it removes the usage of the `StringContains` constructor that is not applicable for the given types.