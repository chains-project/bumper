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
            public void describeMismatch(String s, Description description) {
                description.appendText("was: " + s);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("with message: " + String.format("Status: Downloaded newer image for %s", image));
            }
        };
    }
```
The `StringContains` constructor with a boolean and a `String` has been removed in the new library version, so we need to create a new instance of `StringContains` with the `Override` decorator. We also need to implement the `matches`, `describeMismatch`, and `describeTo` methods to provide the desired behavior.

The `matches` method checks if the input string contains the expected message, and the `describeMismatch` and `describeTo` methods provide additional information for the failure message.

This patch should fix the failing test and allow the code to compile and run correctly with the new library version.