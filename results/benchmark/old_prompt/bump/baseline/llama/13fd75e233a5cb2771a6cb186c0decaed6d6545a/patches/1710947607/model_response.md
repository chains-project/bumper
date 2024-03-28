Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image), 
        new StringContains(true, "Image pulled successfully")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that the method name, and the second is a `Boolean` indicating whether the string should be negated. In the original code, the second parameter is a `String` formatted with the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the second parameter is not a `Boolean`. To fix this, we can create a new `StringContains` object with the negation flag set to `true` and pass the formatted string as the second argument. Then, we can use the `AllOf` matcher to combine the two `StringContains` matchers.

This patch should fix the error and allow the code to compile successfully.