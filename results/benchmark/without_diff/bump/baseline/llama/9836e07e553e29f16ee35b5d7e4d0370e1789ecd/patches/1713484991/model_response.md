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
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pullImage". The `AllOf` matcher returns true only if both of its components match, which means that the string must contain both the specified strings.


This patch should fix the error because it removes the need for the `StringContains` constructor that is not available in the version of the Hamcrest library being used. Instead, it uses the `AllOf` class, which is available in the same version of Hamcrest, to combine two `StringContains` matchers.

Note that this patch assumes that the `AllOf` class is available in the version of Hamcrest being used. If the `AllOf` class is not available, a different approach may be needed.