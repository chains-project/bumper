Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
We've replaced `java.lang.String.format("Status: Downloaded newer image for %s", image)` with `() -> java.lang.String.format("Status: Downloaded newer image for %s", image)`, which creates a lambda expression that returns a string formatted with the image name.


The `StringContains` constructor that takes a boolean and a string is now invoked with the lambda expression as its second argument, which resolves the type mismatch issue.