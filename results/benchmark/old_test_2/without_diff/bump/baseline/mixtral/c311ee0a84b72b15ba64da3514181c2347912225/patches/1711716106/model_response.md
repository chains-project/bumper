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

This version of the method defines a new anonymous class that extends `TypeSafeMatcher<String>` and overrides the `matchesSafely` method to check if the input string contains the desired substring. It also overrides the `describeTo` method to provide a more descriptive error message when the matcher fails.

The `StringContains` class from the Hamcrest library has been removed in newer versions, which is why the original code is causing an error. By defining our own matcher, we can avoid using the deprecated library method and ensure that our code is compatible with newer versions of the library.