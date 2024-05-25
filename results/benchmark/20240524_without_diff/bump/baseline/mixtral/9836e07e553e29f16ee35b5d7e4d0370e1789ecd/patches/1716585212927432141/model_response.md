Here's the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced `org.hamcrest.core.StringContains` with `org.hamcrest.CoreMatchers.StringContains`. It seems that the `StringContains` class has been moved from the `org.hamcrest.core` package to the `org.hamcrest.CoreMatchers` package in the newer version of the library.