Here's the fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String containsString = String.format("Downloaded newer image for %s", image);
    return new StringContains(containsString);
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but the constructor now only accepts a single argument. To fix the error, we need to pass only the string that we want to check for as a single argument. In this case, we extract the string that we want to check for into a separate variable `containsString` and pass it as an argument to the `StringContains` constructor.