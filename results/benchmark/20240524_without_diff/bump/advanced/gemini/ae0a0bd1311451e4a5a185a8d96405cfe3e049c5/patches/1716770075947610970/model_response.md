```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    boolean isLatest = this.image.digest().equals("latest");
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", isLatest ? "latest" : this.image.digest()));
}
```