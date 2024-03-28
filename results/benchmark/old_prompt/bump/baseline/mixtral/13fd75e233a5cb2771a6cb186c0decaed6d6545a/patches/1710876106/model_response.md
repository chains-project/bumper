I cannot see the full code, but I see the issue is related to the usage of the `StringContains` constructor. Based on the error message, it seems that the constructor that accepts a single `String` argument is not found in the `StringContains` class.

If the desired behavior is to check if the given string contains a substring, you can use the `containsString(String substring)` method instead, which is available in Hamcrest 2.1 and later.

Here's the updated `imagePulled` method with the suggested change:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains().containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

This should resolve the compilation error you're facing.