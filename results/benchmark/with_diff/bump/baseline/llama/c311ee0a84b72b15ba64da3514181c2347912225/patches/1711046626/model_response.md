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
            public void describeMismatchSafely(String item, Description description) {
                description.appendText("was not pulled");
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("pulling image " + image);
            }
        };
    }
```
The `StringContains` class has been modified in the new library version, and the constructor that takes two `String` arguments is removed. To fix the error, we can create a new instance of `StringContains` with the `Override` decorator, and implement the `matches`, `describeMismatchSafely`, and `describeTo` methods ourselves.

In the `matches` method, we check if the input string contains the expected string format, which is constructed using the `String.format` method.
In the `describeMismatchSafely` and `describeTo` methods, we provide meaningful descriptions for the matcher.

This patch should fix the error and allow the test to pass.