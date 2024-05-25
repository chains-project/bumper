Here's the proposed patch to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we've replaced the old import statement for `StringContains` with a fully qualified name, using `org.hamcrest.CoreMatchers.StringContains`. This new constructor should be compatible with the updated version of the Hamcrest library.