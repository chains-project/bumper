Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this version, I have changed the import statement from `org.hamcrest.core.StringContains` to `org.hamcrest.CoreMatchers.StringContains`. This is because the `StringContains` class has been removed from the `org.hamcrest.core` package and added to the `org.hamcrest.CoreMatchers` package in the updated version of the library.

By changing the import statement, we can continue to use the `StringContains` constructor in the same way as before, but without encountering the error message.