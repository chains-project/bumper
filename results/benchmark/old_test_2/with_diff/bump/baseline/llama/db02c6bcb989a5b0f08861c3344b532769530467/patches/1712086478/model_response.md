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
The `StringContains` constructor with a single `String` argument is removed in the new library version, so we need to use the alternative constructor that takes two `String` arguments. We also need to override the `matches` method to fix the type issue. The `Override` decorator is not needed, but we keep it for clarity.