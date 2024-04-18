Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is using a lambda expression to provide a function that returns the formatted string, instead of passing the format string and arguments directly to the `StringContains` constructor. This way, we avoid the issue of the removed `StringContains` constructor that took a boolean and a `String` argument.

Note that this patch assumes that the `java.lang.String.format` method is available in the updated library version. If it's not available, you may need to use a different method to format the string.