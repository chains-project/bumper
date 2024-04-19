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
The patch creates an anonymous subclass of `StringContains` and overrides the `matches` method to fix the error. The `matches` method takes a `String` argument named `s` and checks if it contains the expected string format.

The `StringContains` constructor with a `boolean` and a `String` was removed in the new library version, so we had to create a new class that extends `StringContains` and overrides the `matches` method.

The `String.format` method is still used to create the expected string format, but now it's passed as a `String` argument to the `StringContains` constructor.

This patch should fix the failing test and allow the code to compile and run correctly.