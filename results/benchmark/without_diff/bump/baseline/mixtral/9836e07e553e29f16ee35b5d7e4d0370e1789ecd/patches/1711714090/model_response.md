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

In this version, we create a new anonymous class that extends `TypeSafeMatcher` and overrides the `matchesSafely` method to check if the input string contains the desired substring. We also override the `describeTo` method to provide a more informative error message if the matcher fails. This implementation should be compatible with both the old and new versions of the Hamcrest library.