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

The issue with the original code is that it was missing a semicolon after appending the value of the `image` variable inside the `describeTo` method. I created a new variable `imagePattern` to make the code more readable, but that change is not necessary to fix the issue.