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
                description.appendText("was expecting " + image + " but was " + s);
            }
        };
    }
```
The `StringContains` class has been updated in the new library version, and the constructor that takes two `String` arguments has been removed. To fix the error, we can create a new instance of `StringContains` with the `Override` decorator, and implement the `matches` and `describeMismatch` methods ourselves.

In the `matches` method, we check if the input `String` contains the expected message using the `contains` method. In the `describeMismatch` method, we append the expected message and the actual message to the description.

This patch should fix the error and allow the test to pass.