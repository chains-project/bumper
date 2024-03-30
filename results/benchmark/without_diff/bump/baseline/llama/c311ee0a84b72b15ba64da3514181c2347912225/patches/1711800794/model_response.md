Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, which is not applicable to the given types. We can replace it with `AllOf` which takes two matchers as arguments and returns a matcher that matches if both of the given matchers match. We can create a new `StringContains` matcher with the same `boolean` and `String` parameters as before, and combine it with a new `StringEndsWith` matcher that checks if the input string ends with the image name.