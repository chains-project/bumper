Here's a patch that you can apply to the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, I replaced the `StringContains` constructor with `StringStartsWith`, which has the same number of arguments as the original constructor. This should resolve the error message you encountered.