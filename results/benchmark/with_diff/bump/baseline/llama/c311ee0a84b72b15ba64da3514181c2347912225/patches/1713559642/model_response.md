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
The `StringContains` constructor that takes two arguments is not applicable because the second argument is not a `String`. The solution is to create an anonymous class that extends `StringContains` and overrides the `matches` method. The `matches` method checks if the input string contains the expected string format.

The `StringContains` class has not changed in the new library version, so this patch should work with the updated library.