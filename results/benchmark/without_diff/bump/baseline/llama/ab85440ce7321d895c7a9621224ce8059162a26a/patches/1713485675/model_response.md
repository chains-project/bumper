Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name. To fix the error, we can use the `StringEndsWith` matcher instead, which checks if the string ends with the given suffix. We combine both matchers using the `AllOf` matcher, which matches if all of its components match.

Note that I removed the `Override` annotation, as it's not needed in this case.