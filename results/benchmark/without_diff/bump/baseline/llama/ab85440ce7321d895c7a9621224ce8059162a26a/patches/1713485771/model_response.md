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
            "pullImage"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first one checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second one checks for the presence of the string "pullImage".

The `AllOf` matcher returns true if both of its component matchers return true, so this should fix the error by providing a different way to match the expected output.