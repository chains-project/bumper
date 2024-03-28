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
The patch creates an anonymous inner class that extends `StringContains` and overrides its `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains the expected message, and the `describeMismatchSafely` method appends a descriptive text to the provided description.

The reason for this failure is that the `StringContains` constructor that takes two parameters, `expected` and `message`, has been removed in the new version of the library. Instead, you can create an anonymous inner class that extends `StringContains` and overrides its `matches` and `describeMismatchSafely` methods.

This patch should fix the failing test, as it uses the updated `StringContains` constructor and provides the necessary implementations for the `matches` and `describeMismatchSafely` methods.