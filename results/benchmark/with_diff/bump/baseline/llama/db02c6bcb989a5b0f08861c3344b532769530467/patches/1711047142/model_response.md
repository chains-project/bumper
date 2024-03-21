Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return s.contains("Status: Downloaded newer image for ") && s.contains(image);
        }
    };
}
```
The patch creates an anonymous subclass of `StringContains` that overrides the `matches` method. The `matches` method takes a `String` argument and checks if it contains the specified `image` and the string "Status: Downloaded newer image for ". If both conditions are true, it returns `true`, otherwise, it returns `false`.

The reason for this failure is that the `StringContains` constructor that takes two `String` arguments has been removed in the new library version. The proposed patch creates an anonymous subclass of `StringContains` that overrides the `matches` method, which is a valid way to use the `StringContains` class in the new library version.