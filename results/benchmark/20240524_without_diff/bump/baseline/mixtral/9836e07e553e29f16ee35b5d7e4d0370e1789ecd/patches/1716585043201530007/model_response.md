Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(this.description);
        }
    };
}
```

This patch uses the `AbstractMatcher` class from Hamcrest to create a custom matcher for the expected log message. The `matchesSafely` method checks if the given string contains the description of the matcher.

Note: This patch assumes that the `AbstractMatcher` class is available in the Hamcrest library. If it is not, you can use the `TypeSafeMatcher` class instead, which is a more verbose way of creating custom matchers.