Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            " pulle"
        )
    );
}
```
The error is caused by the fact that the `StringContains` constructor takes two parameters of type `String` and `boolean`, whereas in the original code, the second parameter is a `String` format specifier.

The proposed patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of the string " pulle" (without the leading space).

This should fix the error and allow the code to compile successfully.