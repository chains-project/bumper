Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.core.StringContains.StringStartsWith(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `StringStartsWith` constructor from the same `org.hamcrest.core` package. This constructor takes a single argument, which is the expected prefix of the inspected string. This should resolve the compilation error.

Note that this patch assumes that the `StringStartsWith` constructor was added in a newer version of the library, while the `StringContains` constructor was removed. If this is not the case, then the patch may not work.