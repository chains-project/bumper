Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor, which is now a lambda expression that formats the string using the `String.format` method. This avoids the need for the `java.lang.String` parameter, which is no longer available in the updated library version.