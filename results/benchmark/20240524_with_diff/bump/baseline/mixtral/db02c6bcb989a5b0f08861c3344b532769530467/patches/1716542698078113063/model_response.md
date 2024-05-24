Here's a possible patch for the failing method:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

The change here is that we've extracted the `String.format` call into a separate variable `digest`, and then passed that variable to the `StringContains` constructor. This avoids the issue with the constructor having a different argument list.