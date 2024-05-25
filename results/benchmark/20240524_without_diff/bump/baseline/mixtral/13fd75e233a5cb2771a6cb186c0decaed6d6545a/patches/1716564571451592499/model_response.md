Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor call with a fully-qualified name `org.hamcrest.CoreMatchers.StringContains` to avoid conflicts with any other classes with the same name. This assumes that the `org.hamcrest.CoreMatchers` class is available in the classpath.