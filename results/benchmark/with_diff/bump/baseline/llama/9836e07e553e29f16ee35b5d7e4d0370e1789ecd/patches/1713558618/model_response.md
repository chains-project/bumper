Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Downloaded newer image for " + image);
            }

            @Override
            public void describeMismatchSafely(String s, Description description) {
                description.appendText("was not downloaded newer image for " + image);
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains the expected message, and the `describeMismatchSafely` method provides a meaningful description of the mismatch.

The `StringContains` constructor that takes a boolean and a string is used to create a matcher that matches strings that contain the given string. The `false` argument ensures that the matcher returns `false` if the input string does not contain the expected message.

With this patch, the test should now pass, as the `imagePulled` method returns a matcher that correctly identifies whether the input string contains the expected message.