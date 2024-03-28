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
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a format string that includes the image name.

The error message indicates that the `StringContains` constructor cannot be applied to the given types, which means that the second parameter is not a `String`. To fix this, we can create a new `StringContains` object with the format string and the image name as arguments, and then use the `AllOf` matcher to combine it with a new `StringContains` object that looks for the word " Pulled".

This change should fix the error and allow the code to compile and run correctly.