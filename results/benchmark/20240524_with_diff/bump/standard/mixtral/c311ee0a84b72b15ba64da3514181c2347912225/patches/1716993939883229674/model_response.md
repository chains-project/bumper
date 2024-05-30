Here is a patch that you can apply to fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

The error message indicates that the `StringContains` constructor now requires only one argument, whereas before it required two. Therefore, we can fix the error by removing the `false` argument from the constructor.