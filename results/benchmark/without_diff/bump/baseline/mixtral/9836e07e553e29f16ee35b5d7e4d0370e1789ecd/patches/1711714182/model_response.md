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
            description.appendText("a string containing the substring: Downloaded newer image for " + image);
        }
    };
}
```

This version of the method creates an anonymous inner class that extends `TypeSafeMatcher<String>` and overrides the `matchesSafely` method to check if the input string contains the desired substring. The `describeTo` method is also overridden to provide a more descriptive error message when the matcher is used in an assertion and the assertion fails.

The error message indicates that the `StringContains` constructor cannot be applied to the given argument, which is a `String`. This suggests that the `StringContains` constructor being used is not the one that takes a `String` argument. The `TypeSafeMatcher` class provides a more flexible way to create matchers that can check for specific substrings within a string.

Note that the `@Override` annotation has been added to the `matchesSafely` and `describeTo` methods to ensure that they are actually overriding methods in the superclass. This annotation can help catch errors at compile-time if the methods are not actually being overridden.