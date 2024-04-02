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
                description.appendText("Image pulled");
            }
        };
    }
```
The `StringContains` constructor with a `boolean` and a `String` parameter is removed in the new version of the library, so we need to create a custom implementation that overrides the `matches`, `describeMismatch`, and `describeTo` methods. The `StringContains` class is still available, but the constructor with a `boolean` and a `String` parameter is removed, so we need to use the no-args constructor and implement the `Matcher` interface ourselves.

The `matches` method checks if the input string contains the expected string, the `describeMismatch` method appends the failure message to the description, and the `describeTo` method appends the success message to the description.

This patch should fix the failing test by providing a custom implementation of the `Matcher` interface that works with the updated library version.