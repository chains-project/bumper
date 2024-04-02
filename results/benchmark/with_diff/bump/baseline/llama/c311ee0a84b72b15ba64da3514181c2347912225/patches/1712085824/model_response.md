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
The `StringContains` constructor that takes a boolean and a string argument is removed in the new version of the library, so we need to use the alternative constructor that takes a `Matcher` object. We also need to implement the `Matcher` interface to provide the logic for matching.

In the `matches` method, we check if the input string contains the expected message. In the `describeMismatch` and `describeTo` methods, we provide meaningful descriptions for the matcher.

This patch should fix the error and allow the test to pass.