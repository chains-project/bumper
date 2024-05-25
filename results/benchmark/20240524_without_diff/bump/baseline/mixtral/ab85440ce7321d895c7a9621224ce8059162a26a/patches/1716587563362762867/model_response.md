Here's a potential patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.<String>containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` class with the `containsString` method from the `CoreMatchers` class, which is part of the Hamcrest library and should be available in the version being used. This should resolve the compilation error and allow the code to run successfully.