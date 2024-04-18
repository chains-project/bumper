Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is using a lambda expression to provide a function that returns the formatted string, instead of passing the format string and arguments directly to the `StringContains` constructor. This avoids the incompatible parameter list issue.

Note that the `StringContains` class has not changed, so the patch does not modify the library code. The change is limited to the client code, replacing the failing `StringContains` constructor call with a lambda expression that works around the incompatibility.