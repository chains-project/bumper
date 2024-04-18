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
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```

This implementation uses a `TypeSafeMatcher` instead of `StringContains` from Hamcrest. The `TypeSafeMatcher` provides a more flexible way to define custom matchers, and it avoids the need to import any classes that may have been removed in the updated version of the dependency.

The `matchesSafely` method checks if the input string contains the substring "Downloaded newer image for `image`", and the `describeTo` method provides a human-readable description of the matcher.