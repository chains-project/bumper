```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    boolean digest = this.image.digest();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", String.valueOf(digest)));
}
```