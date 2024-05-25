Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.Matchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I changed the import statement from `org.hamcrest.core.StringContains` to `org.hamcrest.Matchers.StringContains`. This is because the `StringContains` constructor is not found in the `org.hamcrest.core` package in the newer version of the library. Instead, it is located in the `org.hamcrest.Matchers` package.

Note that the `Matcher` interface and its `matches` method have not changed, so the rest of the code that uses this method should continue to work as expected.