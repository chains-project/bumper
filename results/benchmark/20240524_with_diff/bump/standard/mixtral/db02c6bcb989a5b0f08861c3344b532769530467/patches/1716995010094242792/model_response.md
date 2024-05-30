Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but the updated library version only accepts one argument. I have removed the first argument `false` to make the code compatible with the updated library version.