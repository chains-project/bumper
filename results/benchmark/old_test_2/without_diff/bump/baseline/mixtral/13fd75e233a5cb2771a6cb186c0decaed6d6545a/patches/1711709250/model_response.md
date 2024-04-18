Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```

In this version, I replaced the `StringContains` matcher with a custom `TypeSafeMatcher`. This allows us to use the `contains` method of the `String` class to check if the desired substring is present in the input string. I also added a `describeTo` method that provides a more informative error message when the matcher fails.