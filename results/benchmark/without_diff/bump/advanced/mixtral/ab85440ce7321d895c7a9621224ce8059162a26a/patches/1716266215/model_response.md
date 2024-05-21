Here's a possible patch for the given client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```
The patch uses the `containsString` method from the `CoreMatchers` class, which takes a single `String` argument. This method is an alternative to the `StringContains` constructor, which has been deprecated.