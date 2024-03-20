Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for "), 
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, and checks if the string contains the given substring. However, in this case, the second parameter is a variable `image` that is not a string literal, so the constructor cannot be applied.

The proposed patch uses the `AllOf` class from the same package as `StringContains` to chain multiple matchers together. The first matcher is a `StringContains` with the fixed string "Status: Downloaded newer image for " and the second matcher is a `StringEndsWith` that checks if the input string ends with the given `image` string.

This should fix the error and make the code compile-time friendly.