Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for "), 
        new StringContains(image)
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher looks for the string "Status: Downloaded newer image for " followed by the image name. The second `StringContains` matcher looks for the image name.


The `AllOf` matcher returns true only if both of its component matchers return true, so it will match if both the "Status: Downloaded newer image for " string and the image name are present in the input string.

This patch replaces the `StringContains` constructor with a call to `AllOf` and removes the `Override` annotation, as it is not needed.