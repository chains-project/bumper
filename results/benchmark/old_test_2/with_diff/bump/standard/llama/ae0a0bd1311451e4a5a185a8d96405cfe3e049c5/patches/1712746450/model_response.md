Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change made was to replace the `java.lang.String.format()` method call with a lambda expression that formats the string using the `String.format()` method. This avoids the need for the `StringContains` constructor that takes a boolean and a string, and instead uses the constructor that takes a supplier of strings.

Note that this patch assumes that the `org.hamcrest.core.StringContains` class has not changed and still has the same constructors. If the class has been modified, the patch may need to be adjusted accordingly.