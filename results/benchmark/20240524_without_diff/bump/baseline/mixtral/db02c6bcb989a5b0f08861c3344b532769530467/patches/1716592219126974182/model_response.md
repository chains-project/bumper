Here's the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.Matchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor from `org.hamcrest.core` with the one from `org.hamcrest.Matchers`. This is because the `StringContains` constructor from `org.hamcrest.core` has been removed in the new version and replaced with a static method. The `StringContains` constructor from `org.hamcrest.Matchers` still exists and can be used instead.