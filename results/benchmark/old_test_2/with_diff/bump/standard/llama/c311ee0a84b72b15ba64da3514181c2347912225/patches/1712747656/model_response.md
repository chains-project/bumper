Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the `StringContains` constructor that takes a boolean and a string.

Note that this patch assumes that the `StringContains` class and its constructor are still available in the updated library version. If the `StringContains` class has been removed or renamed, a different approach may be needed to fix the error.