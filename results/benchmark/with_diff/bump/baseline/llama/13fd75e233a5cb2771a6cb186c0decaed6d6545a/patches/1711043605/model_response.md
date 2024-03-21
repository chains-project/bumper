Here's a proposed patch to fix the error:
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
            public void describeTo(Description description) {
                description.appendText("Image pulled: " + image);
            }
        };
    }
```
The `StringContains` constructor that takes two parameters `matcher` and `description` has been removed in the new version of the library. Therefore, we need to create an anonymous class that implements the `Matcher` interface and overrides its `matches` and `describeTo` methods.

In the `matches` method, we use the `contains` method to check if the input string contains the expected string.
In the `describeTo` method, we append the expected string to the description.

This patch should fix the error and allow the code to compile and run correctly.