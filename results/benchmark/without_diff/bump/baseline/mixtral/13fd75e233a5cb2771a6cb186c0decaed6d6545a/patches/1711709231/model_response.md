Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the text: Status: Downloaded newer image for ").appendValue(image);
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```

This version of the method defines a new anonymous class that extends `TypeSafeMatcher<String>` and overrides the `describeTo` and `matchesSafely` methods. This allows us to define a custom matcher that checks if a string contains a specific substring, without relying on the deprecated `StringContains` constructor.