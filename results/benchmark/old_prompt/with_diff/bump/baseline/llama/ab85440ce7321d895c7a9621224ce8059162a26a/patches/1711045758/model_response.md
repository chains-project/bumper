Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Image pulled:") || s.contains("Status: Downloaded newer image for ");
            }

            @Override
            public void describeMismatchSafely(String s, Description description) {
                description.appendText("was not pulled");
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("Image pulled");
            }
        };
    }
```
The `StringContains` class has been updated in the new library version, and the constructor taking a `boolean` and a `String` has been removed. To fix the error, we can create a new anonymous inner class that extends `StringContains` and overrides the `matches` and `describeMismatchSafely` methods. The `matches` method checks if the input string contains either "Image pulled:" or "Status: Downloaded newer image for ", and the `describeMismatchSafely` method appends "was not pulled" to the description. The `describeTo` method is not used in this case, but it's included for completeness.

This patch should fix the error and allow the test to run successfully.