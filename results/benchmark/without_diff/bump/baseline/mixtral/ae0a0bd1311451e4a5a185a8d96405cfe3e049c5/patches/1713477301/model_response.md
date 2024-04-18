Here's a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("a string containing") {
        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ");
            description.appendText(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```

This patch defines a new anonymous class extending `AbstractMatcher` and overriding the `describeTo` and `matchesSafely` methods. This allows us to define a custom matcher that checks whether a string contains the given substring, while avoiding the use of the deprecated `StringContains` constructor.