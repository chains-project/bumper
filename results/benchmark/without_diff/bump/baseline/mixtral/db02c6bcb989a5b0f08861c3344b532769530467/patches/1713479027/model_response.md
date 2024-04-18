Here is a possible patch for the code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        public void describeTo(Description description) {
            description.appendText("string contains \"Status: Downloaded newer image for \" and ends with: ").appendValue(image);
        }

        @Override
        protected boolean matchesSafely(String item) {
            return item.contains("Status: Downloaded newer image for " + image) && item.endsWith(image);
        }
    };
}
```

This patch uses the AbstractMatcher class from Hamcrest to create a custom matcher that checks if a string contains the specified substring and ends with the specified suffix. This should be equivalent to the original code, but it does not use the deprecated StringContains constructor.