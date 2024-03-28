Here is a patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    String imageDescription = "imagePulled(" + image + ")";
    return new TypeSafeMatcher<String>() {
        @Override
        public boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing ").appendValue(imageDescription);
        }
    };
}
```
The issue with the original code is that the method `describedAs` is being called instead of `describeTo`. The `describedAs` method does not exist in the `TypeSafeMatcher` class, which is why the error message is complaining about a missing semicolon. I replaced it with the correct method `describeTo` and added a variable to make the code more readable.