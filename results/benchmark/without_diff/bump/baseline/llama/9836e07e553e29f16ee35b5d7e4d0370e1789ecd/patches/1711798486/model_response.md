Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor taking two parameters cannot be used because the second parameter is not a String. Instead, create a new `StringContains` object with the first parameter set to `false` and the second parameter set to a string that contains the image name. Then, use the `AllOf` class to combine both `StringContains` objects using the `AllOf` constructor.

This patch modifies the code to fix the error while maintaining the same functionality.