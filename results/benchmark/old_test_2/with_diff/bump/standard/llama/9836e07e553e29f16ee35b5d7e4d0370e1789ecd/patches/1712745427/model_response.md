Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is to replace the `java.lang.String.format()` call with a lambda expression that formats the string using the `String.format()` method. This avoids the need for the `StringContains` constructor that takes a boolean and a string, which is no longer available in the updated library version.

Note that this patch assumes that the `java.lang.String.format()` method is still available in the updated library version. If it's not, a different solution may be needed.