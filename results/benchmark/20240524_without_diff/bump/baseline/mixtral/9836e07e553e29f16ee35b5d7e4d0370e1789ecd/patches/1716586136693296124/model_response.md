Here is a possible patch for the failing method:
```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced the `StringContains` constructor with `org.hamcrest.CoreMatchers.StringContains`, which is the fully-qualified name of the `StringContains` class in the Hamcrest library. This should fix the error message you provided, which indicates that the `StringContains` constructor could not be applied to the given types.

Note that this patch assumes that the Hamcrest library is still available on the classpath, and that the `StringContains` class has not been removed or renamed. If either of these assumptions is incorrect, then this patch may not work.