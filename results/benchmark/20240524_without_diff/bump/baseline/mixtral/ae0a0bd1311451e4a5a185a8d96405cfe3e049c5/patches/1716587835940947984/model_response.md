Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` class from `org.hamcrest.core` with the `containsString` method from `org.hamcrest.CoreMatchers`. This should fix the error message you provided, which indicates that the `StringContains` constructor cannot be applied to the given arguments.

Note that this patch assumes that the `CoreMatchers` class is available in the classpath. If it's not, you may need to add a dependency to your project to include it.