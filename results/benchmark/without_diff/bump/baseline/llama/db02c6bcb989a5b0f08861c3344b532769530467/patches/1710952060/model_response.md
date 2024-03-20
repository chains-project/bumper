Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(true, image)
    );
}
```
Explanation:

The error message indicates that the `StringContains` constructor cannot be applied to the given types. This is because `StringContains` expects a single string argument representing the entire string that the matcher should match, whereas the code is passing a format string and a variable string to be formatted.

To fix this, we can use the `AllOf` matcher, which allows us to combine multiple matchers. We create a new `StringContains` matcher that matches the entire string "Status: Downloaded newer image for " + image, and then combine it with a new `StringContains` matcher that matches the image name. The `AllOf` matcher ensures that both matchers must match for the entire string to be considered a match.

Note that we had to convert the `String.format` call to a plus notation string concatenation to make the code easier to read.