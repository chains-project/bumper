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
                description.appendText("image pulled");
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` and `describeTo` methods. The `matches` method checks if the input string contains the expected message, and the `describeTo` method appends the text "image pulled" to the description.

The reason for this failure is that the `StringContains` constructor that takes two parameters, `actual` and `expected`, has been removed in the new version of the library. Instead, you can create an anonymous subclass of `StringContains` and override the `matches` and `describeTo` methods to achieve the same functionality.