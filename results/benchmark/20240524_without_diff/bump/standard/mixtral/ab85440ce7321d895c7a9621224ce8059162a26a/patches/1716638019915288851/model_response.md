Here's the fixed method:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```
The previous code used the `StringContains` constructor from `org.hamcrest.core` package, which requires a single `String` argument. However, the provided constructor signature in the error message indicates that it requires two arguments: a `boolean` and a `String`.

To fix the issue, I replaced the `StringContains` constructor with the `containsString` method from `org.hamcrest.CoreMatchers`, which accepts a single `String` argument. This should resolve the error and allow the code to compile and run successfully.