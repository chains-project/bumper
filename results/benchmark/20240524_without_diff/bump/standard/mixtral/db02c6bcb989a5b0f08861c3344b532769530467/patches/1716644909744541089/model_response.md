Here is a possible patch for the code you provided:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.startsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
This patch uses the `startsWith` method from the `CoreMatchers` class, which takes a single `String` argument, instead of the `StringContains` constructor, which takes a `boolean` and a `String`. This should fix the error you were seeing about the constructor having the wrong number of arguments.