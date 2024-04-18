Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, an anonymous function that returns a `java.lang.String` is passed. This function takes no arguments and uses the `image` parameter to format the string.

This should fix the error because the anonymous function takes the `image` parameter and returns a `java.lang.String` instance, which matches the expected type of the second argument of the `StringContains` constructor.