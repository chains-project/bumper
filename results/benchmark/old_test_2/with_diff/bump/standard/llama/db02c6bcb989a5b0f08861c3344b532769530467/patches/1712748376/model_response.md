Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that returns a string format method, which is then passed to the `StringContains` constructor. This avoids the issue of the removed `StringContains` constructor that took a boolean and a string argument.

Note that this patch assumes that the `StringContains` class and its constructor are still available in the updated library version. If the `StringContains` class has also been removed, a different approach may be needed.