Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `boolean` value indicating whether the searched string should be found in the beginning of the searched text, and the second is the searched string. In the original code, the second parameter is a format string that contains an expression `%s` that will be replaced by the `image` argument.

The error message indicates that the constructor `StringContains` cannot be applied to the given types, likely because the expression `%s` in the format string is not properly formatted.

The proposed patch replaces the `StringContains` constructor with the `AllOf` class, which takes two `Matcher` objects and returns a `Matcher` that matches if both of the given matchers match. The first `StringContains` matcher is created with the same parameters as before, and the second `StringContains` matcher is created with the format string "Image pulled successfully" and the `image` argument.
This should fix the error and allow the code to compile successfully.