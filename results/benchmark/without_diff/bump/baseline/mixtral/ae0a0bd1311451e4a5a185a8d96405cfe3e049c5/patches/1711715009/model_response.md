Here is a fixed version of the `imagePulled` method that should resolve the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```
Explanation:

The original code is using the `StringContains` class from Hamcrest library to check if a string contains a certain substring. However, the error message suggests that the `StringContains` constructor cannot be applied to the given type.

To fix this issue, we can create a custom `TypeSafeMatcher` that extends the `Matcher` interface. This custom matcher will have a `matchesSafely` method that checks if the input string contains the desired substring. Additionally, we can override the `describeTo` method to provide a more descriptive error message in case the matcher fails.

Note that we cannot use the `StringContains` class directly, as it may have been removed in the new version of the library. Instead, we create our own matcher that achieves the same functionality.