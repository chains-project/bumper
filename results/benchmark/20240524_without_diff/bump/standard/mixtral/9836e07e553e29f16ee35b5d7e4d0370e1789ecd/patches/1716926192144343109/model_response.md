Here is a possible patch for the code you provided:
```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("latest: digest: %s", this.image.digest()));
}
```
This patch uses the `StringStartsWith` matcher from Hamcrest instead of `StringContains`. The `StringStartsWith` matcher only takes a single argument (the string to compare against), so it avoids the error you were seeing with the `StringContains` matcher.

Note that this patch assumes that you want to check if the manifest string starts with the digest of the image. If you actually want to check if the manifest string contains the digest (but not necessarily at the beginning), you may need to use a different matcher or a combination of matchers.