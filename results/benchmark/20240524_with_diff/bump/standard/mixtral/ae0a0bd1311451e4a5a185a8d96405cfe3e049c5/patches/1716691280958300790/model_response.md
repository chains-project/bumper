Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

Explanation:

The error message indicates that the constructor for `StringContains` now requires only one argument, a `String`, whereas the original code passed two arguments, a `boolean` and a `String`.

To fix the error, we can simply remove the first argument, `false`, from the constructor call. This will match the new constructor signature and avoid the compilation error.