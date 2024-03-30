```
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                false,
                " Pulled"
            )
        );
    }
```
The `StringContains` constructor takes two parameters, a `pattern` and a `message`, and it's used to create a matcher that matches when the examined string contains the specified `pattern`. In the original code, the second argument passed to the `StringContains` constructor is a string literal, which doesn't match the expected pattern.

The error message indicates that the constructor `StringContains` in the class `org.hamcrest.core.StringContains` cannot be applied to the given types, which means that the second argument passed to the constructor is not a string.

The proposed patch creates a new `AllOf` matcher, which takes two matchers as arguments, and matches when both of them match. The first argument passed to the `AllOf` constructor is a `StringContains` matcher that matches the string "Status: Downloaded newer image for" followed by the image name, and the second argument is another `StringContains` matcher that matches the string " Pulled".
The `AllOf` matcher returned by the `imagePulled` method will match a string that contains both the specified patterns.