Here is the updated `imagePulled` method that should resolve the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePargtner(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

This updated code uses the new `containsString` method from the updated library, which takes a single `String` argument. This should resolve the issue with the constructor for `StringContains` not accepting the required arguments.