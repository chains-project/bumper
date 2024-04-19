Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(final String actual) {
            return super.matches(actual) && !actual.contains("pull");
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method to filter out strings containing "pull". The `StringContains` constructor taking a boolean and a string argument is used to maintain compatibility with the existing code.