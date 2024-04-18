Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, we're now passing a function that returns a `java.lang.String`. This function takes no arguments, and its body is simply the format string with the image name inserted as a parameter.

This change addresses the error message you mentioned, which was caused by the removal of the `StringContains` constructor that took a `java.lang.String` and a `boolean` argument. The new constructor takes a `java.lang.String` and a `Supplier` (a function that returns a `java.lang.String`), which allows us to pass the format string and the image name as separate arguments.