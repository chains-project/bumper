Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the varargs method in the updated library version.

Note that this patch assumes that the `StringContains` class has not changed and still has a constructor that takes a boolean and a supplier of a string. If the `StringContains` class has also changed, additional modifications may be needed to the patch.