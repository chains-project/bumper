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
The `StringContains` constructor that takes a `boolean` and a `String` has been removed in the new version of the library. We can work around this by creating an anonymous subclass of `StringContains` and overriding the `matches` method to achieve the same functionality.