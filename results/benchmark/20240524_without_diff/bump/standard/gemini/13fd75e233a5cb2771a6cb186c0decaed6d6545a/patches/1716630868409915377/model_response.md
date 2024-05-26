```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    final String digest = this.image.digest();
    return new org.hamcrest.core.StringContains(false, String.format("latest: digest: %s", digest));
}
```