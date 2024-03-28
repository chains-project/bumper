Here's a patch for the failing client code:
```java
private static Matcher<String> imagePulled(final String image) {
    String successMessage = String.format("Status: Downloaded newer image for %s", image);
    return is(containsString(successMessage));
}
```
The issue with the original code is that it is trying to use `is()` method with `containsString()` method, which is not supported. Instead, we create a separate variable `successMessage` to store the string and pass it to `containsString()` method. This will achieve the desired functionality without any errors.