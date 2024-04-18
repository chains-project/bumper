Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, which is the reason for the error. We've replaced it with `AllOf`, which takes two `Matcher` objects, in this case, `StringContains` and `StringEndsWith`, to achieve the desired outcome.

The `AllOf` matcher returns `true` if both of its component matchers return `true`, which is the same behavior as the original code.

This patch should fix the error and allow the code to compile successfully.