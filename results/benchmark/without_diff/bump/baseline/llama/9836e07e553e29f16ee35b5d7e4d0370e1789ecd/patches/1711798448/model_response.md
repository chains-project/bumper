Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `boolean` value indicating whether the searched substring should be case-sensitive, and the second is the substring to search. In this case, the second parameter is a format string that includes the image name.

Instead of using `StringContains`, we can use `AllOf` to combine two matchers: `StringContains` and `StringEndsWith`. `StringContains` will search for the substring "Status: Downloaded newer image for " followed by the image name, while `StringEndsWith` will ensure that the image name is at the end of the string.

With this change, the error should be resolved, and the code should compile successfully.