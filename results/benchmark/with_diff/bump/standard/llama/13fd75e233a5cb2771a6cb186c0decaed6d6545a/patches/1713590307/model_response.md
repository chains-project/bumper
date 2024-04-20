Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not compatible with the updated version of the library.

Note that this patch assumes that the `StringContains` class has not changed in the new version of the library, and that the `format()` method is still available. If the `StringContains` class has been modified, you may need to adapt the patch accordingly.