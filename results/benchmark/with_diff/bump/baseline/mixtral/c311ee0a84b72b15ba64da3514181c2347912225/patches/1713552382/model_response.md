Here is a possible patch for the code:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

I created a variable `digest` to store the digest of the image, and then I used it to create the `StringContains` matcher. This way, the `StringContains` constructor only receives one argument, which is a string, as required by the new library version.