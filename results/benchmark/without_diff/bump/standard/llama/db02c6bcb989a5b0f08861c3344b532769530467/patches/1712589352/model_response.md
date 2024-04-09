Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, we're now passing a function that returns a `java.lang.String`. This function takes no arguments, and simply calls `java.lang.String.format` with the desired format string and the `image` parameter.

This change allows the constructor to be applied with the correct types, as the function returns a `java.lang.String` that can be passed to the constructor.