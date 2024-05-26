```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return new org.hamcrest.core.StringContains(String.format("latest: digest: %s", this.image.digest()));
}
```