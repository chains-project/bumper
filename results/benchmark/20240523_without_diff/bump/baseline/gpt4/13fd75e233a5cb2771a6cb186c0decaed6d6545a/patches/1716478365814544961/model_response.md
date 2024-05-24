```java
private Matcher<String> manifestPushed() {
    return new org.hamcrest.core.StringContains(String.format("latest: digest: %s", this.image.digest()));
}
```