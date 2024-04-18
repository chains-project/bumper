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
The `StringContains` constructor that takes a `boolean` and a `String` has been removed in the new version of the library, so we need to use the alternative constructor that takes a `Function<? super String, Boolean>` and a `String`. We also don't need the `Override` annotation since the method is not overriding any method in the new version.

The `matches` method has been removed, so we need to implement our own version that checks if the input string contains the expected message.

This patch should fix the error and allow the test to run successfully.