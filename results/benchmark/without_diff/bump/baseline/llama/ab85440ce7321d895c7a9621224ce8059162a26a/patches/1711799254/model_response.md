Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first matcher checks for the presence of the string "Status: Downloaded newer image for " followed by the image name, and the second matcher checks for the presence of the string "Image pulled successfully". The `AllOf` matcher returns true only if both of its component matchers return true, which means that the image pull was successful.

This patch removes the need for the `String.format` method, which is not available in the older version of the Java SDK that the code is compiled against. Instead, it uses string concatenation to create the format string.

Please note that this is just one possible solution, and there may be other ways to fix the error.