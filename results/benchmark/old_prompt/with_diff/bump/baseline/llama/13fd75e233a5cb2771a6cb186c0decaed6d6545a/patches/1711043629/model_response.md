Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Status: Downloaded newer image for " + image);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("Image pulled: " + image);
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` and `describeTo` methods. The `matches` method checks if the input string contains the expected string format, and the `describeTo` method appends the description of the image pull status to the given description.

The reason for this failure is that the `StringContains` constructor that takes a boolean and a string has been removed in the new version of the library. The proposed patch creates an anonymous subclass of `StringContains` that overrides the necessary methods to achieve the same functionality.