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
                description.appendText("was not pulled");
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains the expected message, and the `describeMismatchSafely` method appends a descriptive message to the given description.

The `StringContains` constructor that takes a boolean and a string is not used anymore, instead, the anonymous subclass is used to provide the needed functionality.

This patch should fix the error and allow the test to run successfully.