Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using the `String.format()` method, and passes the resulting string to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the `StringContains` constructor that takes two string arguments.

Note that this patch assumes that the `StringContains` class has not been modified in a way that would break the patch. If the `StringContains` class has been modified, additional changes may be necessary to the patch.