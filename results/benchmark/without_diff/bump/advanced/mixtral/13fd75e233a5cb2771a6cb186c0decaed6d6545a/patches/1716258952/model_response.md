Here is a possible patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The patch uses the `containsString` method from the `CoreMatchers` class, which takes a single `String` argument, instead of the `StringContains` constructor, which takes a `boolean` and a `String`. This should fix the error message you provided.