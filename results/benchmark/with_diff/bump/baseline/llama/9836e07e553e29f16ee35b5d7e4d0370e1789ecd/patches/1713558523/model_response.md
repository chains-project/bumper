Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ) {
        @Override
        public boolean matches(String s) {
            return s.contains("Image pulled: ") && s.contains(image);
        }
    };
}
```
The `StringContains` constructor that takes two `String` arguments is removed in the new library version, so we need to use the alternative constructor that takes a `boolean` and a `String`. We also need to override the `matches` method to fix the error. The `StringContains` class is from the Hamcrest library, which is not modified in the new version, so we can still use it.