Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that returns a string format method, which takes the image name as a parameter. The lambda expression is then passed to the `StringContains` constructor, which now takes a single argument of type `java.lang.String`. This fixes the error by providing the correct number of arguments to the constructor.

Note that this patch assumes that the `StringContains` class has not changed in the new library version, and that the `format` method is still available in the `java.lang.String` class. If these assumptions are not correct, a different patch may be required.