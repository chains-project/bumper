Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that wraps the `java.lang.String.format` method call, which allows us to bypass the removed `StringContains` constructor. The lambda expression takes no arguments, so it can be inferred to have a signature of `() -> String`, which matches the expected type of the `StringContains` constructor.

Note that this patch assumes that the `java.lang.String.format` method is still available in the updated library version. If this method has been removed or modified, a different approach may be necessary.