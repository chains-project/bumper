Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using the `String.format` method, and passes the result to the `StringContains` constructor. This avoids the issue of passing a boolean value as the second argument, which is not compatible with the constructor.

Note that this patch assumes that the `StringContains` class and its constructor are unchanged, and that the issue is only with the way the constructor is being called. If the `StringContains` class or its constructor have changed, a different patch may be necessary.