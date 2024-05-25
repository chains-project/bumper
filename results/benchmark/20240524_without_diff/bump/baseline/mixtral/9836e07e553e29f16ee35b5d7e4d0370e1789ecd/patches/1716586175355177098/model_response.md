Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.Matchers.StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this version, I have fully qualified the `StringContains` class with its package name (`org.hamcrest.Matchers`) to avoid any ambiguity. This should allow the code to compile and run successfully.