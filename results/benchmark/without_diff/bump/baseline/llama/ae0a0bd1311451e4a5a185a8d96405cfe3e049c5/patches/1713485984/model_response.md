Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            "pullImage"
        )
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name, which causes the error.

The proposed patch uses the `AllOf` class from the same package as `StringContains`, which allows combining multiple matchers into a single matcher. The first matcher is the same as before, but the second matcher is a new `StringContains` instance that searches for the string "pullImage". This should fix the error and make the code compile-time friendly.