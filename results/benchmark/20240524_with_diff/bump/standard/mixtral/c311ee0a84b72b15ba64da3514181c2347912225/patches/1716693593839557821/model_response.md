Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.core.StringContains.containsString(
            java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

In this patch, we replaced the `StringContains` constructor with the new `containsString` method added in the newer version of the library. This method only requires a single `String` argument, which matches the expected argument type in the error message.