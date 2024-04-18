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
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` method to fix the issue. The `StringContains` constructor now requires a `Supplier` of `String` instead of a `String` argument, which is not compatible with the previous code. By creating a new subclass and overriding the `matches` method, we can maintain the same behavior while using the new version of the library.

Please note that this patch only addresses the provided error and may not cover other potential issues in the code.