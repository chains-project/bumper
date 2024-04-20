Here is the patched method that should fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

The error message indicates that the `StringContains` constructor now requires only one argument, instead of two. The `Matchers.containsString` method is a new addition in the library that can be used as a replacement.