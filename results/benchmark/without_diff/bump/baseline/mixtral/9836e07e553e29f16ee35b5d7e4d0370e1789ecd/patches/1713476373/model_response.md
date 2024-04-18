Here is a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we replaced the `StringContains` class with the `containsString` method from the `org.hamcrest.CoreMatchers` class, which is a more appropriate way to check if a string contains a substring in Hamcrest.

Note that this patch assumes that the `CoreMatchers` class is available in the classpath. If it is not, you may need to add a dependency to the project's build configuration.