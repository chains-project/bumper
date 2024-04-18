Here's a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        public boolean matches(final Object item) {
            return item != null && item instanceof String
                && ((String) item).contains(this.expected);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing \"").appendText(expected).appendText("\"");
        }
    };
}
```

In this patch, we replace the `StringContains` matcher with a custom matcher that extends `AbstractMatcher`. This allows us to define our own `matches` and `describeTo` methods that use the `contains` method of the `String` class, which is an added method in Hamcrest 1.3 (identified with `++`).

Note that this patch assumes that the failure is caused by an external dependency update that removes the `StringContains` matcher. If the failure is caused by a different issue, this patch may not work.