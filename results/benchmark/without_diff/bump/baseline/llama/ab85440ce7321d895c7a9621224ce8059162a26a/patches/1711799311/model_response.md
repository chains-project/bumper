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
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of " Pulled". The `AllOf` matcher ensures that both conditions are met for the match to succeed.

This patch addresses the error by providing a different way to write the matcher that does not rely on the `StringContains` constructor that is not applicable due to the type mismatch.