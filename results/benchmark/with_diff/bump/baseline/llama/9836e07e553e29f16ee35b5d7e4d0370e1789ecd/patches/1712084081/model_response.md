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
            public void describeMismatch(String s, Description description) {
                description.appendText("was not pulled");
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` and `describeMismatch` methods. The `matches` method checks if the input string contains the expected message, and the `describeMismatch` method appends the reason for the mismatch to the description.

The `StringContains` constructor that takes a boolean and a string is used to create a matcher that matches strings that contain the given string. The `Override` annotation is used to indicate that the `matches` and `describeMismatch` methods are being overridden.

This patch should fix the error and allow the test to pass.