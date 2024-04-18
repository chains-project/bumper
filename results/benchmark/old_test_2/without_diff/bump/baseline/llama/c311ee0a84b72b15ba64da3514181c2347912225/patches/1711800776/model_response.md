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
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pullImage". The `AllOf` matcher returns true if both of its component matchers return true, which means that the output string contains both the expected strings.


This patch should fix the error because it removes the need for the `StringContains` constructor that is not available in the version of the hamcrest library being used. Instead, it uses the `AllOf` class, which is available in the same version of hamcrest, to combine two `StringContains` matchers.