Here is a possible patch for the given error:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

The patch creates a new variable `digest` to store the digest of the image, and uses it to create the `StringContains` matcher. This avoids the error caused by the updated `StringContains` constructor, which now only takes a single `String` argument.