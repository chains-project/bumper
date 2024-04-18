Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes the image name as an argument. This avoids the need for the `StringContains` constructor that is no longer available in the updated library version.

Note that this patch assumes that the `StringContains` class has not been modified in a way that breaks the lambda expression. If the `StringContains` class has been modified in a way that breaks the lambda expression, a different patch may be required.