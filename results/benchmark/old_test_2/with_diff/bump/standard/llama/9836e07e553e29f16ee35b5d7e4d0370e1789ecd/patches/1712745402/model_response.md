Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that returns a string format of the desired message, and passes it to the `StringContains` constructor. This avoids the issue of the removed `StringContains` constructor that took a boolean and a string argument.

Note that this patch assumes that the `StringContains` class has not been modified in a way that would break the lambda expression. If the `StringContains` class has been modified to expect a different format of the message, then a different patch may be required.