Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(true, " Pulled")
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the full match, and the second is a `Boolean` that indicates whether the match should be case-sensitive. In this case, we're passing `false` as the second argument, which means the match will be case-insensitive.

The error message indicates that the `StringContains` constructor cannot be applied to the given types, which means that the compiler is trying to pass a `Boolean` value as the second argument instead of a `Boolean` variable.

To fix this issue, we can create a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher will look for the string "Status: Downloaded newer image for " followed by the image name, and the second `StringContains` matcher will look for the string " Pulled". The `AllOf` matcher will ensure that both matchers must match for the entire string to be considered a match.

This change should fix the error and allow the code to compile without any issues.