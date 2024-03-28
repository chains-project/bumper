Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for "), 
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that specifies the contains pattern, and the second is a `boolean` that indicates whether the pattern should be matched ignoring case. In this case, the second parameter is not provided, which causes the error.

The proposed patch uses the `AllOf` class from the same package as `StringContains`, which allows combining multiple matchers into a single matcher. The first matcher is a `StringContains` with the fixed parameters, and the second matcher is a `StringEndsWith` that checks if the input string ends with the image name.

This patch preserves the function's signature and behavior while fixing the error.