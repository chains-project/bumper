Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the equivalent `stringContains` constructor from the `CoreMatchers` class, which is a new addition in the Hamcrest library. This should resolve the compilation error.