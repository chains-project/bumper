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
            description.appendText("a string containing the substring: Downloaded newer image for ").appendValue(image);
        }
    };
}
```

In this version, we create an anonymous subclass of `TypeSafeMatcher` and override the `matchesSafely` method to check if the input string contains the desired substring. We also override the `describeTo` method to provide a helpful description of the matcher. This should resolve the error caused by the `StringContains` constructor not being applicable to the given types.