Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, an anonymous function that returns a `java.lang.String` is passed. This function takes no arguments and uses the `java.lang.String.format` method to create a string with the format "Status: Downloaded newer image for %s" and the image name as an argument.

This should fix the issue because the constructor `StringContains(boolean, Function<java.lang.String, java.lang.String>)` can be applied to the given types, and the `Function` interface is implemented by the anonymous function.