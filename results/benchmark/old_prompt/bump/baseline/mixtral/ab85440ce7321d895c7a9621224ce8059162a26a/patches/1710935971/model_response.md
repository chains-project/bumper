Based on the error message, it seems like the `StringContains` constructor is not accepting the provided argument. This might be due to the addition of a new constructor in the new version of the library that has different arguments.

To fix this issue, we can use the `containsString` method from the `org.hamcrest.CoreMatchers` class instead of the `StringContains` constructor. This method is marked with `++` which means it is a new method added in the new version of the library.

Here's the updated code:

```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This code creates a matcher that checks if the given string contains the specified substring. In this case, it checks if the log message "Status: Downloaded newer image for [image]" is present in the response.