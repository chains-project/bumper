Here's a possible patch for the given code:

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

This patch defines a new anonymous class extending `AbstractMatcher` to replace the usage of `StringContains`. This new class implements the `matches` and `describeTo` methods to provide the same functionality as the original code.