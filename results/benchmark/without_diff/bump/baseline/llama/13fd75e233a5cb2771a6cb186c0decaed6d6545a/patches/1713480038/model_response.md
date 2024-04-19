Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first matcher checks for the presence of the string "Status: Downloaded newer image for " followed by the image name, and the second matcher checks for the presence of the string "Image pulled successfully".

The `AllOf` matcher returns a matcher that matches if all of its components match, so this should fix the error caused by the incompatible types.