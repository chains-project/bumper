Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is using a lambda expression to provide a function that returns the formatted string, instead of passing the format string and arguments directly to the `StringContains` constructor. This avoids the issue of the constructor expecting a single `String` argument instead of a `boolean` and a `String`.

Note that this patch assumes that the `StringContains` class and its constructor remain unchanged in the new library version. If the constructor has changed, the patch may need to be adjusted accordingly.