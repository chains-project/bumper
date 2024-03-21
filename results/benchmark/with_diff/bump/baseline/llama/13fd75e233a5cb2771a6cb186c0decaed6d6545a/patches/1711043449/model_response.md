Here's a proposed patch to fix the error:
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
                description.appendText("Status: Downloaded newer image for " + image);
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` and `describeTo` methods. The `matches` method checks if the input string contains the expected message, and the `describeTo` method appends the expected message to the description.

The reason for this change is that the `StringContains` constructor that takes a boolean and a string is deprecated in the new version of the library, and the `StringContains` class has been modified to not have a constructor that takes a boolean and a string. Instead, you must create an anonymous subclass and override the `matches` and `describeTo` methods.

This patch should fix the error and allow the code to compile and run correctly.