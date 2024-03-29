Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected booleanmatchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```

In this version, we define a new anonymous class extending `TypeSafeMatcher` instead of using the `StringContains` class. This allows us to define our own `matchesSafely` method, which checks if the input string contains the desired substring. We also provide a `describeTo` method that generates a helpful description of the matcher, which can be useful for debugging and testing.