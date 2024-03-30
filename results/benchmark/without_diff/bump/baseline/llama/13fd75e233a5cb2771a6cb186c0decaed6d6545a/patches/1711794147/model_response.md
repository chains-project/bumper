Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `boolean` value indicating whether the searched string should be present in the beginning of the searched text, and the second is the searched string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the compiler cannot convert the formatted string to a `String` object.

The patch creates a new `AllOf` matcher that combines two matchers: `StringContains` and `StringEndsWith`. The `StringContains` matcher is created with the same parameters as before, but the `StringEndsWith` matcher is created with the image name directly, without formatting. This ensures that the image name is properly matched at the end of the string, regardless of its format.
This change should fix the error and allow the code to compile successfully.