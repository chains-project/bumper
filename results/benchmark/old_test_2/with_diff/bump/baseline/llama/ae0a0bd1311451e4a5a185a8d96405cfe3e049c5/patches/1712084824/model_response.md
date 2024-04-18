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
The `StringContains` constructor that takes a boolean and a string has been removed in the new version of the library. Therefore, we need to use the alternative constructor that takes a `Matcher` object. We also need to provide an implementation for the `matches` method to make the code compile.