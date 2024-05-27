Here is a possible patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced the `StringContains` constructor with the `containsString` method from the `Matchers` class, which takes a single `String` argument. This should fix the error message you provided, which indicates that the `StringContains` constructor expects a single `String` argument, but was given a `boolean` and a `String`.