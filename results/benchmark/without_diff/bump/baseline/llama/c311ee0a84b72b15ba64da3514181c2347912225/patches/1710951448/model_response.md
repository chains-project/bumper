Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(false, "Status: Downloaded newer image for " + image),
            new StringEndsWith(image)
        );
    }
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In this case, the second parameter is a format string that includes the image name.

Instead of using `StringContains`, we can use `AllOf` to combine two matchers: `StringContains` and `StringEndsWith`. `StringEndsWith` is used to check that the image name is present at the end of the string.

This change should fix the error and allow the code to compile successfully.