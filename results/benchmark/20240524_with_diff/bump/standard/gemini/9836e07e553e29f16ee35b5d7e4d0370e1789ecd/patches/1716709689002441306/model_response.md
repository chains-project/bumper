```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    String digest = this.image.digest();
    String format = String.format("latest: digest: %s", digest);
    return new org.hamcrest.core.StringContains(false, format);
}
```