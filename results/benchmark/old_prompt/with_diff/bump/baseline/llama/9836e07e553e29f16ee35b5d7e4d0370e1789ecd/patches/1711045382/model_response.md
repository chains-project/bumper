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
The patch creates an anonymous inner class that extends `StringContains` and overrides the `matches` method. The `matches` method takes a `String` argument and checks if it contains the expected string format. The `StringContains` constructor with two arguments is used to create a matcher that expects a string containing the specified image name.


The reason for this failure is that the `StringContains` constructor with two arguments was removed in the new library version. The patch creates a new anonymous inner class that extends `StringContains` and overrides the `matches` method to achieve the same functionality.

The patch only modifies the failing method, and it does not remove or add any methods, so it should not affect other parts of the code.