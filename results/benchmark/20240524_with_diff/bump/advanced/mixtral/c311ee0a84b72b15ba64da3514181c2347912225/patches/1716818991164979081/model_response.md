Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.core.StringStartsWith.startsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
In the new library version, the constructor for `StringContains` no longer accepts a boolean argument. Instead, we can use the `StringStartsWith` matcher, which accepts a single string argument representing the expected prefix. This matcher will check if the actual string starts with the given prefix.