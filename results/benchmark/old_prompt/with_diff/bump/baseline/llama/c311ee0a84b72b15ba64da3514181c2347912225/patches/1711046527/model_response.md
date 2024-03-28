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
            public void describeMismatchSafely(String s, Description description) {
                description.appendText("was not pulled");
            }
        };
    }
```
The `StringContains` constructor that takes two `String` arguments is not available in the new version of the library. To fix the failure, we can create a new instance of `StringContains` with the `Override` decorator and implement the `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains the expected string, and the `describeMismatchSafely` method describes the mismatch.

The proposed patch creates a new `StringContains` instance with the `Override` decorator and implements the `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains the expected string, and the `describeMismatchSafely` method describes the mismatch.

This patch should fix the failure and allow the test to pass.