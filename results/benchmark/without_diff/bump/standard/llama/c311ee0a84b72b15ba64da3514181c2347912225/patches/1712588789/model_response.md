Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor, which is now a lambda expression that returns a string format with the image name. This avoids the need to pass a boolean value as the first argument, which was causing the constructor to fail.

Note that this patch assumes that the `StringContains` class and its constructor are unchanged. If the constructor has been modified, the patch may need to be adjusted accordingly.