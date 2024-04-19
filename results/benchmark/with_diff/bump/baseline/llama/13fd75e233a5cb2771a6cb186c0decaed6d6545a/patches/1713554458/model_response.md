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

            @Override
            public void describeTo(Description description) {
                description.appendText("image pulled");
            }
        };
    }
```
The patch creates an anonymous inner class that extends `StringContains` and overrides its `matches`, `describeMismatch`, and `describeTo` methods.
The `matches` method checks if the input string contains the expected message.
The `describeMismatch` method appends the message "was not pulled" to the description.
The `describeTo` method appends the message "image pulled" to the description.
The `StringContains` constructor with two parameters is used instead of the one with three parameters to avoid the error caused by the external dependency.