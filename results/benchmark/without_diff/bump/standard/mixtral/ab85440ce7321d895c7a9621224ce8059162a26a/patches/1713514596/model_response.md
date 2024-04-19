Here's the patched version of the code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

The original code was using the `StringContains` constructor that takes a `boolean` and a `String`, but the error message indicates that the constructor that takes only a `String` is expected. To fix this, we replace the usage of `StringContains` with `containsString` from `org.hamcrest.CoreMatchers`. This method takes a `String` as its parameter and checks if the provided string contains the specified substring.