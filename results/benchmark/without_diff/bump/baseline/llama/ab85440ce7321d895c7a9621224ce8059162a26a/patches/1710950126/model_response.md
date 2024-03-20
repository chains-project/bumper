Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(false, "Status: Downloaded newer image for " + image),
            new StringContains(false, "Image pulled successfully")
        );
    }
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for " followed by the image name, while the second `StringContains` matcher checks for the presence of the string "Image pulled successfully".

The `AllOf` matcher returns true if both of its components match, which means that the image name is present in the output and the image has been pulled successfully.

This patch addresses the error by providing a different way to check for the image pull status, without using the `StringContains` constructor that is not applicable due to the type mismatch.