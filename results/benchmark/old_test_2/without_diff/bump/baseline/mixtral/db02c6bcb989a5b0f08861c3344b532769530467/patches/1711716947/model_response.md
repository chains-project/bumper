Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Downloaded newer image for ").appendValue(image);
        }
    };
}
```

Explanation:

The original implementation of the `imagePulled` method uses the `StringContains` class from the Hamcrest library to check if a string contains a substring. However, the error message indicates that the `StringContains` constructor cannot be applied to the given type.

To resolve this issue, we can create a custom `Matcher` that extends the `TypeSafeMatcher` class and implements the `matchesSafely` method to check if the input string contains the desired substring. We can then use the `appendText` and `appendValue` methods of the `Description` class to provide a descriptive error message.

This implementation avoids using the `StringContains` class and instead uses the more general `contains` method of the `String` class to check if the input string contains the desired substring. It also provides a descriptive error message that explains what the matcher is looking for.

Note: I am assuming that the `TypeSafeMatcher` and `Description` classes are available in the current version of the Hamcrest library. If not, you may need to find an alternative way to implement the custom matcher.