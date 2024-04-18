Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that returns a string format method, which takes the image name as an argument, and uses it as the second argument for the `StringContains` constructor. This way, the constructor's second argument is now a function that returns a string, rather than a string literal, which fixes the incompatibility issue with the updated library version.

Note that this patch assumes that the `java.lang.String.format` method is still available in the updated library version. If it's not, you may need to use a different method to format the string.