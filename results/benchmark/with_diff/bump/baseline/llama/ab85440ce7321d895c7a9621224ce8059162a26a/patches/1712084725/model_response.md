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
                description.appendText("image pulled");
            }
        };
    }
```
The `StringContains` class has been updated in the new library version, and the constructor that takes two `String` arguments has been removed. To fix the failure, we can create a new instance of `StringContains` with the `boolean` value set to `false` and the message to be matched as a `String`. Then, we need to implement the `matches`, `describeMismatch`, and `describeTo` methods to mirror the behavior of the removed constructor.

In the `matches` method, we check if the input `String` contains the message we want to match. In the `describeMismatch` method, we append the text "was not pulled" to the description. In the `describeTo` method, we append the text "image pulled" to the description.

This patch should allow the test to pass without modifying the function signature or removing the `Override` decorator.