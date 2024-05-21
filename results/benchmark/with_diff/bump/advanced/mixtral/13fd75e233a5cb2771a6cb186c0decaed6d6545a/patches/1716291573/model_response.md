Here is the proposed patch:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + image);
}
```

In the new version of the library, the `StringContains` constructor no longer accepts a `boolean` argument. Therefore, we can simply remove the first argument `false` and concatenate the string using `+` instead of `String.format()`.