Here's the proposed patch to fix the error:

```java
private Matcher<String> manifestPushed() {
    String digest = this.image.digest();
    return new StringContains(String.format("latest: digest: %s", digest));
}
```

In this patch, I created a new variable `digest` to store the digest of the image. This makes the code easier to read and understand. I then removed the `false` argument from the `StringContains` constructor, as it's not needed and is causing the error. Finally, I concatenated the `digest` variable with the required string format.