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
            " pulling image " + image + " newer image"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first one checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second one checks for the presence of the string "pulling image" followed by the image name and the word "newer".

The `AllOf` matcher returns true if both of its component matchers return true, so if both of the `StringContains` matchers match, the `imagePulled` method will return a matcher that matches.

This patch should fix the error because it no longer tries to create a `StringContains` matcher with a format string that contains a `%s` placeholder, which is not allowed. Instead, it uses two separate `StringContains` matchers that each check for a specific substring within the input string.