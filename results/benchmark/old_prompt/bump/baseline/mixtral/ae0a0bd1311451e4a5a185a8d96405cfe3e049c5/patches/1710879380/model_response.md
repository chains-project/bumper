Here's a patch for the given code failure:

```java
private static Matcher<String> imagePulled(final String image) {
    String imagePattern = String.format("Status: Downloaded newer image for %s", image);
    return new TypeSafeMatcher<String>() {
        @Override
        public boolean matchesSafely(String item) {
            return item.contains(imagePattern);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ").appendValue(image);
        }
    }.describedAs("imagePulled(" + image + ")");
}
```

The fix includes storing the image pattern in a local variable, `imagePattern`, and using it in the `matchesSafely` method. This eliminates the need for the `String.format()` call inside the method, simplifying the code and fixing the error.