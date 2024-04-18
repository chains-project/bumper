Here's a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.core.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I've fully qualified the `StringContains` class name with its package name `org.hamcrest.core`. This ensures that the correct version of the class is used, even if there are conflicts with other versions of the class in the classpath.