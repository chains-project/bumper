Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `boolean` value indicating whether the searched substring should be found from the beginning of the searched string, and the second is the substring to search. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the formatted string is not a substring of the searched string.

The proposed patch replaces the `StringContains` matcher with an `AllOf` matcher that combines two matchers: `StringContains` and `StringEndsWith`. The `StringContains` matcher searches for the formatted string, and the `StringEndsWith` matcher ensures that the searched string ends with the image name.
This should fix the error and allow the code to compile successfully.