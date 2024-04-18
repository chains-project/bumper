Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `boolean` value for the `ignoreCase` parameter, we're now passing a function that returns a `String` value. The function is defined as `() -> java.lang.String.format("Status: Downloaded newer image for %s", image)`. This function takes no arguments and returns a `String` value that is formatted with the `image` parameter.

This change should fix the error because the `StringContains` constructor now receives a `String` argument, which is what the `image` variable is, and not a `boolean` value.