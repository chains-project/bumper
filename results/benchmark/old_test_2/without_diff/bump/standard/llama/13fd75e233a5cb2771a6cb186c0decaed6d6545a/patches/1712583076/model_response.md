Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, we're now passing a function that returns a `java.lang.String`. This function takes no arguments and returns a string formatted with the `image` parameter.

The reason for this change is that the `StringContains` constructor expects a `java.lang.String` as its second argument, but the `java.lang.String.format` method returns a `java.lang.String` object. By wrapping the call to `format` in a function, we ensure that the resulting `java.lang.String` object is properly constructed and compatible with the `StringContains` constructor.