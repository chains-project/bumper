Here's a patch for the given code to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    String imagePattern = String.format("Status: Downloaded newer image for %s", image);
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(imagePattern);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ").appendValue(image);
        }
    }.describedAs("imagePulled(" + image + ")");
}
```
Changes made:
1. Declared a variable `imagePattern` for the formatted string to avoid repetition of the formatting code.
2. Replaced the direct use of `item.contains(String.format("Status: Downloaded newer image for %s", image))` with `item.contains(imagePattern)`.
This should resolve the compilation error.