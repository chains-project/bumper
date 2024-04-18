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
            " Pulled"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string " Pulled".

The `AllOf` matcher returns a matcher that matches if both of its components match, which in this case means that both parts of the string must be present in the input string.

This should fix the error because the `StringContains` constructor with two arguments is not available in the version of the hamcrest library that you are using, but the `AllOf` class is available and can be used to achieve the same result.