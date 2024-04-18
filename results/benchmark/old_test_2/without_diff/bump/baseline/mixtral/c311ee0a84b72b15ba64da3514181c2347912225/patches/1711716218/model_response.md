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
            description.appendText("a string containing the substring: Status: Downloaded newer image for ").appendValue(image);
        }
    };
}
```
In this version, I replaced the usage of `StringContains` with a custom `TypeSafeMatcher` implementation. This is necessary because the `StringContains` constructor used in the original code is not compatible with the version of the Hamcrest library being used.

The `TypeSafeMatcher` class is a part of the Hamcrest library and allows you to create custom matchers. In this case, I implemented the `matchesSafely` method to check if the input string contains the desired substring, and the `describeTo` method to provide a meaningful description of the matcher.

With these changes, the code should now compile and pass the tests.