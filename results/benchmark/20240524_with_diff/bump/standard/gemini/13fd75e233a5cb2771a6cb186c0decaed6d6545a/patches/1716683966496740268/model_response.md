```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    boolean isLatest = this.image.digest().isPresent();
    String digest = isLatest ? this.image.digest().get() : "unknown";
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", digest));
}
```