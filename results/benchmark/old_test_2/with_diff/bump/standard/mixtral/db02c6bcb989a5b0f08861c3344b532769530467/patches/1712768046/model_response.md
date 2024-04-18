Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.MatcherAssert.assertThat(image, new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```

The patch uses the new `MatcherAssert.assertThat` method added in the new library version to replace the old `new StringContains` constructor, which has been removed. This should fix the error caused by the dependency update.