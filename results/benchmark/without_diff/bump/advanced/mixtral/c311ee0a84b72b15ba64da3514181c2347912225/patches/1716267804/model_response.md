Here's a potential patch for the given client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this updated code, we're using the `containsString` method from the `CoreMatchers` class, which takes a single `String` argument. This should resolve the error message indicating that the constructor for `StringContains` expects only one argument.