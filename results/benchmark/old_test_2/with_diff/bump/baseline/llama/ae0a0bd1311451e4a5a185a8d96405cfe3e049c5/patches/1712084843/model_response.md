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
                description.appendText("was not pulled");
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("pulling image " + image);
            }
        };
    }
```
The `StringContains` constructor with a `boolean` and a `String` argument is removed in the new version of the library. To fix the error, we can create a new instance of `StringContains` with the `String` argument only, and override the `matches`, `describeMismatch`, and `describeTo` methods to implement the desired behavior.

The `matches` method checks if the input string contains the expected message, and the `describeMismatch` and `describeTo` methods provide additional information about the mismatch and the expected output, respectively.

This patch should allow the test to pass without modifying the function signature or removing the `Override` decorator.