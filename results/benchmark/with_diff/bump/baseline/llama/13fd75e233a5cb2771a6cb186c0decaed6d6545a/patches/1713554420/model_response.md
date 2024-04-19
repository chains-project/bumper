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
The patch creates an anonymous inner class that extends `StringContains` and overrides the `matches` method to fix the error. The `StringContains` constructor taking a `boolean` and a `String` is used instead of the one taking a `String` and a `Boolean`, as the latter is not available in the updated library version. The `matches` method is implemented to check if the input string contains the expected message.