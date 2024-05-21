Here's the patched version of the code that should work with the new library version:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + image);
}
```

The previous version of the library had a constructor for `StringContains` that took a `boolean` and a `String`, but that constructor has been removed in the new version. Instead, there is a constructor that takes a single `String` argument. Therefore, we can simplify the code by removing the `false` argument and concatenating the strings directly.