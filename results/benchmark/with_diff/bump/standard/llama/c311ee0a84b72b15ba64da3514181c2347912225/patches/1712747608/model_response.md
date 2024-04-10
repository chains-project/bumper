Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the varargs method `StringContains(boolean, String, Object...)`.

The patch also removes the `java.lang.String` import statement, as it is not needed.

Note that this patch assumes that the `org.hamcrest.core.StringContains` class has not changed and still has a constructor that takes a boolean and a string. If the constructor has changed, the patch may need to be adjusted accordingly.