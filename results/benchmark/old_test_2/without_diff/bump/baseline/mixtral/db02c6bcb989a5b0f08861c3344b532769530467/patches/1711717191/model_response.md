Here is a proposed patch for the given failing method:
```java
private static Matcher<String> imagePulled(final String image) {
    boolean containsCorrectSubstring(String item) {
        String lookup = String.format("Status: Downloaded newer image for %s", image);
        return item.contains(lookup);
    }

    return new TypeSafeMatcher<String>() {
        @Override
        public boolean matchesSafely(String item) {
            return containsCorrectSubstring(item);
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing the substring: Status: Downloaded newer image for " + image);
        }
    };
}
```
This patch defines a new helper method `containsCorrectSubstring` that checks if a given string contains the expected substring. This method is then used in the `matchesSafely` method of the `TypeSafeMatcher`. This should resolve the error message about the missing return type.