Here's a proposed patch to fix the error:
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
            public void describeMismatchSafely(String s, Description description) {
                description.appendText("Status: Downloaded newer image for " + image);
            }
        };
    }
```
The `StringContains` constructor that takes two `String` arguments is removed in the new library version, so we need to use the alternative constructor that takes a single `String` argument and overrides the `matches` and `describeMismatchSafely` methods.

The `matches` method checks if the input string contains the expected string, and the `describeMismatchSafely` method is used to provide a meaningful description of the mismatch.

This patch should fix the error and allow the code to compile and run correctly.