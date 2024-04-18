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
            " pulling image " + image + " latest"
        )
    );
}
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string " pulling image " followed by the image name and the word "latest".

The `AllOf` matcher returns true if both of its component matchers return true, so if the image name is found in the output with the expected status message, followed by the image name and the word "latest", the matcher will return true.

This patch should fix the error because it uses the `AllOf` matcher, which is available in the latest version of the hamcrest library, instead of the `StringContains` matcher which is not available in the latest version.