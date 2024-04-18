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
                description.appendText("was ");
                description.appendValue(s);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("a string containing ");
                description.appendValue(image);
            }
        };
    }
```
The `StringContains` constructor that takes a `boolean` and a `String` parameter is removed in the new version of the library, so we need to create a new instance of `StringContains` with the `Override` decorator and implement the `matches`, `describeMismatch`, and `describeTo` methods ourselves.

In the `matches` method, we use the `contains` method to check if the input string contains the expected string. In the `describeMismatch` method, we append the input string and the expected string to the description. In the `describeTo` method, we append the expected string to the description.

This patch should fix the error and allow the test to pass.