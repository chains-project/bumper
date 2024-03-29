Here is a potential patch for the failing method:
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
I added explicit return type to the `matchesSafely` method and changed the `description.appendText` method to use `String.format` to include the image variable in the description.