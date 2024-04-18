Here's a potential patch for the code to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor from the `org.hamcrest.core` package with the `containsString` method from the `org.hamcrest.CoreMatchers` package. The `containsString` method is a new addition in the external dependency, which can be used as a replacement for the deprecated `StringContains` constructor.