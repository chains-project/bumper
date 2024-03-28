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
                "pullImage"
            )
        );
    }
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pullImage".

The `AllOf` matcher returns true if both of its component matchers return true, so if both strings are present in the input string, the `imagePulled` method will return a matcher that matches the input string.

This patch addresses the error by providing a different way to write the matcher that does not rely on the `StringContains` constructor that is not available in the version of the hamcrest library being used.