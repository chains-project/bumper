```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    boolean isLatest = this.image.digest().isPresent() && this.image.digest().get().equals(this.image.tag());
    String digest = isLatest ? "latest" : this.image.digest().get();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("digest: %s", digest));
}
```