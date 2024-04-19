Here's a proposed patch to fix the failing test:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return s.contains("Status: Downloaded newer image for " + image);
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method. The `matches` method is implemented to check if the input string contains the expected message format, which includes the image name.

The reason for this failure is that the `StringContains` constructor that takes two arguments, a flag to indicate whether the match should be case-sensitive and the expected substring, has been removed in the new version of the library.

The patch creates a new `StringContains` instance with the `false` flag for case-sensitivity and the formatted message as the expected substring. Then, it overrides the `matches` method to check if the input string contains the expected message format.

This patch should fix the failure and allow the test to pass.