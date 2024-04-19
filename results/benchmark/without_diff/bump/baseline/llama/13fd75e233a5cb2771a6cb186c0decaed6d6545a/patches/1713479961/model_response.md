Here's a proposed patch to fix the error:
```
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the entire input string, and the second is a `String` that represents the substring that should be found within the input string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the compiler cannot convert the formatted string to a `String` object.

To fix this issue, we can create a new `StringContains` object by chaining two `StringContains` objects using the `AllOf` class. The first `StringContains` object searches for the substring "Status: Downloaded newer image for " + image, and the second `StringContains` object searches for the substring "Image pulled successfully".
By chaining these two objects, we create a new matcher that matches any string that contains both substrings.
This should fix the error and allow the code to compile successfully.