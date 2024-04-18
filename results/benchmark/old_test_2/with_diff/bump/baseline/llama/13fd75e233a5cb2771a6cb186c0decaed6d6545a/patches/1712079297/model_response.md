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
The `StringContains` constructor that takes two `String` arguments is removed in the new library version, so we need to use the alternative constructor that takes a `boolean` and a `String`. We also need to override the `matches` method to fix the error. The `Override` decorator is not needed as the method is not overriding any method in the new version.

Note that this patch assumes that the `StringContains` class is still available in the new library version, if it's not, you may need to use a different class or create a custom implementation of the `Matcher` interface.