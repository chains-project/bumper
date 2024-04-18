Here's a possible patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.<String>containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we're using the `containsString` method from the `CoreMatchers` class instead of the `StringContains` constructor. This method has the same behavior as the `StringContains` constructor, but it doesn't have the same parameter types, which is why the original code was failing.

Note that `CoreMatchers` is a class from the Hamcrest library, which is a dependency of the project. We're not changing the external dependency, but we're using a different method from the same library to avoid the error.