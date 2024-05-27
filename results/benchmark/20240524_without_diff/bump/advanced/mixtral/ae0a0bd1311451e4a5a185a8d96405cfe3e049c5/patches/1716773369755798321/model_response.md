Here is a potential patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which only takes a single `String` argument, instead of the `StringContains` constructor which takes a `boolean` and a `String`. This should resolve the error message you provided.