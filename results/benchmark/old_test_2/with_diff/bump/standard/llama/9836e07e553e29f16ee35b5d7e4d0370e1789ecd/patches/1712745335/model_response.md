Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using the `String.format` method, and passes the result to the `StringContains` constructor. This avoids the need to pass a boolean value as the second argument, which is no longer supported in the updated library version.

Note that this patch assumes that the `StringContains` class has not changed in the updated library version, and that the `format` method is still available. If the `StringContains` class has been modified, or if the `format` method has been removed, a different patch may be necessary.