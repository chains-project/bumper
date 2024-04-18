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
            " Pulled"
        )
    );
}
```
The `StringContains` constructor takes two parameters, the first is a `String` that represents the container, and the second is a `String` that represents the contained string. In this case, the error is happening because the second parameter is not a `String` but a `String` formatted with `%s`.

The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for %s" and the second `StringContains` matcher checks for the presence of the string " Pulled".

This should fix the error and allow the code to compile.