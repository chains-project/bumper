Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that returns a string format method, which is then passed to the `StringContains` constructor. This avoids the error caused by the removed `StringContains` constructor that took a boolean and a string argument.

Note that this patch assumes that the `StringContains` class has not been modified in a way that would break the functionality of the `imagePulled` method. If the `StringContains` class has been modified in a way that affects its behavior, additional changes to the patch may be necessary.