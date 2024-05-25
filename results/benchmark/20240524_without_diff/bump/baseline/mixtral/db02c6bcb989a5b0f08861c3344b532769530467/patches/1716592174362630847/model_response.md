Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.Matchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we're using the fully-qualified name for the `StringContains` class, which is now located in the `org.hamcrest.Matchers` package. This should resolve the compilation error.