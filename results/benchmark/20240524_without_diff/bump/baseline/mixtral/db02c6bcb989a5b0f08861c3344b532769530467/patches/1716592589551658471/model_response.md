Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.CoreMatchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` class with `org.hamcrest.CoreMatchers.StringContains` to use the correct class from the Hamcrest library.