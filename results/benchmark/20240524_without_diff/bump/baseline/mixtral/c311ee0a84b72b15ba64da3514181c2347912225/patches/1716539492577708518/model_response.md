Here's a possible patch for the given code:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

In this patch, we create a separate variable `digest` for the image digest, and pass it as a single argument to the `StringContains` constructor, which matches the updated library version.