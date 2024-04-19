Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, suggesting that the issue is with the second parameter. Instead of using `String.format`, we can use `StringEndsWith` to achieve the same result.

The proposed patch replaces `StringContains` with `AllOf`, which takes two matchers as arguments. The first matcher is `StringContains` with the same parameters as before, and the second matcher is `StringEndsWith` with the image name as its parameter. This should fix the error and allow the code to compile.