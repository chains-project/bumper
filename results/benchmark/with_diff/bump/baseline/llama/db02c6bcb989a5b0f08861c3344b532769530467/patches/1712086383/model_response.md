Here's a proposed patch to fix the error:
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
The `StringContains` constructor that takes two parameters is removed in the new library version, so we need to use the one that takes a single `String` parameter and overrides the `matches` method to achieve the same result.