Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, " Pulled")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the second parameter is not a `String`. The solution is to format the string inside the `StringContains` constructor, like this:
```java
new StringContains(false, " Pulled")
```
This will create a `StringContains` matcher that looks for the string " Pulled" inside the response.

Additionally, the `AllOf` matcher is used to combine both `StringContains` matchers, this way the method will return true only if both matchers match.

This patch should fix the error and allow the code to compile and run correctly.