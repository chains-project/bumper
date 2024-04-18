Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, " pulling image ")
    );
}
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for " followed by the image name, while the second `StringContains` matcher checks for the presence of " pulling image ". The `AllOf` matcher returns true if both of its component matchers return true, which allows the test to pass.

This patch addresses the error by providing an alternative way to write the matcher that doesn't rely on the `StringContains` constructor that is not applicable due to the type mismatch.