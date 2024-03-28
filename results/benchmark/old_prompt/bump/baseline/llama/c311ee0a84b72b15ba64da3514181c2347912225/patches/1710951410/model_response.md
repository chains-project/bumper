Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that contains the text we want to find, and the second is a `boolean` that indicates whether the search should be case-sensitive or not. In this case, the second parameter is not needed, so we can remove it.

Also, we can simplify the code by using `AllOf` matcher, which allows us to chain multiple matchers together. We can use `StringEndsWith` matcher to check if the string ends with the image name.

This patch should fix the error and make the code compile-time ready.