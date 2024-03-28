I understand that you're asking for a fixed version of the `imagePulled` method, considering the error message provided. It seems that the `StringContains` constructor is not accepting the given argument types. I'll provide a corrected version of the method using a `Matcher` that checks if the given string contains the desired substring.

Here's the fixed method using a `CoreMatchers.containsString()` method from Hamcrest, which is an added method identified with `++`:

```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This fixed version uses the `CoreMatchers.containsString()` method, which checks if the given string contains the specified substring. This should resolve the compilation error you encountered.