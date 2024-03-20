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
            " Pulled"
        )
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In this case, the error is happening because the second parameter is not a `String`, it's a `String.format` result.

The patch creates a new `AllOf` matcher, that contains two `StringContains` matchers, the first one is the same as before, and the second one is a new `StringContains` that checks if the string contains the word " Pulled" (with a space before)

This should fix the error and allow the code to compile.