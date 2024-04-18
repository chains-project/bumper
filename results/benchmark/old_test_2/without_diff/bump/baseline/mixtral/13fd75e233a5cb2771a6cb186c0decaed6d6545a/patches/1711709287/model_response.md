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

In this version, I replaced the `StringContains` matcher with a custom `TypeSafeMatcher` that checks if the string contains the desired substring. The `matchesSafely` method implements the actual comparison logic, and the `describeTo` method provides a human-readable description of the matcher for debugging purposes.

Note that the `TypeSafeMatcher` class is part of Hamcrest's matcher library, so it should be available in the project's classpath. If not, you may need to add a dependency to the Hamcrest library in your project's build configuration.