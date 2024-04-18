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
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` method to fix the error. The `StringContains` constructor with a `boolean` parameter is not applicable due to the removal of the `java.lang.String` parameter in the new library version. Instead, we create a new `StringContains` instance with the `String` parameter and override the `matches` method to achieve the desired result.