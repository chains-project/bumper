Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return s.contains("Downloaded newer image for " + image);
        }
    };
}
```
The `StringContains` constructor that takes two arguments, `ignored` and `pattern`, has been removed in the new library version. To fix the error, we can create a new instance of `StringContains` with the `pattern` argument only and override the `matches` method to achieve the same functionality.

The `matches` method checks if the input string contains the pattern "Downloaded newer image for " + image, which is the same logic as the original code.

This patch should fix the error and make the code compile-able with the new library version.