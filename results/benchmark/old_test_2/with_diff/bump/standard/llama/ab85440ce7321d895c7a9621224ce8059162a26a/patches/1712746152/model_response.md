Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

Becomes:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is using a lambda expression to provide a function that returns the format string, instead of passing the format string directly to the `StringContains` constructor. This avoids the issue of the constructor having been removed in the new version of the library.