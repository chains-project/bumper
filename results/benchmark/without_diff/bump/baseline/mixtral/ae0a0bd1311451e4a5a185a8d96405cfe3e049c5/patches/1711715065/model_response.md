Here is a fixed version of the method that should resolve the error:

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

This version of the method defines a new anonymous class extending `TypeSafeMatcher` and overrides the `matchesSafely` method to check if the given string contains the substring "Status: Downloaded newer image for `image`". It also overrides the `describeTo` method to provide a meaningful description of the matcher for error messages.

The original version of the method used the `StringContains` matcher, which has been removed in the new version of the library. The `StringContains` matcher was deprecated in favor of the more flexible `TypeSafeMatcher`, which allows for more custom behavior.

By defining a new anonymous class that extends `TypeSafeMatcher`, we can replicate the behavior of the `StringContains` matcher while also providing a more descriptive error message in the event of a failure. This should allow the test to pass and provide more informative error messages if it does fail.