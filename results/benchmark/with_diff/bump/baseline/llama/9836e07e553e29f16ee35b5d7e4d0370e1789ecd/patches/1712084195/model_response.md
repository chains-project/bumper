Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String item) {
            return super.matches(item) && !item.contains("pull");
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method to filter out strings containing "pull". This fixes the error by providing a single-argument matcher that matches the updated dependency.