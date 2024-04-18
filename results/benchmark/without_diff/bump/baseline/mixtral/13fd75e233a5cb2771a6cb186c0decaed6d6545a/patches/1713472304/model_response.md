Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        public boolean matches(final Object item) {
            return item != null && item instanceof String &&
                   ((String) item).contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string that contains 'Status: Downloaded newer image for " + image + "'");
        }
    };
}
```

This code creates a custom `Matcher` implementation using Hamcrest's `AbstractMatcher` class. It overrides the `matches` method to check if the given string contains the expected message. It also overrides the `describeTo` method to provide a helpful description of the matcher.

Note that this implementation does not use any deprecated or removed methods from the Hamcrest library.