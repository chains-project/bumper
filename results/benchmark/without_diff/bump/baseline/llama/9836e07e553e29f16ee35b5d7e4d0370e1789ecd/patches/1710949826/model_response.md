Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `boolean` value indicating whether the searched string should be evaluated case-insensitively, and the second is the search string. In this case, the second parameter is a format string that includes the image name.

Instead of using `StringContains`, we can use `AllOf` to combine two matchers: `StringContains` and `StringEndsWith`. The first matcher will search for the "Status: Downloaded newer image for" string, and the second will ensure that the searched string ends with the image name.

This change should fix the error and allow the code to compile successfully.