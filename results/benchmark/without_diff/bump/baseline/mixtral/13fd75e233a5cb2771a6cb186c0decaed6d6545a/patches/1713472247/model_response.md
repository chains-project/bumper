Here is a fixed version of the `imagePulled` method that uses the `containsString` method from the `StringAssert` class in the Hamcrest library, which is an alternative to the `StringContains` class constructor:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringAssert(String.format("Status: Downloaded newer image for %s", image)).containsString("Status: Downloaded newer image for");
}
```

This code creates a new `StringAssert` object and then calls the `containsString` method on it, passing in the string that we want to check for. This will return a `Matcher` object, just like the original code.

Note that I had to make a guess about the expected format of the string that you are checking for, since it was not specified in the error message. You may need to adjust the argument to the `containsString` method to match the actual format of the string.