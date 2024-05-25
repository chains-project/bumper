Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` class from Hamcrest with the `CoreMatchers.containsString` method from the same library. This method has the same functionality as `StringContains` but is more suitable for the given use case.

Note that the `CoreMatchers` class is part of the Hamcrest library, so it should be already available in the project's classpath. If not, you may need to add a dependency to the Hamcrest library in your project's build configuration.