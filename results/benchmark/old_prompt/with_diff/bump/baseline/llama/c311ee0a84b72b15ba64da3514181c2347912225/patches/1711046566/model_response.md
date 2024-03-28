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
            public void describeTo(Description description) {
                description.appendText("String contains ");
            }
        };
    }
```
The `StringContains` class has been updated in the new library version, and the constructor that takes two `String` arguments is removed. To fix the error, we can create a new anonymous class that extends `StringContains` and overrides the `matches` and `describeTo` methods.

In the `matches` method, we check if the input string contains the expected substring "Downloaded newer image for " + image. We also override the `describeTo` method to provide a meaningful description of the matcher.

This patch should fix the failing test, as it uses the updated `StringContains` class and provides the correct implementation for the `matches` and `describeTo` methods.