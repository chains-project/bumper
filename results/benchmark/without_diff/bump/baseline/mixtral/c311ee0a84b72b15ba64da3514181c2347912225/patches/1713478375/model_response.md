Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
The issue was caused by the use of a string format inside the `containsString` method. Instead, we can format the string first and then use the formatted string in the `containsString` method. This should resolve the reported error.