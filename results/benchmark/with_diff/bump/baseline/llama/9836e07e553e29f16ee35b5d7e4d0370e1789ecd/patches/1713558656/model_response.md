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
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method to fix the error. The `matches` method takes a `String` argument and checks if it contains the expected string. The `StringContains` constructor with two arguments is used to create a `Matcher` that matches the expected string.