Here's a possible patch for the code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        public boolean matches(final Object item) {
            return item != null && item instanceof String
                && ((String) item).contains(this.description);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing: ").appendDescriptionOf(this.description);
        }
    };
}
```

This patch uses the `AbstractMatcher` class from Hamcrest to create a custom matcher for the expected log message. The `AbstractMatcher` class is a part of the Hamcrest library, so it should be available in the project's classpath.

The `matches` method checks if the given object is a string and contains the expected log message. The `describeTo` method provides a human-readable description of the matcher's expected value.

Note that the `StringContains` class is not used in this patch. The `contains` method from the `String` class is used instead. This should avoid the "constructor StringContains in class org.hamcrest.core.StringContains cannot be applied to given types" error.