```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    String digest = image.digest();
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", digest));
}
```