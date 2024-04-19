Here's a proposed patch to fix the error:
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
The `StringContains` constructor that takes two parameters is not available in the new version of the library, so we need to use the constructor that takes a single `String` argument and overrides the `matches` method to achieve the same functionality.