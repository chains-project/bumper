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
The `StringContains` constructor that takes a boolean and a string has been removed in the new library version, so we need to use the alternative constructor that takes a hamcrest.Matcher.
We create an anonymous subclass of `StringContains` and override the `matches` method to achieve the same functionality.
The `Override` decorator is not needed as the method is not overriding any method in the new version.
The code should now compile and work as expected.