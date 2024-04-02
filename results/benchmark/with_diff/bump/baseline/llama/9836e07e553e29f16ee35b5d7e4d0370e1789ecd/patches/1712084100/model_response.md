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
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method. The `matches` method is implemented to check if the input string contains the expected message. The `StringContains` constructor taking a `boolean` and a `String` is used, as the `String` parameter is not mandatory.