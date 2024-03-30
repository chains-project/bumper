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
            "pullImage"
        )
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the contains pattern, and the second is a `boolean` that indicates whether the pattern should be matched ignoring case or not. In this case, the second parameter is not provided, so it defaults to `false`, which means the pattern will be matched case-sensitively.

The error message suggests that the `StringContains` constructor cannot be applied to the given types, which means that the types of the parameters passed to the constructor do not match the expected types.

The fix is to change the second parameter of the `StringContains` constructor to `true`, which will make the pattern matching case-insensitive. This can be done by creating a new `StringContains` object with the same pattern and `true` as the second parameter, and then using the `AllOf` class to combine the two `StringContains` objects.

This change should fix the error and allow the code to compile successfully.