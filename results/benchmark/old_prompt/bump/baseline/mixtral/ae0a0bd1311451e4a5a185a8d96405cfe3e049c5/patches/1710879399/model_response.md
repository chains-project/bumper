Here's a patch for the given code to fix the error:
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
Changes made:
1. Created a `imageDescription` variable to store the string `"imagePulled(" + image + ")"`.
2. Replaced the usage of `description.appendText("a string containing ").appendValue(image));` with `description.appendText("a string containing ").appendValue(imageDescription);` to use the newly created variable.

This patch addresses the issue of a missing semicolon in the original code and simplifies the code by using a separate variable for the image description.