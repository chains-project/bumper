Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch creates a lambda expression that formats the string using `String.format()` and passes it to the `StringContains` constructor. This avoids the issue of passing a boolean and a string to the constructor, which is not allowed due to the removal of the `StringContains` constructor that takes a boolean and a string.

The lambda expression is used to create a function that returns a string, which can be passed to the `StringContains` constructor. The `() ->` syntax is used to create a lambda expression that takes no arguments and returns a string. The `java.lang.String.format()` method is used to format the string with the image name.

This patch should fix the failure and allow the code to compile and run correctly.