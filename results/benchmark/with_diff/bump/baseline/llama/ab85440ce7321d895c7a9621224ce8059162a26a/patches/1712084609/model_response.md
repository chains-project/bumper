Here's a proposed patch to fix the failing test:
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
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method. The `matches` method is implemented to check if the input string contains the expected message format, with the image name included.

The reason for this failure is that the `StringContains` constructor that takes two parameters, `ignored` and `pattern`, has been removed in the new version of the library. Instead, a single-parameter constructor that takes a pattern string is available. To fix the failure, we create a new subclass of `StringContains` that overrides the `matches` method to check the format of the string.