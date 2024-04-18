Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Status: Downloaded newer image for ") && s.contains(image);
            }

            @Override
            public void describeMismatch(String s, Description description) {
                description.appendText("was not pulled");
            }
        };
    }
```
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` and `describeMismatch` methods. The `matches` method checks if the input string contains the specified image name and the phrase "Status: Downloaded newer image for ". The `describeMismatch` method appends the text "was not pulled" to the description.

The reason for this failure is that the `StringContains` constructor that takes a single `String` argument has been removed in the new version of the library. The proposed patch creates an anonymous subclass of `StringContains` and overrides the necessary methods to achieve the same functionality.