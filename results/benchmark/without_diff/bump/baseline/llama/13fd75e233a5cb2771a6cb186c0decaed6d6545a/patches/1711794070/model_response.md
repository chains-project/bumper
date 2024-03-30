Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return s.contains("Image pulled") || s.contains("Image updated");
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method to check if the input string contains either "Image pulled" or "Image updated" instead of just "Status: Downloaded newer image for". This should fix the error and make the code compile-time safe.