Here's a possible patch for the code:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

In this patch, we create a separate variable `digest` to store the digest of the image, and then pass it to the `StringContains` constructor without the `false` argument. This is possible because the `StringContains` constructor with a single argument is still available in the new library version.