Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor, which is now a lambda expression that formats the string using `String.format`. This avoids the need for the `java.lang.String` parameter in the constructor, which is not applicable due to the incompatible types.