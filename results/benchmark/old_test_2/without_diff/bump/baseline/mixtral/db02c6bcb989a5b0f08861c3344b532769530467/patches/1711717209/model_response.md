Here is a proposed patch for the `imagePulled` method:
```
private static Matcher<String> imagePulled(final String image) {
    return new TypeSafeMatcher<String>() {
        @Override
        public boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText(String.format("a string containing the substring: Status: Downloaded newer image for %s", image));
        }
    };
}
```
I changed the return type of the `matchesSafely` method from `void` to `boolean`, and updated the `describeTo` method to use `String.format` to include the image name in the description.