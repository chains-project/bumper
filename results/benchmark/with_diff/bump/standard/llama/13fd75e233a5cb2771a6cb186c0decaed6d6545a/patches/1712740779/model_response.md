Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `java.lang.String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not compatible with the updated version of the library.

Note that this patch assumes that the `java.lang.String.format()` method is available in the updated library version. If it's not available, you may need to use a different method to format the string.