Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String actual) {
            return super.matches(actual) && actual.contains("Downloaded newer image for " + image);
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` method to call `super.matches` and then checks if the actual string contains the expected string. The `StringContains` constructor with a single `String` argument is used instead of the one with two `String` arguments to avoid the error message.

This patch should fix the error and allow the code to compile and run correctly.