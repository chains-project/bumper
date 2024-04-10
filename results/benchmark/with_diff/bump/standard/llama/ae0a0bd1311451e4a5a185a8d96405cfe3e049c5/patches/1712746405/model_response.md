Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using the `String.format` method, and passes the result to the `StringContains` constructor. This avoids the issue of the removed `StringContains` constructor that took a `boolean` and a `String` argument.

Note that this patch assumes that the `StringContains` class has not been modified in a way that breaks the lambda expression. If the `StringContains` class has been modified to not accept a lambda expression, then a different patch may be necessary.