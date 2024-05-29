Here is a possible patch for the failing method:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
This patch uses the `StringStartsWith` matcher instead of `StringContains`, which only takes one argument. The behavior of the test may be different, so you should make sure that this is the desired behavior.