```java
private org.hamcrest.Matcher<String> manifestPushed() {
    return new org.hamcrest.core.StringContains(false, String.format("latest: digest: %s", this.image.digest()));
}
```