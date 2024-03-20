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
                " Pulled"
            )
        );
    }
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of " Pulled" at the end of the string.

The `AllOf` matcher returns true if both of its components match, so the `imagePulled` method will return a matcher that checks for the presence of both "Status: Downloaded newer image for" followed by the image name and " Pulled" at the end of the string.

This patch should fix the error because it uses the `AllOf` matcher, which is available in the updated version of the library, instead of the `StringContains` matcher, which is not available in the updated version.