Here's a possible patch for the failing method:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

The change here is to remove the `false` argument from the `StringContains` constructor, since it's not needed and is causing the error. The `digest()` method is still called on `this.image` to get the digest value.