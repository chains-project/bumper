Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return super.matches(s) && s.contains("Image pulled");
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` method to add an extra check for the presence of "Image pulled" in the input string. This should fix the error by providing a compatible implementation of `Matcher<String> imagePulled(final String image)` that can be used with the updated library version.