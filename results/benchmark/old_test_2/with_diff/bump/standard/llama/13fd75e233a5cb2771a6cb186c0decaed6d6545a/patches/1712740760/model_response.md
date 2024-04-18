Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor, which is now a lambda expression that formats the string using the `String.format` method. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the `StringContains` constructor with two string arguments.

Note that this patch assumes that the `org.hamcrest.core.StringContains` class has not been modified and is still compatible with the new library version. If the class has been modified, the patch may need to be adjusted accordingly.