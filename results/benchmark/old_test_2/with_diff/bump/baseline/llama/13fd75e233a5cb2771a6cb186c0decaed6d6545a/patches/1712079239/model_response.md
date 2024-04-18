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
                description.appendText("pulling image ");
                description.appendValue(image);
            }
        };
    }
```
The `StringContains` class has been updated to use the `matches`, `describeMismatch`, and `describeTo` methods from the `Matcher` interface, which are used to provide more informative error messages. The `StringContains` class has also been updated to use the `Override` annotation to indicate that the `matches` and `describeTo` methods are being overridden.

The `StringContains` class has also been updated to use the `String.format` method to create a message that includes the `image` parameter, which is passed to the constructor. This allows the `matches` method to use the `contains` method to check if the message contains the image name.

This patch should fix the error and allow the test to pass.